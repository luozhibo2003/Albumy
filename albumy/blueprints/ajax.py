# -*- coding: utf-8 -*-
"""
    :author: Zhibo Luo
    :url: http://www.ddup.date
    :copyright: © 2018 Zhibo Luo <luozhibo2008@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os

from flask import Blueprint

ajax_bp = Blueprint('ajax', __name__)


@ajax_bp.route('/notifications_count')
def notifications_count():
    return 'notifications_count'