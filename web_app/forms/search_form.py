from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Search(FlaskForm):
    text_name = StringField('', validators=[DataRequired()])
    submit = SubmitField('Search')