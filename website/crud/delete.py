from operator import pos
from flask import Blueprint, render_template, request, jsonify, flash, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from ..models import Post, Comment
from .. import db

delete = Blueprint("delete", __name__)

@delete.route("delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("post does not exist", category="error")

    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post Deleted", category="success")

    return redirect(request.referrer)


@delete.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first() or Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash('Error.', category='error')
    elif current_user.id != comment.user_id and current_user.id != comment.post.id:
        flash('You do not have permission to delete this comment.', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()
        flash('Comment deleted.', category='success')


    return redirect(request.referrer)
