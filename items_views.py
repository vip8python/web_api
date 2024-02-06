from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(
    prefix='/items',
    tags=['Items']
)


@router.get('/')
def list_items():
    return [
        'items1',
        'items2',
    ]


@router.get('/latest')
def get_latest_item():
    return {'item': {'id': 'o', "name": 'latest'}}


@router.get('/{item_id}')
def get_item_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        'item': {
            'id': item_id,
        }
    }
