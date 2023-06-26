import os
import smtplib
import ssl
from email.message import EmailMessage

# credentials
PASSWORD = os.environ.get("PASSWORD")
sender_gmail = os.environ.get("MAIL_ID")


def send_mail(mail_id: str):
    PORT = 465
    HOST = "smtp.gmail.com"

    subject = "Successfully Working with SMTP"
    body = """Dear Friend,
    
I hope this email finds you well. I wanted to share some exciting news with you—I have successfully implemented the Simple Mail Transfer Protocol (SMTP) to send emails programmatically!
    
Warm regards,
Urvish Patel
"""

    mail = EmailMessage()
    mail["From"] = sender_gmail
    mail["Subject"] = subject
    mail["To"] = mail_id
    mail.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(HOST, PORT, context=context) as smtp:
        smtp.login(sender_gmail, PASSWORD)
        smtp.sendmail(sender_gmail, mail_id, mail.as_string())


mail_list = ["urvishp45003@gmail.com",
             "kahan2607@gmail.com",
             "jalvrund2017@gmail.com",
             "medivyapatel27@gmail.com",
             ]

for i in mail_list:
    send_mail(i)
