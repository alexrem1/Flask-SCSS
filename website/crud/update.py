from flask import Blueprint, request, flash
from flask.templating import render_template
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from ..models import User
from .. import db

update = Blueprint("update", __name__)

@update.route("/account/my-details/<first_name>", methods=["POST", "GET"])
@login_required
def updateDetails(first_name):
    user = User.query.filter_by(first_name=first_name).first()

    if request.method == "POST":
        user.email = request.form.get("email")
        user.address = request.form.get("address")
        user.post_code = request.form.get("post_code")        
        
        if (user):
            db.session.commit()
            flash('Details updated!', category='success')
            return redirect(request.referrer)

        else:
            flash('Error!', category='error')
            return redirect(request.referrer)

    return render_template("my-details.html", user=current_user)
    
