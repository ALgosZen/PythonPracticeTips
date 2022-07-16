from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import email.mime.application

email_user = "crisisyear08@gmail.com"
email_pass = "zfurdtldbszstpcx"
#second password to check zvldrzkkptfsuigs

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
s = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
s.login(email_user, email_pass)


msg = MIMEMultipart()
msg['Subject'] = 'Dataset files123'
msg['From'] = email_user
msg['To'] = email_user

txt = MIMEText('datasets124 CSV file attached .')
msg.attach(txt)

filename = 'testfile.txt' #path to file
fo=open(filename,'rb')
attach = email.mime.application.MIMEApplication(fo.read(),_subtype="pdf")
fo.close()
attach.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(attach)
s.send_message(msg)
s.quit()