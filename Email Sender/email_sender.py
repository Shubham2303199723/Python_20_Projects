# two factor authentication is needed before code will start work
# app password is needed in google for temporary basis
# create a function for send mail



from email.message import EmailMessage
from password import password_id # Assuming password_id is stored in password.py
import ssl 
import smtplib

email_ID = "Shubhamgurjar222@gmail.com"
password_ID = password_id

email_receiver = "yibisa7618@aersm.com"

subject = "This is Test Mail Form Python Code"

body = "this is mail from shubham gurjar"

em = EmailMessage()   # this is an instance from long name EmailMessage to short name em

em['from'] = email_ID
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_ID, password_ID)   # this will login your id in Python code for temoprary basis
    smtp.send_message(em)       # this email receiver will come here     

