import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "ldetermination7@gmail.com"
password = "zrsxkhwyxncmarqf"
receiver = "4clover0@gmail.com"

message = """
Hi!
how are you?
!!!
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username,receiver, message)