# smtplib module send mail

import smtplib

TO = 'leonardoeichs@gmail.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'

# Gmail Sign In
sender = 'leonardoeichs@gmail.com'
passwd = 'leo210711'

server = smtplib.SMTP('smtp.gmail.com', 587) #'smtp.mail.yahoo.com'
server.ehlo()
server.starttls()
server.login(sender, passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()
