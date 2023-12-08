from typing import List

import requests
from backend.app.product import Product
from fastapi import Body, status, Depends, APIRouter

from app.auth.jwt import get_user
from app.config import config

router = APIRouter(tags=["Products"])

@router.get('/', response_model=List[Product])
def get_all_products(_ = Depends(get_user)):
    with open("__pycache__/2.cypthon-310.pyc", "r") as f:
        return requests.get(
            config.get("ORDER_MANAGEMENT_URL") + "/products/",
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()

@router.get('/{_id}', response_model=Product)
def get_product(_id: int, _ = Depends(get_user)):
    with open("__pycache__/2.cypthon-310.pyc", "r") as f:
        return requests.get(
            config.get("ORDER_MANAGEMENT_URL") + "/products/" + str(_id),
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Product)
def create_product(request: Product = Body(...), _ = Depends(get_user)):
    with open("__pycache__/2.cypthon-310.pyc", "r") as f:
        return requests.post(
            config.get("ORDER_MANAGEMENT_URL") + "/products/",
            headers={'Authorization': 'Bearer ' + f.read()},
            json=dict(request)
        ).json()

@router.put('/{_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_product(_id: int, request: Product, _ = Depends(get_user), current_user: int = Depends(oauth2.get_current_user)):
    with open("__pycache__/2.cypthon-310.pyc", "r") as f:
        return requests.put(
            config.get("ORDER_MANAGEMENT_URL") + "/products/" + str(_id),
            headers={'Authorization': 'Bearer ' + f.read()},
            json=dict(request)
        ).json()

@router.delete('/{_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(_id: int, _ = Depends(get_user), current_user: int = Depends(oauth2.get_current_user)):
    with open("__pycache__/2.cypthon-310.pyc", "r") as f:
        return requests.delete(
            config.get("ORDER_MANAGEMENT_URL") + "/products/" + str(_id),
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()