
import smtplib
import email.mime.multipart  
import email.mime.text
import time
import datetime


class emailTool:

    def __init__(self,cfg):
        self.config = cfg

    def send(self, content):
        smtp=smtplib.SMTP()  
        smtp.connect(self.config['Host'],'25')  
        smtp.login(self.config['From'],self.config['PW'])
        msg=email.mime.multipart.MIMEMultipart()  
        msg['from'] = self.config['From']
        msg['to'] = self.config['To']
        msg['subject'] = self.config['subject']
        #content = self.config['content']
        txt=email.mime.text.MIMEText(content)  
        msg.attach(txt)  
        smtp.sendmail(self.config['From'],self.config['To'],str(msg))  
        smtp.quit()
        print("send mail at "+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))) 

    def sendDelay(self, dtime, content):
        self.send(content)
        time.sleep(dtime)
    
    def sendcyc(self, pro_time, pro_num, content):
        #content_inner = cotent
        pro_time = pro_time
        pro_cnt = 0
        mail_cnt = 0
        while pro_cnt < pro_num:
            send_num = pro_cnt + 1
            sleeptime = int(pro_time/send_num)
            while send_num > 0:
                print("pro_cnt="+str(pro_cnt)+" at "+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                #time.sleep(sleeptime)
                mail_cnt += 1
                content_inner2 = ''
                if mail_cnt >=2:
                    content_inner2 = '邮件内容与前面的几封相同，在没有得到问题的答复之前，我会一直如此询问下去.'
                content_inner = "\n这是关于此问题的第"+str(mail_cnt)+"封邮件.\n"+content_inner2+"\n\n"+content
                try:
                    self.sendDelay(sleeptime,content_inner)
                    #send_num -= 1
                except:
                    print("send mail except")
                finally:
                    send_num -= 1
            pro_cnt +=1
