from functools import wraps

from flask import session, render_template


def guest_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("logged_in"):
            return render_template("info.html"), 403
        return func(*args, **kwargs)

    return wrapper
