import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_mailer = smtplib.SMTP("smtp.gmail.com", 587)
smtp_mailer.ehlo()
smtp_mailer.starttls()

user_email = input("What is your email address?")
user_password = input("What is your password?")

smtp_mailer.login(user_email, user_password)
print("Login successful")

message = MIMEMultipart()

message["From"] = user_email
message["To"] = input("What is the email address of the receiving party?")
message["Subject"] = input("What is the subject of your email?")

email_body = input("What would you like to say in your email?")

message.attach(MIMEText(email_body, "plain"))

smtp_mailer.send_message(message)
smtp_mailer.quit()
