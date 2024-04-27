from flask import Flask
from flask import redirect
from flask import request
from emailhandler import Mailer
import os

app = Flask(__name__)


@app.route("/process", methods=["POST"])
def process():
	info = request.form

	mymailer = Mailer(os.environ["mailUsername"], os.environ["mailPassword"])

	mymailer.login()

	email = os.environ["mailUsername"]

	mymailer.send(target=email,
	              content=f"""Someone named {info} has filled leadform. 
 	        Thanks Arhan (Developer)""",
	              subject="Lead form Submission")

	print("Email Sent!")

	mymailer.quit()

	return redirect("https://lead-form.arhanansari2009.repl.co/successful")


@app.route("/successful")
def successful():
	page = ""
	f = open('successful.html', 'r')
	page = f.read()
	f.close()
	return page


#No need of it
#@app.route("/viewdata")
#def viewdata():
#f = open("savedFile.txt", "r")
#data = f.read()
#f.close()
#return data


@app.route('/')
def index():
	page = ""
	f = open('leadform.html', 'r')
	page = f.read()
	f.close()
	return page


app.run(host='0.0.0.0', port=8080)