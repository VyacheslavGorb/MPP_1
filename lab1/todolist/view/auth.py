from flask import Blueprint, render_template, url_for, session, redirect, request

from todolist.model.service.jwt_service import generate_jwt
from todolist.model.service.user_service import login_available, insert_user, is_valid_credentials
from todolist.view.decorator.auth_required import auth_required
from todolist.view.decorator.guest_only import guest_only
from todolist.view.decorator.validate_form import validate_form
from todolist.view.validator.validators import LoginFormValidator, SingUpFormValidator

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route('/login', methods=["GET"])
@guest_only
def go_to_login_page():
    return render_template("auth/login.html")


@auth_bp.route('/signup', methods=["GET"])
@guest_only
def go_to_signup_page():
    return render_template("auth/signup.html")


@auth_bp.route('/signup', methods=["POST"])
@validate_form(SingUpFormValidator)
@guest_only
def signup(is_form_valid):
    if not is_form_valid:
        session["signup_error_message"] = "Invalid form input"
        return redirect(url_for("auth.signup"))
    if not login_available(request.form["login"]):
        session["signup_error_message"] = "Login is not available"
        return redirect(url_for("auth.signup"))
    insert_user(request.form["login"], request.form["password"])
    return redirect("auth.login")


@auth_bp.route('/login', methods=["POST"])
@validate_form(LoginFormValidator)
@guest_only
def login(is_form_valid):
    if not is_form_valid or not is_valid_credentials(request.form["login"], request.form["password"]):
        redirect(url_for("auth.login"))
    token = generate_jwt({
        "login": request.form["login"]
    })
    resp = redirect("/")
    resp.set_cookie("token", value=token, httponly=True)
    return resp


@auth_bp.route('/logout', methods=["GET"])
@auth_required
def logout():
    session.clear()
    return redirect("/")
