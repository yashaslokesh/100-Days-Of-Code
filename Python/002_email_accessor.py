import imapclient
import json
import datetime
import imaplib
import pyzmail
import getpass

# Load file with login details
with open("details.json") as details:
    jsonData = json.loads(details.read())
    user_email = jsonData["MyEmail"]

# Start imapclient, that will be used to retrieve messages
imap = imapclient.IMAPClient("imap.gmail.com", ssl=True)

# Ask for password, never store
user_password = getpass.getpass(f"Enter the password for {user_email} (The password will not show "                                "up for security purposes): ")

imap.login(user_email, user_password)
print("Login successful")

imap.select_folder("INBOX", readonly=False) # Select only the inbox, for testing

today_date = datetime.datetime.today()

email_UIDs = imap.search([u'SINCE', today_date]) # search for all of the emails from today...

unprocessed_messages = imap.fetch(email_UIDs, ["BODY[]"]) # Retrieve messages using the email UIDs

imap.logout() # Log out of IMAP server, all messages already retrieved

# Create dictionary for storing email addresses and the address's owner's names
senders_dict = dict()

""" 
    Add the email sender's name and email address by processing the "BODY[]" element of the email, 
    using pyzmail. I found out about this module when a friend was talking to me about learning to code with "Automate the Boring Stuff with Python" by Al Sweigart. The .get_addresses("from")method returns a single-element list of a two-element tuple, and by accessing this tuple, I can add the sender's name and email address to my final dictionary.
"""
for uid in email_UIDs:
    message = pyzmail.PyzMessage.factory(unprocessed_messages[uid][b"BODY[]"])
    from_list = message.get_addresses("from")
    senders_dict[f"{from_list[0][0]}"] = f"{from_list[0][1]}"

""" 
    Create a formatted string from the datetime object for today. Used to update the same file if
    this script is run multiple times a day. In the future days of code, I hope to add an auto-replier based on the type of email, or on other criteria.
"""
today_formatted = datetime.datetime.today().strftime("%m-%d-%Y")

"""
    Comment out the next 3 lines of code below if you'd like to NOT save the list of organizations/people who sent you emails for today. That is, if they should not be saved into your local files, and should only be viewed in the console. If you'd like to disable viewing the addresses in the console, comment out the very last line.
"""

with open(f"emails_senders_{today_formatted}.json", "w") as emails:
    senders_json_data = json.dumps(senders_dict, indent=3, sort_keys=True)
    emails.write(senders_json_data)

print(senders_json_data)
