
from main_site import login_manager
from flask_login import UserMixin

import json
with open('/etc/mainsite_user.json') as config_file:
    pw = json.load(config_file)

class User(UserMixin):
    id = 1
    username = pw.get('SECRET_USER')
    password = pw.get('SECRET_PASS')

    def __repr__(self):
        return f"User('{self.username}', '{self.image_file}')"

@login_manager.user_loader
def load_user(user_id):
    return User()