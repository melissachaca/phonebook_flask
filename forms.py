from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number= StringField('Phone Number', validators=[DataRequired()])
    address= StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Add Contact')