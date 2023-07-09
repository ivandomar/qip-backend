from typing import List

from models.element import Element

def format_element_list_response(elements: List[Element]):
    response = []

    for element in elements:
        response.append(format_element_response(element))

    return {'elements': response}

def format_element_response(element: Element):
    return {
        'id': element.id,
        'title': element.title,
        'content': element.content,
        'element_type_id': element.element_type_id,
        'created_at': element.created_at,
        'updated_at': element.updated_at,
    }