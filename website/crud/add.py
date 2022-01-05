from flask import Blueprint, request, flash
from flask.helpers import url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from ..models import Comment, Like, Post
from .. import db

add = Blueprint("add", __name__)

@add.route("/discussion", methods=["POST"])
@login_required
def posts():
    posts = Post.query.all()

    if request.method == 'POST':
        post = request.form.get('post')

        if len(post) < 1:
            flash('Post post cannot be empty', category='error')
        else:
            new_post = Post(data=post, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post added!', category='success')

    return redirect(url_for("views.posts", user=current_user, posts=posts))

@add.route("/discussion/create-comment/<post_id>", methods=["POST"])
@login_required
def posts_comments(post_id):
    text = request.form.get("comment")
    if not text:
        flash("Comment cant be empty", category="error")

    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(data=text, user_id=current_user.id, post_id=post_id )
            db.session.add(comment)
            db.session.commit()
            flash('Coment added!', category='success')

        else:
            flash("Post does not exist")
    
    return redirect(url_for("views.posts"))

@add.route("/like-post/<post_id>", methods=["GET"])
def like(post_id):
    post = Post.query.filter_by(id=post_id)
    like = Like.query.filter_by(user_id=current_user.id, post_id=post_id).first()

    if not post:
        flash("Post does not exist!", category="error")
    elif like:
        db.session.delete(like)
        db.session.commit()
    else: 
        like=Like(user_id=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()

    return redirect(request.referrer)
