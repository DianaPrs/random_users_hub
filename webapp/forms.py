import urllib.request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import URL, DataRequired, Email, ValidationError


class UserForm(FlaskForm):
    """Create user instance"""

    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    gender = StringField("Gender", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    country = StringField("Country", validators=[DataRequired()])
    street = StringField("Street", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    picture = URLField("Photo", validators=[DataRequired(), URL()])
    submit = SubmitField("Save")

    def validate_picture(self, field):
        """Validates URL availability
         and picture format.

        :param field: URL field
        """
        if field.data[-4:].lower() != ".jpg":
            raise ValidationError("Image url should end on .jpg")
        try:
            urllib.request.urlopen(field.data)
        except Exception:
            raise ValidationError("URL not available")
