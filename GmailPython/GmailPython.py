import os
import smtplib
import mimetypes
from threading import Thread
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64

class MyThread(Thread):

    def __init__(self,fun,gmailUser,recipient,msg):

        Thread.__init__(self)
        self.gmailUser=gmailUser
        self.recipient=recipient
        self.msg=msg
        self.fun=fun
    
    def run(self):
        self.fun(self.gmailUser,self.recipient, self.msg)

        


def sendMail(subject, text, *attachmentFilePaths):
  gmailUser = 'gomord@gmail.com'
  gmailPassword = ''
  recipient = 'gomord@gmail.com'

  msg = MIMEMultipart()
  msg['From'] = 'asd@asdf'
  msg['To'] = recipient
  msg['Subject'] = subject
  msg.attach(MIMEText(text))

  for attachmentFilePath in attachmentFilePaths:
      msg.attach(getAttachment(attachmentFilePath))

  mailServer = smtplib.SMTP('smtp.gmail.com', 587)
  mailServer.ehlo()
  mailServer.starttls()
  mailServer.ehlo()
  mailServer.login(gmailUser, gmailPassword)
  dicThred={}
  numTh=10
  for i in range(numTh):
      print i
      dicThred['i']=MyThread(mailServer.sendmail,msg['from'], msg['To'], msg.as_string() + ' num %d'%i)
      dicThred['i'].start()
      #dicThred['i'].join()
      #thread.start_new_thread(mailServer.sendmail,(msg['from'], msg['To'], msg.as_string()))
##  mailServer.sendmail(msg['from'], msg['To'], msg.as_string())
  for i in range(numTh):
      
      dicThred['i'].join()
  mailServer.close()

  print('Sent email to %s' % recipient)

def getAttachment(attachmentFilePath):
  if not os.path.isfile(attachmentFilePath):
      return ''
  contentType, encoding = mimetypes.guess_type(attachmentFilePath)

  #if contentType is None or encoding is not None:
  contentType = 'application/octet-stream'

  mainType, subType = contentType.split('/', 1)
##  file = open(attachmentFilePath, 'rb')

##  if mainType == 'text':
##    attachment = MIMEText(file.read())
##  elif mainType == 'message':
##    attachment = email.message_from_file(file)
##  elif mainType == 'image':
##    attachment = MIMEImage(file.read(),_subType=subType)
##  elif mainType == 'audio':
##    attachment = MIMEAudio(file.read(),_subType=subType)
##  else:
##
  attachment = MIMEBase(mainType, subType)
  attachment.set_payload(open(attachmentFilePath, 'rb').read())
  encode_base64(attachment)
  attachment.add_header('Content-Disposition', 'attachment', filename=os.path.split(attachmentFilePath)[1])
  return attachment
##  file.close()

