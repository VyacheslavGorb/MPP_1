from functools import wraps

from flask import session, render_template


def guest_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Entered")
        if session["logged_in"]:  # TODO
            print(session["logged_in"])
            return render_template("info.html")
        return func(*args, **kwargs)

    return wrapper
