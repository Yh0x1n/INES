from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel

from database import ines_db

import random

router = APIRouter()

@router.get('/forms/{id}')
def get_form(id: int):

    form = ines_db.forms.get(id)

    return {'form': form}


def random_id():
    numbers = '1234567890'
    len = 4
    return int(''.join(random.sample(numbers, len)))

class InsertForm(BaseModel):
    id: Optional[int]
    name: str
    items: str
    id_creator: str

@router.post('/forms')
def post_form(form: InsertForm):

    if not form.id: 
        form.id = random_id()

    if not ines_db.forms.insert(form):
        return {'success': False}

    return {
        'success': True,
        'form': form
    }

@router.delete('/forms/{id}')
def delete_form(id: int):

    if not ines_db.forms.delete(id):
        return {'success': False}   

    return {'success': True}