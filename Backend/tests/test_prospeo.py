from pprint import pprint
from dataclasses import asdict

from services.prospeo import ProspeoClient


def main():
    client = ProspeoClient()

    domain = "brex.com"

    print(f"\nSearching decision makers for {domain}...\n")

    contacts = client.get_decision_makers(domain)

    print("\n" + "=" * 60)
    print("DECISION MAKERS")
    print("=" * 60)

    for i, contact in enumerate(contacts[:10], start=1):
        print(f"\nCONTACT #{i}")
        pprint(asdict(contact))

    print("\n" + "=" * 60)
    print("COMPACT VIEW")
    print("=" * 60)

    for i, contact in enumerate(contacts[:10], start=1):
        print(
            f"{i}. "
            f"{contact.name} | "
            f"{contact.title} | "
            f"{contact.email} | "
            f"{contact.linkedin_url}"
        )

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    total_contacts = len(contacts)

    contacts_with_email = [
        c for c in contacts
        if c.email
    ]

    print(f"Total Contacts      : {total_contacts}")
    print(f"Contacts With Email : {len(contacts_with_email)}")

    if total_contacts:
        coverage = (
            len(contacts_with_email)
            / total_contacts
            * 100
        )

        print(f"Email Coverage      : {coverage:.1f}%")

    print("=" * 60)


if __name__ == "__main__":
    main()