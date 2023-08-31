import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "larsondg2000@gmail.com"
    password = "PASSWORD"

    receiver = "larsondg2000@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



"""
store passwords securely:
Import os
cut password
password = os.getenv("PASSWORD")
in windows got environment variables
click new
variable is any name but we use PASSWORD here
value should be the password set up in gmail like below
password = "gwtjvoygfdljdpdm"

pyinstaller --onefile --windowed --clean file.py
"""
