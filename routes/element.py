from flask_openapi3 import APIBlueprint, Tag

from constants.http_statuses import OK, SEMANTIC_ERROR, SYNTAX_ERROR
from controllers.element import add_element
from schemas.responses.element import ElementResponseSchema
from schemas.responses.general import ErrorResponseSchema

element_blueprint = APIBlueprint("element", __name__, url_prefix="/elements")

element_tag = Tag(name="Elements", description="CRUD of qip elements (notes and folders)")

element_blueprint.post(
    "/",
    tags=[element_tag],
    summary="Creates new element",
    responses={
        str(OK): ElementResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
    )(add_element)

