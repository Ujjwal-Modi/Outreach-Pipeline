from models.contact import Contact
from services.brevo import BrevoClient

contacts = [
    Contact(
        company="Vocallabs",
        domain="vocallabs.com",
        name="Test User",
        title="CEO",
        linkedin_url="",
        email="ujjawalmodi321@gmail.com"
    )
]

client = BrevoClient()

result = client.send_batch(contacts)

print(result)