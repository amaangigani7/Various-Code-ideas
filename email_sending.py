import smtplib, email, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

lis = ['amaangigani35@gmail.com', 'raymondmarkseries@gmail.com']

for x in lis:
    mail_content = '''Welcome to this page'''
    sender_address = 'raymondmarkseries@gmail.com'
    sender_pass = '#Amaan@Raymond_250'
    body = "Welcome"
    receiver_address = x

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = "Welcome to this page"
    message.attach(MIMEText(body, "plain"))

    text = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_address, sender_pass)
        server.sendmail(sender_address, receiver_address, text)
print('sent')


# session = smtplib.SMTP('smtp.gmail.com', 587)
# session.starttls()
# session.login(sender_address, sender_pass)
# text = message
# session.sendmail(sender_address, receiver_address, text)
# session.quit()
# print('email sent')


# file_name = "G:\\DCN\\List_Of_practical.docx"
# with open(file_name, 'rb') as attachment:
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())
#
# encoders.encode_base64(part)
#
# part.add_header(
#     "Content-Disposition",
#     f"attachment; file_name= {file_name}",)
# message.attach(part)



