import smtplib

from email.message import EmailMessage

smtp_mailer = smtplib.SMTP("smtp.gmail.com", 587)
smtp_mailer.ehlo()
smtp_mailer.starttls()

user_email = input("What is your email address?")
user_password = input("What is your password?")

smtp_mailer.login(user_email, user_password)
print("Login successful")

message = EmailMessage()
message.set_content("")

message["From"] = user_email

send_email = input("What is the email address of the receiving party?")

message["To"] = send_email

message["Subject"] = input("What would you like to say in the email?")

smtp_mailer.send_message(message)
smtp_mailer.quit()
