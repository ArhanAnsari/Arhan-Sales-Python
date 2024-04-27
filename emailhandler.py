import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer():
	def __init__(self, username, password):
		"""Init Mailer"""

		# username and password should be stored
		# in replit secrets. See readme.md for more
		
		self.USERNAME = username
		self.PASSWORD = password


	def login(self):
		"""Login to SMTP server"""
		# init connection
		self.smtp = smtplib.SMTP('smtp.gmail.com', 587)

		# start ttls for secure connection
		self.smtp.starttls()

		# login
		self.smtp.login(self.USERNAME, self.PASSWORD)


	def quit(self):
		"""Close SMTP server"""
		self.smtp.quit()
	

	def send(self, target, content, subject=""):
		"""Send an email"""

		# init message
		msg = MIMEMultipart()

		# set message vals
		msg['Subject'] = subject
		msg['From'] = self.USERNAME
		msg['To'] = target

		# add message content in HTML format
		msg.attach(MIMEText(content, "html"))

		# send email
		self.smtp.sendmail(self.USERNAME, target, msg.as_string())
