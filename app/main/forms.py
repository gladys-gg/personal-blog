from flask_wtf import FlaskForm
from wtforms import Form,StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class BlogForm(FlaskForm):
    title = StringField('The Title:', validators = [DataRequired()])
    content = TextAreaField('Your Content', validators = [DataRequired()])
    submit = SubmitField('Post')
    
class UpdateBlogForm(FlaskForm):
    title = StringField('The Title:', validators = [DataRequired()])
    content = TextAreaField('Your Content', validators = [DataRequired()])
    submit = SubmitField('Update Post')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Say something!', validators = [DataRequired()])
    submit = SubmitField('comment')
    

class UpdateProfile(FlaskForm):
    first_name = StringField('Input your First Name:')
    last_name = StringField('Input your Last Name:')
    bio = TextAreaField('Update your bio:')
    email = StringField('Email:')
    submit = SubmitField('Input your First Name:')
    