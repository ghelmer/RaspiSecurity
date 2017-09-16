import json
import smtplib
import uuid
import os
import glob

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


class TempImage:
	def __init__(self, basePath="./", ext=".jpg"):
		# construct the file path
		self.path = "{base_path}/{rand}{ext}".format(base_path=basePath,
			rand=str(uuid.uuid4()), ext=ext)

	def cleanup(self):
		# remove the file
		os.remove(self.path)


def send_email(conf):
    fromaddr = conf['email_from']
    for email_address in conf['email_address']:
        toaddrs  = email_address
        print("[INFO] Emailing to {}".format(email_address))
        text = 'Hey Someone in Your House!!!!'
        subject = 'Security Alert!!'
        message = 'Subject: {}\n\n{}'.format(subject, text)

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddrs
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        # set attachments
        files = glob.glob("/tmp/talkingraspi*")
        print("[INFO] Number of images attached to email: {}".format(len(files)))
        for f in files:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)

        # Credentials (if needed) : EDIT THIS
        email_username = None
        if 'email_username' in conf:
            username = conf['email_username']
        password = None
        if 'email_password' in conf:
            password = conf['email_password']

        # The actual mail send
        server = smtplib.SMTP(conf['email_server'])
        server.starttls()
        if email_username and email_password:
            server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()



def send_mail(conf, files=None,
              ):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))



    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
