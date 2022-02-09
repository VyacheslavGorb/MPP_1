from asyncio.log import logger
from functools import wraps
from flask import request
import jwt
from jwt import DecodeError, ExpiredSignatureError

secret = "secret passphrase"  # TODO get from config and logging
algorihm = "HS256"


def generate_jwt(payload: dict[str, str]) -> str:
    encoded_jwt = jwt.encode(payload, secret, algorithm=algorihm)
    return encoded_jwt


def validate_jwt(token: str) -> bool:
    if token is None:
        return False

    is_valid = True
    try:
        jwt.decode(token, secret, algorithms=algorihm)
    except (DecodeError, ExpiredSignatureError) as e:
        is_valid = False

    return is_valid


def auth_required(f):  # TODO
    @wraps(f)
    def wrapper(*args, **kwargs):
        logger.error("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return f(*args, **kwargs)

    return wrapper
