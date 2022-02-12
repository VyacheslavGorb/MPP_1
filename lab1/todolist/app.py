from flask import Flask, session, request

from todolist.model.models import db
from todolist.view.auth import auth_bp
from todolist.view.decorator.auth_required import auth_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:slav2712@localhost/todo_list_db'
app.config["JWT_SECRET"] = "jwt_secret"
app.secret_key = 'BAD_SECRET_KEY'
db.init_app(app)
app.app_context().push()


@app.before_first_request
def init_session():
    session["logged_in"] = False
    session["sign_up_error"] = False


@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


@app.before_request
def clean_session():
    attributes_to_remove = {
        "auth.go_to_signup_page": ["signup_error_message"],
        "auth.login": ["login_error"]
    }
    endpoint = request.endpoint

    if request.method == "POST" or endpoint == "static":
        return

    for pair in attributes_to_remove.items():
        if pair[0] != endpoint:
            for attribute in pair[1]:
                session[attribute] = None


@app.route("/")
@app.route("/index")
@auth_required
def hello_world1():
    return "Hello"  # TODO redirect to tasks page


app.register_blueprint(auth_bp)
