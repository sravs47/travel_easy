from wtforms import Form,StringField,PasswordField,validators

# Register Form Class
class RegisterForm(Form):
    firstname = StringField('firstname', [validators.DataRequired(),validators.Length(min=1, max=50)])
    lastname = StringField('lastname', [validators.DataRequired(),validators.Length(min=1, max=50)])
    rusername = StringField('rusername', [validators.DataRequired(),validators.Length(min=4, max=25)])
    email = StringField('email', [validators.DataRequired(),validators.Length(min=6, max=50)])
    rpassword = PasswordField('rpassword', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')