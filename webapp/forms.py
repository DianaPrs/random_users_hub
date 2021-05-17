from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import URLField, EmailField
from wtforms.validators import DataRequired, Email, URL, ValidationError
import urllib.request


class UserForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    gender = StringField("Gender", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    country = StringField("Country", validators=[DataRequired()])
    street = StringField("Street", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    picture = URLField("Photo", validators=[URL()],)
    submit = SubmitField("Save")

    @staticmethod
    def validate_picture(form, field):
        try:
            urllib.request.urlopen(field.data)
        except Exception as ex:
            raise ValidationError(ex)

