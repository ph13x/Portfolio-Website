import smtplib, ssl


def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465

    username = "ldetermination7@gmail.com"
    password = "zrsxkhwyxncmarqf"
    receiver = "4clover0@gmail.com"

    message = user_message


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver, message)