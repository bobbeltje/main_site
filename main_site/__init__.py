
from flask import Flask
from flask_login import LoginManager
from main_site.config import Config

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from main_site import routes
