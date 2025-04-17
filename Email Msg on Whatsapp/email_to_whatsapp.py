import imaplib
import email
from email.header import decode_header
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twilio credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp = os.getenv("TWILIO_WHATSAPP_NUMBER")
to_whatsapp = os.getenv("TO_WHATSAPP_NUMBER")

# Email credentials
EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

# Connect to email server
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, PASSWORD)
mail.select("inbox")

# Get latest email
status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()
latest_email_id = email_ids[-1]

# Fetch email
res, msg_data = mail.fetch(latest_email_id, "(RFC822)")
msg = email.message_from_bytes(msg_data[0][1])
subject = decode_header(msg["Subject"])[0][0]
if isinstance(subject, bytes):
    subject = subject.decode()

# Body
if msg.is_multipart():
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True).decode()
            break
else:
    body = msg.get_payload(decode=True).decode()

# Twilio send message
client = Client(account_sid, auth_token)
text = f"📧 Email Received!\nSubject: {subject}\n\n{body[:100]}..."  # Trimmed preview

message = client.messages.create(
    body=text,
    from_=from_whatsapp,
    to=to_whatsapp
)

print("WhatsApp message sent!")
