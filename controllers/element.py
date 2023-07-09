from sqlalchemy.exc import IntegrityError

from constants.error_messages import DUPLICATED_ELEMENT, GENERAL_ERROR
from constants.http_statuses import OK, SEMANTIC_ERROR, SYNTAX_ERROR
from database import Session
from formatters.element import format_element_response
from models.element import Element
from schemas.requests.element import NewElementRequestSchema


def add_element(form: NewElementRequestSchema):
    new_element = Element(form.title, form.content, form.element_type_id, form.parent_id)
    
    try:
        session = Session()
        
        session.add(new_element)
        
        session.commit()
        
        return format_element_response(new_element), OK

    except IntegrityError as e:
        return {"mesage": DUPLICATED_ELEMENT}, SEMANTIC_ERROR

    except Exception as e:
        error_msg = "Could not process this request"
        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR