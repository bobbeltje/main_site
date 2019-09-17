
from main_site import login_manager
from flask_login import UserMixin

class User(UserMixin):
    id = 1
    username = 'bobbel'
    password = 'testing'

    def __repr__(self):
        return f"User('{self.username}', '{self.image_file}')"

@login_manager.user_loader
def load_user(user_id):
    return User()