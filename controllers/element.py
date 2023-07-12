from constants.error_messages import DUPLICATED_ELEMENT, FOLDER_NOT_FOUND, GENERAL_ERROR
from constants.http_statuses import OK, CREATED, SEMANTIC_ERROR, SYNTAX_ERROR
from database import Session
from formatters.element import format_element_response, format_element_list_response
from models.element import Element
from schemas.requests.element import GetElementRequestSchema, ListElementRequestSchema, NewElementRequestSchema, RemoveElementRequestSchema

from datetime import datetime

def add(form: NewElementRequestSchema):
    new_element = Element(form.title, form.content, form.element_type_id, form.parent_id)
    
    try:
        session = Session()

        parent = session.query(Element).filter(Element.id == form.parent_id).one_or_none()

        if parent is None:
            raise ValueError(FOLDER_NOT_FOUND)
        
        matching_element = session.query(Element).filter(
            Element.parent_id == new_element.parent_id,
            Element.title == new_element.title
        ).first()

        if matching_element is None:
            raise AttributeError(DUPLICATED_ELEMENT)

        session.add(new_element)
        session.commit()
        
        return format_element_response(new_element), CREATED

    except (AttributeError, ValueError) as e:
        return {"mesage": str(e)}, SEMANTIC_ERROR

    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR
    

def get_by_folder(form: ListElementRequestSchema):
    parent_id = form.parent_id
    
    try:
        session = Session()

        parent = session.query(Element).filter(Element.id == parent_id).one_or_none()

        if parent is None:
            raise ValueError(FOLDER_NOT_FOUND)

        elements = session.query(Element).filter(
            Element.parent_id == parent_id,
            Element.deleted_at == None
        ).all()
        
        return format_element_list_response(elements), OK

    except ValueError as e:
        return {"mesage": str(e)}, SEMANTIC_ERROR

    except Exception as e:        
        return {"mesage": str(e)}, SYNTAX_ERROR
    

def get(form: GetElementRequestSchema):
    id = form.id
    
    try:
        session = Session()
        elements = session.query(Element).filter(
            Element.id == id,
            Element.deleted_at == None
        ).one()
        
        return format_element_response(elements), OK

    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR
    

def remove(form: RemoveElementRequestSchema):
    id = form.id
    
    try:
        session = Session()
        session.query(Element).filter(Element.id == id).update({'deleted_at': datetime.now()})
        session.commit()
        
        return None, OK

    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR
