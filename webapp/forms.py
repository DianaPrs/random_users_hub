from flask_wtf import FlaskForm
from wtforms import StringField, FormField, IntegerField, SubmitField
from wtforms.fields.html5 import URLField, EmailField
from wtforms.validators import DataRequired


class PhoneForm(FlaskForm):
    pass


class UserForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    gender = StringField("Gender", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    phone = IntegerField("Phone", validators=[DataRequired()])
    address = URLField("Address", validators=[DataRequired()])
    pic = StringField("Photo", validators=[DataRequired()])
    submit = SubmitField("Save")
