from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()


class NotificationManager:
    def send_sms(self, message_content):
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+12184323195',
            body=message_content,
            to='+918737969494'
        )

        print(message.status)
