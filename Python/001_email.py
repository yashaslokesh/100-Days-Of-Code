import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import getpass

"""
    We start an SMTP server with gmail (the 587 is a port number). smtp_mailer.ehlo() sends a command to the server to identify ourselves. The smtplib documentation says we don't need to call the ehlo() function explicitly, but we'll do it anyway for reference and just to make sure we understand kind of what happens in the smtplib module. We then use smtp_mailer.starttls() to start the TLS protocol, to allow the emails to be sent securely.
"""
smtp_mailer = smtplib.SMTP("smtp.gmail.com", 587)
smtp_mailer.ehlo()
smtp_mailer.starttls()

"""
    Load and use details.json to prefill some fields in the email message that is eventually sent, makes it easier for testing.
"""
with open("supporting_files/details.json") as details:
    json_data = json.loads(details.read())
    user_email = json_data["MyEmail"]

# Always asks for user password instead of storing, for security
user_password = getpass.getpass(f"Enter the password for {user_email} (The password will not show "                                "up for security purposes): ")

smtp_mailer.login(user_email, user_password)
print("Login successful")

message = MIMEMultipart()

message["From"] = user_email
message["To"] = json_data["To"]
message["Subject"] = json_data["Subject"]

email_body = json_data["Body"]

message.attach(MIMEText(email_body, "plain"))

smtp_mailer.send_message(message)
smtp_mailer.quit()
