from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user
from flask_login.utils import login_required
from sqlalchemy.sql.expression import asc, desc

from website.crud.add import posts_comments
from .models import Comment, Post, User
from . import db


views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html", user=current_user)

@views.route("/discussion")
@login_required
def posts():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template("posts.html", user=current_user, posts=posts)

@views.route("/account/my-posts/<first_name>")
@login_required
def my_posts(first_name):
    user = User.query.filter_by(first_name=first_name).first()

    if not user:
        flash("No user with that username exists", category="error")
        return redirect(url_for("views.home"))

    posts = Post.query.filter_by(user_id=user.id).order_by(Post.date.desc()).all()
    print(posts)
    # posts = user.posts
    return render_template("my-posts.html", user=current_user, posts=posts, first_name=first_name)
