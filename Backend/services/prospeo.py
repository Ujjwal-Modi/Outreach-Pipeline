import os
import requests
import time

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv

from models.contact import Contact

load_dotenv()


class ProspeoClient:
    def __init__(self):
        self.api_key = os.getenv("PROSPEO_API_KEY")

        self.session = requests.Session()

        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )

        self.session.mount(
            "https://",
            HTTPAdapter(max_retries=retries)
        )

    def search_people(self, domain: str, page: int = 1):
        """
        Search decision makers for a company domain.
        """

        url = "https://api.prospeo.io/search-person"

        headers = {
            "X-KEY": self.api_key,
            "Content-Type": "application/json"
        }

        payload = {
            "page": page,
            "filters": {
                "company": {
                    "websites": {
                        "include": [domain]
                    }
                },
                "person_seniority": {
                    "include": [
                        "Founder/Owner",
                        "C-Suite",
                        "Vice President"
                    ]
                }
            }
        }

        response = self.session.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def search_all_people(self, domain: str):
        """
        Fetch all pages from Prospeo.
        """

        page = 1
        all_results = []

        while True:

            data = self.search_people(
                domain=domain,
                page=page
            )

            people = data.get("results", [])

            if not people:
                break

            all_results.extend(people)

            pagination = data.get("pagination", {})
            total_pages = pagination.get("total_page", 1)

            if page >= total_pages:
                break

            if page < total_pages:
                time.sleep(1.2)

            page += 1

        return all_results

    def normalize_contacts(self, results):
        """
        Convert Prospeo response into Contact objects.
        """

        contacts = []

        for item in results:

            person = item.get("person", {})
            company = item.get("company", {})

            contact = Contact(
                company=company.get("name", ""),
                domain=company.get("domain", ""),
                name=person.get("full_name", ""),
                title=person.get("current_job_title", ""),
                linkedin_url=person.get("linkedin_url", ""),
                email=None,
                person_id=person.get("person_id")
            )

            contacts.append(contact)

        return contacts

    def deduplicate_contacts(self, contacts):
        """
        Remove duplicate contacts.
        """

        unique = []
        seen = set()

        for contact in contacts:

            key = (
                contact.company,
                contact.linkedin_url
            )

            if key in seen:
                continue

            seen.add(key)
            unique.append(contact)

        return unique

    def enrich_contacts(self, contacts):

        if not contacts:
            return []

        url = "https://api.prospeo.io/enrich-person"

        headers = {
            "X-KEY": self.api_key,
            "Content-Type": "application/json"
        }

        enriched_contacts = []

        for contact in contacts:

            if not contact.person_id:
                continue

            payload = {
                "only_verified_email": True,
                "data": {
                    "person_id": contact.person_id
                }
            }

            response = self.session.post(
                url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 429:

                reset_seconds = int(
                    response.headers.get(
                        "x-second-reset-seconds",
                        1
                    )
                )

                print(
                    f"Rate limited. Waiting "
                    f"{reset_seconds + 1}s..."
                )

                time.sleep(reset_seconds + 1)

                response = self.session.post(
                    url,
                    headers=headers,
                    json=payload,
                    timeout=30
                )

            if response.status_code != 200:
                print(
                    f"Failed enrichment for "
                    f"{contact.name}"
                )
                print(response.text)
                continue

            result = response.json()

            person = result.get("person", {})
            email_data = person.get("email", {})

            email = email_data.get("email")

            if email:
                contact.email = email
                enriched_contacts.append(contact)

            # Respect Prospeo free-plan limit
            time.sleep(1.2)

        return enriched_contacts

    def get_decision_makers(self, domain: str):
        """
        Main method used by pipeline.
        """

        raw_results = self.search_all_people(domain)
        print(f"RAW RESULTS: {len(raw_results)}")

        contacts = self.normalize_contacts(raw_results)
        print(f"NORMALIZED: {len(contacts)}")

        contacts = self.deduplicate_contacts(contacts)
        print(f"DEDUPED: {len(contacts)}")

        contacts = contacts[:2]
        
        contacts = self.enrich_contacts(contacts)
        print(f"EMAILS FOUND: {len(contacts)}")

        return contacts