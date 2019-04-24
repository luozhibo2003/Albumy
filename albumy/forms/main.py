from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import Optional, Length, DataRequired


class DescriptionForm(FlaskForm):
    description = TextAreaField('图片描述', validators=[Optional(), Length(0, 500)])
    submit = SubmitField('提交')


class TagForm(FlaskForm):
    tag = StringField('Add Tag (use space to separate)', validators=[Optional(), Length(0, 64)])
    submit = SubmitField('提交')


class CommentForm(FlaskForm):
    body = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('发表评论')
