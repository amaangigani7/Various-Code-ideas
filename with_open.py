import smtplib, email, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase


def check_name(file, name):
    present = False
    s = name.lower()
    with open(file, 'r') as lis:
        for line in lis:
            if s in line:
                present = True
                break
        if not present:
            with open(file, 'a') as f:
                f.writelines(s)
                f.writelines('\n')


def send_email(file):
    mail_content = '''Welcome to Raymond Mark Series'''
    sender_address = 'raymondmarkseries@gmail.com'
    sender_pass = '#Raymond@Mark_500'
    body = 'You are receiving this because you have subscribed the series on the website'

    message = MIMEMultipart()
    message['From'] = sender_address
    message['Subject'] = "Welcome to this page"
    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    with open(file, 'r') as email_file:
        for line in email_file:
            receiver_address = line

            message['To'] = receiver_address
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_address, sender_pass)
                server.sendmail(sender_address, receiver_address, text)
            print('sent')


def unsubscribe(file, name):
    s = name.lower()
    with open(file, "r") as f:
        data = f.readlines()

    with open(file, "w") as f:
        for line in data:
            if line.strip("\n") != s:
                f.write(line)


# check_name('list.txt', 'amaangigani35@gmail.com')
# send_email('list.txt')
# unsubscribe('list.txt', 'giganIamaan071@gmail.com')
