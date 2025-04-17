# from twilio.rest import Client

# # Twilio credentials (yaha apna real Account SID aur Auth Token daalo)
# account_sid = 'AC2962ebca189a9051b3edb240c70cc0be'   # <-- Yaha apna Account SID paste karo
# auth_token = '95ee5748cc68167450c78fc6a67e2d6c'          # <-- Yaha apna Auth Token paste karo
# client = Client(account_sid, auth_token)

# # Message bhejna

#  text = input("Hello This Side Kashish Gurjar ")
#  message = client.messages.create(
#     from_='whatsapp:+14155238886', # Twilio Sandbox WhatsApp number
#     body=text,
#     to='whatsapp:+919131736172'             # <-- Yaha apna WhatsApp number likho (e.g. +919876543210)
# )

# print(f"Message sent: {message.sid}")






from twilio.rest import Client

# Twilio credentials
account_sid = 'AC2962ebca189a9051b3edb240c70cc0be'
auth_token = '95ee5748cc68167450c78fc6a67e2d6c'
client = Client(account_sid, auth_token)

# User input le lo
text = input("Kya message bhejna hai?")

# Message bhejna
message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=text,
    to='whatsapp:+919131736172'  # <-- apna WhatsApp number likhna (e.g. +919876543210)
)

print("✅ Message bhej diya gaya hai WhatsApp pe!")
