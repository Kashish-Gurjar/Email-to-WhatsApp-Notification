import smtplib
from twilio.rest import Client
import openai

# Function to generate dynamic email content using AI (GPT-3)
def generate_ai_content():
    openai.api_key = 'your_openai_api_key'  # Replace with your OpenAI API key

    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-3 model
        prompt="Generate a polite email message about the latest product update.",
        max_tokens=100  # Limit the response length
    )

    generated_text = response.choices[0].text.strip()  # Get the AI-generated text
    return generated_text

# Function to send an email
def send_email():
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@example.com"
    password = "your_email_password"

    subject = "Product Update"
    body = generate_ai_content()  # Generate email content using AI

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, receiver_email, message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to send a WhatsApp message
def send_whatsapp_message():
    account_sid = 'your_account_sid'  # Twilio SID
    auth_token = 'your_auth_token'  # Twilio Auth Token

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Here is a new update from our team!",  # WhatsApp message content
        from_='whatsapp:+14155238886',  # Twilio WhatsApp sandbox number
        to='whatsapp:+91xxxxxxxxxx'  # Recipient's WhatsApp number
    )

    print(f"Message sent: {message.sid}")

# Send email
send_email()

# Send WhatsApp message
send_whatsapp_message()
