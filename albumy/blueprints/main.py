# -*- coding: utf-8 -*-
"""
    :author: Zhibo Luo
    :url: http://www.ddup.date
    :copyright: © 2018 Zhibo Luo <luozhibo2008@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os

from flask import Blueprint, render_template, request, current_app, send_from_directory
from flask_login import current_user

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        page = request.args.get('page', 1, type=int)
        per_page = current_app.config['ALBUMY_PHOTO_PER_PAGE']
        # pagination = Photo.query \
        #     .join(Follow, Follow.followed_id == Photo.author_id) \
        #     .filter(Follow.follower_id == current_user.id) \
        #     .order_by(Photo.timestamp.desc()) \
        #     .paginate(page, per_page)
        # photos = pagination.items
    else:
        pagination = None
        photos = None
    # tags = Tag.query.join(Tag.photos).group_by(Tag.id).order_by(func.count(Photo.id).desc()).limit(10)
    return render_template('main/index.html')


@main_bp.route('/explore')
def explore():
    return 'explore'


@main_bp.route('/search')
def search():
    return 'search'


@main_bp.route('/show_notifications')
def show_notifications():
    return 'show_notifications'


@main_bp.route('/upload')
def upload():
    return 'upload'


@main_bp.route('/avatar/<path:filename>')
def get_avatar(filename):
    # return send_from_directory(current_app.config['AVATARS_SAVE_PATH'], filename)
    return 'get_avatar'


@main_bp.route('/show_photo')
def show_photo():
    return 'show_photo'
