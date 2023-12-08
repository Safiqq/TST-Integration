from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, status

import app.databases.livestock_product as db
from app.schemas.livestock_product import LivestockProduct
from app.auth.jwt import get_user

livestock_product_router = APIRouter(tags=["Livestock Products"])


@livestock_product_router.post("/", response_model=dict)
async def create_livestock_product(
    livestock_product: LivestockProduct = Body(...), _: str = Depends(get_user)
) -> dict:
    try:
        _id = db.create_livestock_product(livestock_product.to_db())
        return {"message": f"LivestockProduct created successfully with ID {_id}"}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create the livestock_product",
        ) from exc


@livestock_product_router.get("/", response_model=List[dict])
async def retrieve_all_livestock_products(_: str = Depends(get_user)) -> List[dict]:
    return db.get_livestock_products()


@livestock_product_router.get("/{_id}", response_model=dict)
async def retrieve_livestock_product(_id: int, _: str = Depends(get_user)) -> dict:
    livestock_product = db.get_livestock_product_by_id(_id)
    if livestock_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="LivestockProduct with supplied ID does not exist",
        )
    return livestock_product


@livestock_product_router.patch("/{_id}", response_model=dict)
async def update_livestock_product(
    _id: int, updated_livestock_product: dict = Body(...), _: str = Depends(get_user)
) -> dict:
    try:
        db.update_livestock_product(_id, updated_livestock_product)
        return {"message": "LivestockProduct updated successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="LivestockProduct with supplied ID does not exist",
        ) from exc


@livestock_product_router.delete("/{_id}", response_model=dict)
async def delete_livestock_product(_id: int, _: str = Depends(get_user)) -> dict:
    try:
        db.delete_livestock_product(_id)
        return {"message": "LivestockProduct deleted successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="LivestockProduct with supplied ID does not exist",
        ) from exc
