import smtplib
import ssl


def mail_sender(message = "Hello"):
    host = "smtp.gmail.com"
    port = 465

    user_name = "utkarsh.09914021@gmail.com"
    password = "lcvb cxmp kagb lnoj"

    receiver = "utkarsh.09914021@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)

