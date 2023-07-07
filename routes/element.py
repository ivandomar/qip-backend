from flask import Blueprint
from flask_openapi3 import Tag

from controllers.element import index

element_blueprint = Blueprint("element", __name__, url_prefix="/element")

element_tag = Tag(name="Element", description="CRUD of qip elements (notes and folders)")

element_blueprint.route('/')(index)
