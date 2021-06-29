import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587) # (server address, port number)

server.ehlo()

server.starttls()
# Log into account

with open('login_credentials.txt', 'r') as f:
    credentials = f.read()
    email = credentials.split(',')[0].replace("'","")
    password = credentials.split(',')[1].replace("'","")
    f.close()

server.login(email, password)
msg = MIMEMultipart()
msg['From'] = 'Thomas'
msg['To'] = 'krishans290@gmail.com'
msg['Subject'] = 'Test'

with open('message.txt', 'r') as f:
    message = f.read()
    f.close()

# Attach a text message
msg.attach(MIMEText(message, 'plain'))

# Attach an image
filename = 'andy.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail(email, 'krishans290@gmail.com', text)
server.quit()