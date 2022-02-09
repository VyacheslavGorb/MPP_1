from flask import Blueprint, render_template

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login")
def hello_world():
    return render_template("auth/login.jinja", name="login")