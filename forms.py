from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class AddArticle(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    intro = StringField('Intro: ', validators=[DataRequired()])
    text = TextAreaField('Text: ', validators=[DataRequired()])
    submit = SubmitField('Add')