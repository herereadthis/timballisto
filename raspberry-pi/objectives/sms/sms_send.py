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

    def format_number(self, number):
        """Format a number that Twilio can use."""
        # Expand on this in the future, including regex validation
        return '+%s' % number

    def set_from_number(self, from_num):
        """Set the number from which the message will go."""
        self.from_number = self.format_number(from_num)

    def set_to_number(self, to_num):
        """Set the number to which the message will go."""
        self.to_number = self.format_number(to_num)

    def send_message(self, message):
        """Send a text message with SMS."""
        try:
            self.messages.create(
                to=self.to_number,
                from_=self.from_number,
                body=message
            )
        except NameError as e:
            print(e)


if __name__ == '__main__':
    sms_service = SmsService(account_sid, auth_token)
    sms_service.set_from_number(sender_phone)
    sms_service.set_to_number(sendee_phones[0]['number'])
    message = 'Hello, this is test message from Lutra'

    sms_service.send_message(message)
