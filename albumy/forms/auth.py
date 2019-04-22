# -*- coding: utf-8 -*-
"""
    :author: Zhibo Luo (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Zhibo Luo <luozhibo2008@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 254), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('登录')


