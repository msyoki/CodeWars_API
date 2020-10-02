
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PostForm(FlaskForm):

    title = StringField('Code Language',validators=[Required()])
    text = TextAreaField('Code',validators=[Required()])
    category = SelectField('Challenge',choices=[('leaderboard_climbers','Leaderboard climbers challenge'),('highest_and_lowest','Highest and lowest challenge'),('two_oldest_ages','Two oldest ages challenge')],validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')