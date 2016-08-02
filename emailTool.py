
import smtplib
import email.mime.multipart  
import email.mime.text
import time
import datetime


class emailTool:

    def __init__(self,cfg):
        self.config = cfg

    def send(self):
        smtp=smtplib.SMTP()  
        smtp.connect(self.config['Host'],'25')  
        smtp.login(self.config['From'],self.config['PW'])
        msg=email.mime.multipart.MIMEMultipart()  
        msg['from'] = self.config['From']
        msg['to'] = self.config['To']
        msg['subject'] = self.config['subject']
        content = self.config['content']
        txt=email.mime.text.MIMEText(content)  
        msg.attach(txt)  
        smtp.sendmail(self.config['From'],self.config['To'],str(msg))  
        smtp.quit()
        print("send mail at "+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))) 

    def sendDelay(self,dtime):
        time.sleep(dtime)
        self.send() 
