from flask_openapi3 import APIBlueprint, Tag

from constants.http_statuses import OK, SEMANTIC_ERROR, SYNTAX_ERROR
from controllers.element import add, edit, get, get_by_folder, remove
from schemas.responses.element import ElementResponseSchema, ElementListResponseSchema
from schemas.responses.general import ErrorResponseSchema

element_blueprint = APIBlueprint("element", __name__, url_prefix="/elements")

element_tag = Tag(name="Elements", description="CRUD of qip elements (notes and folders)")

element_blueprint.get(
    '/<id>',
    tags=[element_tag],
    summary='Gets element by its unique id',
    responses={
        str(OK): ElementResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(get)

element_blueprint.get(
    '/<id>/elements',
    tags=[element_tag],
    summary='Gets elements of the specified parent element',
    responses={
        str(OK): ElementListResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(get_by_folder)

element_blueprint.delete(
    '/<id>',
    tags=[element_tag],
    summary='Removes the specified element from the database',
    responses={
        str(OK): None,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(remove)

element_blueprint.patch(
    '/<id>',
    tags=[element_tag],
    summary='Edits an element',
    responses={
        str(OK): ElementResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(edit)

element_blueprint.post(
    '/',
    tags=[element_tag],
    summary='Creates new element',
    responses={
        str(OK): ElementResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(add)
