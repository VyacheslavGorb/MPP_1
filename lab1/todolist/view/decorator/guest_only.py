from functools import wraps

from flask import session, render_template, request


def guest_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.cookies.get("token"):
            return render_template("info.html"), 403
        return func(*args, **kwargs)

    return wrapper
