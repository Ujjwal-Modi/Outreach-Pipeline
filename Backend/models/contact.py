from dataclasses import dataclass


@dataclass
class Contact:
    company: str
    domain: str
    name: str
    title: str
    linkedin_url: str
    email: str | None = None
    person_id: str | None = None