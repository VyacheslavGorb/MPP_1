from wtforms import Form, StringField, PasswordField, validators

LOGIN_REGEXP = r"^[A-Za-z][0-9a-zA-Z]{2,19}$"
PASSWORD_REGEXP = r"^[0-9a-zA-Z]{8,20}$"


class LoginFormValidator(Form):
    login = StringField('login', [validators.Regexp(LOGIN_REGEXP), validators.InputRequired()])
    password = PasswordField('password', [validators.Regexp(PASSWORD_REGEXP), validators.InputRequired()])


class SingUpFormValidator(Form):
    login = StringField(validators=[validators.Regexp(LOGIN_REGEXP), validators.InputRequired()])
    password = PasswordField(validators=[
        validators.InputRequired(),
        validators.EqualTo('confirm')
    ])
    confirm = PasswordField(validators=[validators.Regexp(PASSWORD_REGEXP), validators.InputRequired()])
