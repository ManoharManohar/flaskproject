import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)  #587
    server.login('dumpetimurali93@gmail.com','gyla exxd uayq asdz')
    msg=EmailMessage()
    msg['FROM']='dumpetimurali93@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()