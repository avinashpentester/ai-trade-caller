# alerts/whatsapp_bot.py
from twilio.rest import Client
import os
from dotenv import load_dotenv
from config import TWILIO_WHATSAPP_FROM, TWILIO_WHATSAPP_TO

load_dotenv()

def send_whatsapp_message(body):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=body,
            from_=TWILIO_WHATSAPP_FROM,
            to=TWILIO_WHATSAPP_TO
        )
        print(f"📲 WhatsApp message sent: SID {message.sid}")
    except Exception as e:
        print(f"❌ WhatsApp message failed: {e}")