from sqlalchemy.orm import backref
from . import db
from flask_login import UserMixin # custom class that user objects inherit from user mixins
from sqlalchemy.sql import func

# Users have many posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    comments = db.relationship('Comment', backref="post", passive_deletes=False, cascade="all")
    likes = db.relationship("Like", backref="post", passive_deletes=False, cascade="all")

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)

class Like(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    address = db.Column(db.String(150))
    post_code = db.Column(db.String(8))

    posts = db.relationship('Post', backref="user", passive_deletes=True)
    comments = db.relationship('Comment', backref="user", passive_deletes=True)
    likes = db.relationship('Like', backref="user", passive_deletes=True)
