import smtplib
import ssl
import os
import certifi
context = ssl.create_default_context(cafile=certifi.where())

def mail_sender(message = "Hello"):
    host = "smtp.gmail.com"
    port = 465

    user_name = os.getenv("USER_NAME_1")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("USER_NAME_1")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)

