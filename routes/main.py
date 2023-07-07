from flask import Blueprint

from controllers.home import index

main_blueprint = Blueprint('main', __name__)

main_blueprint.route('/')(index)
