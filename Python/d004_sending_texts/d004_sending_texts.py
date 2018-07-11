from twilio.rest import Client
import json

account_SID = "ACa7a85e5b259c5d97173ffe0248b396e0"
auth_token = input("Input the Twilio authorization token: ")

client = Client(account_SID, auth_token)
with open("../supporting_files/details.json") as details:
    json_data = json.loads(details.read())
    twilio_number = json_data["TwilioNumber"]

my_number = "+1" + input("Enter your number, with no spaces or extra characters: ")

import d002_email_accessor

message_body = "You received email from these organizations/people in your gmail inbox today:"

for name in d002_email_accessor.senders_dict:
    message_body += f"\n{name}"

message = client.messages.create(body = f"{message_body}", 
                                from_ = twilio_number, to = my_number)