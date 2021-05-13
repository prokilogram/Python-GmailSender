from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


# Create Message Object Instance
sourceMail = input(
    str("Enter Source Mail(with SMTP active option in Gmail): "))
sourcePass = input(str("Enter Source Mail Password: "))
targetMail = input(str("Enter Your Target Mail: "))
subject = input(str("Enter Your Subject: "))
message = input(str("Enter Your Message: "))


msg = MIMEMultipart()


# Setup The Parameter Of The Message
msg['From'] = sourceMail
msg['To'] = targetMail
msg['Subject'] = subject

# Add In The Message Body
msg.attach(MIMEText(message))


# Create Server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sourceMail, sourcePass)
        smtp.send_message(msg)
        print("Message Successfully Sent!!")
    except:
        print("Sending Faild...Try Again!!")
