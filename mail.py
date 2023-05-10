import smtplib
from email.mime.text import MIMEText

def mail(content):
    
    mail_host = 'smtphz.qiye.163.com' 
    mail_user = 'xxxxxx@163.com'  
    mail_pass = '授权码'   
    sender = 'xxxxxx@163.cn'  
    receivers = ['xxxxxx@163.com']  

    message = MIMEText(content,'plain','utf-8')
    message['Subject'] = '校园网重连信息' 
    message['From'] = sender 
    message['To'] = receivers[0]  

    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user,mail_pass) 
        smtpObj.sendmail(
            sender,receivers,message.as_string()) 
        smtpObj.quit() 
        print('success')
    except smtplib.SMTPException as e:
        print('error',e)
