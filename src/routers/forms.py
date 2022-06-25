from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel
import random
from database import ines_db
import util

router = APIRouter()

@router.get('/forms/{id}')
def get_form(id: int):

    form = ines_db.forms.get(id)

    return {'form': form}

class InsertForm(BaseModel):
    id: Optional[int]
    name: str
    items: str
    id_creator: str

@router.post('/forms')
def post_form(form: InsertForm):

    form.id = util.random_id()

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