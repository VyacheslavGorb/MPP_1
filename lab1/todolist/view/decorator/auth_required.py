from functools import wraps

from flask import session, redirect, url_for, request

from todolist.model.service.jwt_service import validate_jwt


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not validate_jwt(request.cookies.get("token")):
            session.clear()
            return redirect(url_for("auth.login"))
        return func(*args, **kwargs)

    return wrapper
