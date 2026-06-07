from services.ocean import OceanClient
from services.prospeo import ProspeoClient
from services.brevo import BrevoClient
from models.contact import Contact


MAX_COMPANIES = 2


def preview_pipeline(
    domain: str,
):

    ocean = OceanClient()
    prospeo = ProspeoClient()

    print("\nSTEP 1: Finding similar companies...\n")

    companies = ocean.get_similar_companies(domain)

    companies = companies[:MAX_COMPANIES]

    print(f"Companies Found: {len(companies)}")

    all_contacts = []
    print("\nSTEP 2: Finding decision makers...\n")

    for company in companies:

        company_name = company.get("name")
        company_domain = company.get("domain")

        if not company_domain:
            continue

        print(
            f"\nProcessing: "
            f"{company_name} ({company_domain})"
        )

        try:

            contacts = prospeo.get_decision_makers(
                company_domain
            )

            print(
                f"Found {len(contacts)} contacts"
            )

            all_contacts.extend(contacts)

        except Exception as e:

            print(
                f"Failed for {company_name}: {e}"
            )

    return {
    "input_domain": domain,
    "companies_found": len(companies),
    "contacts_found": len(all_contacts),
    "companies": companies,
    "contacts": [
        {
            "company": c.company,
            "domain": c.domain,
            "name": c.name,
            "title": c.title,
            "linkedin_url": c.linkedin_url,
            "email": c.email,
            "person_id": c.person_id
        }
        for c in all_contacts
    ]
    }

def send_emails(contacts_data):

    contacts = []

    for c in contacts_data:
        contacts.append(
            Contact(
                company=c["company"],
                domain=c["domain"],
                name=c["name"],
                title=c["title"],
                linkedin_url=c["linkedin_url"],
                email=c.get("email"),
                person_id=c.get("person_id")
            )
        )

    brevo = BrevoClient()

    return brevo.send_batch(contacts)