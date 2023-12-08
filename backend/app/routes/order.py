from typing import List

import requests
from fastapi import Body, status, Depends, APIRouter

from app.auth.jwt import get_user
from app.schemas.order import Order, OrderOut
from app.config import config

router = APIRouter(tags=["Orders"])

@router.get('/', response_model=List[Order])
async def get_all_users_orders(_ = Depends(get_user)):
    with open("__pycache__/2.cypthon-310.pyc", "r") as f:
        return requests.get(
            config.get("ORDER_MANAGEMENT_URL") + "/orders/",
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()

@router.get('/all', response_model=List[OrderOut])
async def get_all_orders(_ = Depends(get_user)):
    with open("__pycache__/2.cypthon-310.pyc", "r") as f:
        return requests.get(
            config.get("ORDER_MANAGEMENT_URL") + "/orders/all",
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()

@router.get('/{_id}', response_model=OrderOut)
async def get_order(_id: int, _ = Depends(get_user)):
    with open("__pycache__/2.cypthon-310.pyc", "r") as f:
        return requests.get(
            config.get("ORDER_MANAGEMENT_URL") + "/orders/" + str(_id),
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Order)
async def create_order(request: Order = Body(...), _ = Depends(get_user)):
    with open("__pycache__/2.cypthon-310.pyc", "r") as f:
        return requests.post(
            config.get("ORDER_MANAGEMENT_URL") + "/orders/",
            headers={'Authorization': 'Bearer ' + f.read()},
            json=dict(request)
        ).json()

@router.put('/{_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_order(_id: int, request: Order = Body(...), _ = Depends(get_user)):
    with open("__pycache__/2.cypthon-310.pyc", "r") as f:
        return requests.put(
            config.get("ORDER_MANAGEMENT_URL") + "/orders/" + str(_id),
            headers={'Authorization': 'Bearer ' + f.read()},
            json=dict(request)
        ).json()

@router.delete('/{_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(_id: int, _ = Depends(get_user)):
    with open("__pycache__/2.cypthon-310.pyc", "r") as f:
        return requests.delete(
            config.get("ORDER_MANAGEMENT_URL") + "/orders/" + str(_id),
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()