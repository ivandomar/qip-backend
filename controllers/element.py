from sqlalchemy.exc import IntegrityError

from database import Session
from models.element import Element
from schemas.requests.element import NewElementRequestSchema


def add_element(form: NewElementRequestSchema):
    new_element = Element(form.title, form.content, form.element_type_id, form.parent_id)
    
    try:
        session = Session()
        
        session.add(new_element)
        
        session.commit()
        
        # TODO: format object before responsing
        return new_element, 200

    except IntegrityError as e:
        error_msg = 'Element title already exists in this folder'

        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        
        return {"mesage": error_msg}, 400