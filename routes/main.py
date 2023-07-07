from flask import Blueprint, redirect

from controllers.home import index

main_blueprint = Blueprint('main', __name__)

main_blueprint.route('/')(index)
