from constants.error_messages import DUPLICATED_ELEMENT, FOLDER_NOT_FOUND, GENERAL_ERROR, REQUIRED_CONTENT
from constants.http_statuses import OK, CREATED, SEMANTIC_ERROR, SYNTAX_ERROR
from database import Session
from datetime import datetime
from flask import request
from formatters.element import format_element_response, format_element_list_response
from models.element import Element
from schemas.requests.element import GetElementRequestSchema, ListElementRequestSchema, NewElementRequestSchema, RemoveElementRequestSchema


def add(body: NewElementRequestSchema):
    new_element = Element(body.title, body.content, body.element_type_id, body.parent_id)
    
    try:
        session = Session()

        if new_element.element_type_id == 2 and new_element.content is None:
            raise ValueError(REQUIRED_CONTENT)

        if new_element.parent_id is not None:
            parent = session.query(Element).filter(Element.id == new_element.parent_id).one_or_none()

            if parent is None:
                raise ValueError(FOLDER_NOT_FOUND)
        
        matching_element = session.query(Element).filter(
            Element.parent_id == new_element.parent_id,
            Element.title == new_element.title
        ).one_or_none()

        if matching_element is not None:
            raise AttributeError(DUPLICATED_ELEMENT)

        session.add(new_element)
        session.commit()
        session.close()
        
        return format_element_response(new_element), CREATED

    except (AttributeError, ValueError) as e:
        return {"mesage": str(e)}, SEMANTIC_ERROR

    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR
    

def get_by_folder(path: ListElementRequestSchema):
    parent_id = path.parent_id
    
    try:
        session = Session()

        if parent_id is not None:
            parent = session.query(Element).filter(Element.id == parent_id).one_or_none()

            if parent is None:
                raise ValueError(FOLDER_NOT_FOUND)

        elements = session.query(Element).filter(
            Element.parent_id == parent_id,
            Element.deleted_at == None
        ).all()

        session.close()
        
        return format_element_list_response(elements), OK

    except ValueError as e:
        return {"mesage": str(e)}, SEMANTIC_ERROR

    except Exception as e:        
        return {"mesage": str(e)}, SYNTAX_ERROR
    

def get(path: GetElementRequestSchema):
    id = path.id
    
    try:
        session = Session()
        elements = session.query(Element).filter(
            Element.id == id,
            Element.deleted_at == None
        ).one()

        session.close()
        
        return format_element_response(elements), OK

    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR
    

def remove(path: RemoveElementRequestSchema):
    id = path.id

    try:
        session = Session()
        session.query(Element).filter(Element.id == id).update({'deleted_at': datetime.now()})
        session.commit()
        session.close()
        
        return '', OK

    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR
