from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import os
app = Flask(__name__)

app.secret_key = "bananas"
bcrypt = Bcrypt(app)

app.config['MAIL_SERVER']=os.environ.get("MAIL_SERVER")
app.config['MAIL_PORT'] = os.environ.get("MAIL_PORT")
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False

mail = Mail(app)
mail.init_app(app)

DATABASE = "ka8anivojoliyick"
# DATABASE = "BakedBlessingsDB"