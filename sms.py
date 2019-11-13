from twilio.rest import Client
import secrets

class Texter:
    def __init__(self):
        self.client = Client(secrets.TWILIO_SID, secrets.TWILIO_AUTH_TOKEN)

    def send(self, message):
        self.client.messages.create(to=secrets.TO_NUMBER,
                               from_=secrets.FROM_NUMBER,
                               body=message)