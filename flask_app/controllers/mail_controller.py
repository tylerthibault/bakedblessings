from flask_mail import Message
from flask_app import app, mail
from flask import render_template, redirect, session, request
from flask_app.config.helpers import page_back


@app.route("/mail/test")
def test_mail():

    msg = Message('Hello from the other side!', sender ='blessingsbaked@gmail.com', recipients = ['tyler.thibault@protonmail.com'])
    msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
    
    mail.connect().send(msg)

    return "sent?"