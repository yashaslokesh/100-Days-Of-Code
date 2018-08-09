from twilio.rest import Client
import json
import os
import sys

sys.path.append('/Users/lokeshkrishnappa/Desktop/python-projects/100-Days-Of-Code/Python')

account_SID = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(account_SID, auth_token)
with open("supporting_files/details.json") as details:
    json_data = json.loads(details.read())
    twilio_number = json_data["TwilioNumber"]

my_number = "+1" + input("Enter your number, with no spaces or extra characters: ")

from d002_email_accessor import email_accessor

message_body = "You received email from these organizations/people in your gmail inbox today:"

for name in email_accessor.senders_dict:
    message_body += f"\n{name}"

message = client.messages.create(body = f"{message_body}", 
                                from_ = twilio_number, to = my_number)