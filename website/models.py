from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# one user can post many comments.
# each picture can have many comments -> be able to load all the comments.
# each comment should have the food id also. 


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    food_id = db.Column(db.String(10000))
    user_name = db.Column(db.String(150))
    # must pass a valid, existing user_id. One to Many relationship
    # one user can have many notes

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150), unique=True)
    comments = db.relationship('Comment')
    # will be able to access all the comments under a user.