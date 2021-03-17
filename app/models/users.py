from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return User.get(id)

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(86))
    email = db.Column(db.String(84), unique=True)

    @property 
    def is_authenticated(self):
        return True

    @property 
    def is_active(self):
        return True

    @property 
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    
    
    def __init__ (self, username, password, name, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.name = name
        self.email = email
    def __repr__(self):
        return "<User {}".format (self.username)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
