from flask import Flask, render_template, redirect, session

from todolist.view.auth import auth_bp
from todolist.model.models import db
from todolist.view.decorator.guest_only import guest_only

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:slav2712@localhost/todo_list_db'
app.secret_key = 'BAD_SECRET_KEY'
db.init_app(app)
app.app_context().push()
app.register_blueprint(auth_bp)


@app.before_first_request
def init_session():
    session["logged_in"] = False

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

@app.route("/")
@app.route("/index")
@guest_only
def hello_world1():
    return "Hello"
