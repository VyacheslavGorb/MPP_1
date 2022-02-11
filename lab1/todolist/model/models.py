from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.BINARY(60), nullable=False)


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    status = db.Column(db.Enum('ACTIVE', 'IN_PROGRESS', 'DONE'))
    expected_completeon_date = db.Column(db.Date)


class TaskFile(db.Model):
    __tablename__ = 'task_files'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey(Task.id))
    file_path = db.Column(db.String(256), unique=True, nullable=False)
