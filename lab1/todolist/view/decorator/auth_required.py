from functools import wraps
from flask import session, redirect, url_for


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Entered")
        if session["logged_in"]: #TODO
            return redirect(url_for("auth.login"))
        return func(*args, **kwargs)

    return wrapper
