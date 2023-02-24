from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class AddArticle(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()], render_kw={'class': 'form-control'})
    intro = StringField('Intro: ', validators=[DataRequired()], render_kw={'class': 'form-control'})
    text = TextAreaField('Text: ', validators=[DataRequired()], render_kw={'class': 'form-control', 'rows': 5})
    submit = SubmitField('Add')


class UpdateArticle(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()], render_kw={'class': 'form-control'})
    intro = StringField('Intro: ', validators=[DataRequired()], render_kw={'class': 'form-control'})
    text = TextAreaField('Text: ', validators=[DataRequired()], render_kw={'class': 'form-control', 'rows': 5})
    submit = SubmitField('Update')