"""Send an SMS file with Twilio."""

from twilio.rest import Client
from auth import (
    account_sid,
    auth_token,
    sendee_phones,
    sender_phone
)


class SmsService(Client):
    """Simplify the Twilio stuff."""

    def send_message(self, to_num, from_num, message):
        """Send a text message with SMS."""
        return self.messages.create(to=to_num, from_=from_num, body=message)

if __name__ == '__main__':
    to_number = '+%s' % sendee_phones[0]['number']
    from_number = '+%s' % sender_phone
    message = 'Hello, this is test message from Lutra'

    sms_service = SmsService(account_sid, auth_token)
    sms_service.send_message(to_number, from_number, message)
