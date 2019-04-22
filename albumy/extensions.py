# -*- coding: utf-8 -*-
"""
    :author: Zhibo Luo
    :url: http://www.ddup.date

"""

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, AnonymousUserMixin
from flask_mail import Mail
from flask_moment import Moment
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
moment = Moment()
csrf = CSRFProtect()

# login_manager.login_view = 'auth.login'
# # login_manager.login_message = 'Your custom message'
# login_manager.login_message_category = 'warning'
#
# login_manager.refresh_view = 'auth.re_authenticate'
# # login_manager.needs_refresh_message = 'Your custom message'
# login_manager.needs_refresh_message_category = 'warning'