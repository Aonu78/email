import smtplib
from email.message import EmailMessage

def emailsender(email,subject,text):
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = "info@ssebowa.com"
    msg['To'] = email
    s =server = smtplib.SMTP_SSL('mail.privateemail.com', 465)
    s.login("info@ssebowa.com","1D2i3s4a5n!-iNf0")
    s.send_message(msg)
    s.quit()