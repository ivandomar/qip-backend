from sqlalchemy.exc import IntegrityError

from constants.error_messages import DUPLICATED_ELEMENT, GENERAL_ERROR
from constants.http_statuses import OK, CREATED, SEMANTIC_ERROR, SYNTAX_ERROR
from database import Session
from formatters.element import format_element_response, format_element_list_response
from models.element import Element
from schemas.requests.element import NewElementRequestSchema, ListElementRequestSchema


def add_element(form: NewElementRequestSchema):
    new_element = Element(form.title, form.content, form.element_type_id, form.parent_id)
    
    try:
        # TODO: check if element title already exists in its folder, throw an error if positive
        session = Session()
        session.add(new_element)
        session.commit()
        
        return format_element_response(new_element), CREATED

    except IntegrityError as e:
        return {"mesage": DUPLICATED_ELEMENT}, SEMANTIC_ERROR

    except Exception as e:
        error_msg = "Could not process this request"
        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR
    

def get_by_folder(form: ListElementRequestSchema):
    parent_id = form.parent_id
    
    try:
        session = Session()
        elements = session.query(Element).filter(Element.parent_id == parent_id).first()
        
        return format_element_list_response(elements), OK

    except Exception as e:
        error_msg = "Could not process this request"
        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR