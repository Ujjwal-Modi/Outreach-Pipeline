import os
import requests
from dotenv import load_dotenv

load_dotenv()


class OceanClient:
    def __init__(self):
        self.api_key = os.getenv("OCEAN_API_KEY")
        self.url = "https://api.ocean.io/v3/search/companies"

    def get_similar_companies(self, domain):
        headers = {
            "x-api-token": self.api_key,
            "Content-Type": "application/json"
        }

        payload = {
            "size": 10,
            "companiesFilters": {
                "lookalikeDomains": [domain]
            },
            "fields": [
                "domain",
                "name"
            ]
        }

        response = requests.post(
            self.url,
            headers=headers,
            json=payload
        )

        response.raise_for_status()

        data = response.json()

        companies = []

        for item in data.get("companies", []):
            company = item.get("company", {})

            companies.append({
                "domain": company.get("domain"),
                "name": company.get("name")
            })

        return companies