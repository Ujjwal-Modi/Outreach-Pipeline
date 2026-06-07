import os
import uuid
import requests

from dotenv import load_dotenv

load_dotenv()


class BrevoClient:
    def __init__(self):
        self.api_key = os.getenv("BREVO_API_KEY")

        self.url = "https://api.brevo.com/v3/smtp/email"

        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": self.api_key
        }

        self.sender = {
            "name": os.getenv("FROM_NAME"),
            "email": os.getenv("FROM_EMAIL")
        }

    def send_batch(self, contacts):
        """
        Send personalized outreach emails using Brevo.
        """

        message_versions = []

        for contact in contacts:

            if not contact.email:
                continue

            html_content = f"""
            <html>
            <body>

            <p>Hi {contact.name},</p>

            <p>
            I noticed you're working as <strong>{contact.title}</strong>
            at <strong>{contact.company}</strong>.
            </p>

            <p>
            We help teams automate:
            </p>

            <ul>
                <li>Prospect discovery</li>
                <li>Decision-maker identification</li>
                <li>Email verification</li>
                <li>Personalized outreach</li>
            </ul>

            <p>
            I thought this could be relevant if you're exploring
            ways to improve outbound prospecting and lead generation.
            </p>

            <p>
            Would you be open to a quick conversation?
            </p>

            <p>
            Regards,<br>
            Ujjwal Modi
            </p>

            </body>
            </html>
            """

            message_versions.append(
                {
                    "to": [
                        {
                            "email": contact.email,
                            "name": contact.name
                        }
                    ],
                    "subject": f"Quick idea for {contact.company}",
                    "htmlContent": html_content
                }
            )

        if not message_versions:
            print("No valid recipients found.")
            return {
                "success": False,
                "message": "No recipients with valid emails"
            }

        payload = {
            "sender": self.sender,
            "subject": "Outreach",
            "htmlContent": "<html><body>Default</body></html>",
            "headers": {
                "idempotencyKey": str(uuid.uuid4())
            },
            "messageVersions": message_versions
        }

        print(
            f"Sending {len(message_versions)} email(s) via Brevo..."
        )

        response = requests.post(
            self.url,
            headers=self.headers,
            json=payload,
            timeout=60
        )

        if not response.ok:
            print("\n========== BREVO ERROR ==========")
            print("Status:", response.status_code)
            print("Response:", response.text)
            print("=================================\n")
            response.raise_for_status()

        result = response.json()

        print("\n========== BREVO SUCCESS ==========")
        print(result)
        print("===================================\n")

        return result