from flask import Flask, request, render_template, redirect
from email_validator import validate_email, EmailNotValidError
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'a827040b949b19'
app.config['MAIL_PASSWORD'] = '2664e575b9b214'
app.config['MAIL_DEFAULT_SENDER'] = 'sender'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

@app.route('/', methods = ['POST','GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        email = request.form['email']
        title = request.form['title']
        text = request.form['text']
        try:
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError:
            return redirect('/')
        if len(title)<1 or len(text)<1:
            return redirect('')
        msg = Message(title, recipients=[email])
        msg.body = text
        mail.send(msg)
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)