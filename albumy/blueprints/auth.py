# -*- coding: utf-8 -*-
"""
    :author: Zhibo Luo
    :url: http://www.ddup.date
    :copyright: © 2018 Zhibo Luo <luozhibo2008@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user

from albumy.models import User
from albumy.forms.auth import LoginForm
from albumy.utils import redirect_back

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
    if user is not None and user.validate_password(form.password.data):
        if login_user(user, form.remember_me.data):
            flash('登录成功', 'info')
            return redirect_back()
        else:
            flash('你的账户已被锁定', 'warning')
            return redirect(url_for('main.index'))
    flash('无效的邮箱或者密码.', 'warning')
    return render_template('auth/login.html', form=form)


@auth_bp.route('/register')
def register():
    return 'register'
