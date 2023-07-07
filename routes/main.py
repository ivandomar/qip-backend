from flask import Blueprint
from flask_openapi3 import Tag

from controllers.home import index

main_blueprint = Blueprint("main", __name__)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")

main_blueprint.route('/')(index)
