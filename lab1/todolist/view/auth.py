from flask import Blueprint, render_template, request, session

from todolist.view.decorator.auth_required import auth_required
from todolist.view.validator.validators import LoginFormValidator

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route('/login', methods=["GET"])
def go_to_login_page():
    session['logged_in'] = True
    return render_template("auth/login.html")


@auth_bp.route('/login', methods=["POST"])
def login():
    form = LoginFormValidator(request.form)
    print(form.validate())
    session['logged_in'] = True
    return render_template("auth/login.html")


@auth_bp.route('/signup', methods=["GET"])
# @auth_required
def go_to_signup_page():
    session['logged_in'] = False
    return render_template("auth/signup.html")
