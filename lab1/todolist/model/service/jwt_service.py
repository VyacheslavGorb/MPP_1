import jwt
from jwt import DecodeError, ExpiredSignatureError

secret = "secret passphrase"  # TODO get from config and logging
algorithm = "HS256"


def generate_jwt(payload: dict[str, str]) -> str:
    encoded_jwt = jwt.encode(payload, secret, algorithm=algorithm)
    return encoded_jwt


def validate_jwt(token: str) -> bool:
    if token is None:
        return False

    is_valid = True
    try:
        jwt.decode(token, secret, algorithms=algorithm)
    except (DecodeError, ExpiredSignatureError):
        is_valid = False

    return is_valid
