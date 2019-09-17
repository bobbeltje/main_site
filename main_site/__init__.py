
from flask import Flask
from main_site.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from main_site import routes
