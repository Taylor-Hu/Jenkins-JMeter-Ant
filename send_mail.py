# 发送邮件的命令
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class Send_Email:
    def email(self, body, attach, filename):
        sender = 'hulei_pm@163.com'  # 发送邮箱
        receivers = 'hulei_pm@163.com'  # 接收邮箱，设置收件人的邮箱（可以一次发给多个人,用逗号分隔）

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        # message = MIMEText('<p style="color: red; font-size: 30px">这是一封来自Python发送的测试邮件的内容...</p>', 'html', 'utf-8')
        # message['Subject'] = Header('一封Python发送的邮件', 'utf-8')

        msg = MIMEMultipart()
        msg['Subject'] = 'WoniuSales持续集成报告'
        msg['From'] = sender
        msg['To'] = receivers

        # content = MIMEText(body, 'html', 'utf-8')
        # 将邮件正文设置成HTML样式，这样就可以用css样式丰富邮件正文了
        content = MIMEText(open('./Jenkins_email.html', 'rb').read(), 'html', 'utf-8')
        msg.attach(content)
        # attach: report.zip  放在你本地要发送附件的名字
        attachment = MIMEApplication(open(attach, 'rb').read())
        print("---1---")
        # filename：test_report.zip  接收到的附件名字，其实就是你本地要发送的附件
        # attachment.add_header('Content-Disposition', 'attachment', filename='test_report.zip')
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        print('---2----')
        msg.attach(attachment)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect('smtp.163.com', '25')
            # QJAPIKLONSOWELSB
            smtpObj.login(user='hulei_pm@163.com', password='QJAPIKLONSOWELSB')
            smtpObj.sendmail(sender, receivers, str(msg))
            smtpObj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


