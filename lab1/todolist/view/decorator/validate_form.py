from functools import wraps

from flask import request
from wtforms import Form


def validate_form(validator_class: Form.__class__):
    def nested_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            form = validator_class(request.form)
            return func(form.validate(), *args, **kwargs)

        return wrapper

    return nested_dec
