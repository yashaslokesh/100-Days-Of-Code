import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

smtp_mailer = smtplib.SMTP("smtp.gmail.com", 587)
smtp_mailer.ehlo()
smtp_mailer.starttls()

with open("details.json") as details:
    json_data = json.loads(details.read())
    user_email = json_data["MyEmail"]

user_password = input(f"Enter the password for {user_email}: ")

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
