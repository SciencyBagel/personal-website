from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField  # used for text area
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL

class PostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    img_url = URLField('Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
