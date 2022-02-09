from flask import Flask, render_template
from todolist import auth
from todolist.jwt_auth import auth_required
from todolist.model.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:slav2712@localhost/todo_list_db'

db.init_app(app)
app.app_context().push()
db.create_all()


app.register_blueprint(auth.bp)



@app.route("/")
@app.route("/index")
@auth_required
def hello_world1():
    return render_template("auth/login.jinja", name="name2")