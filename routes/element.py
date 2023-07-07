from flask_openapi3 import APIBlueprint, Tag

from controllers.element import index

element_blueprint = APIBlueprint("element", __name__, url_prefix="/elements")

element_tag = Tag(name="Elements", description="CRUD of qip elements (notes and folders)")

element_blueprint.get("/", tags=[element_tag], summary="Shows default JSON")(index)

