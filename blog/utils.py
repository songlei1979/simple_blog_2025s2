import os
from os import getenv
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = getenv("SENDGRID_KEY")

def send_email(to_email, subject, html_content):
    message = Mail(
        from_email="hebei.stu01@gmail.com",
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_KEY"))
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        return str(e)