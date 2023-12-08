from typing import List
from app.models.model import LivestockProductDB
from app.schemas.livestock_product import LivestockProduct
from app.databases.connection import sess


def create_livestock_product(new_livestock_product: LivestockProduct) -> int:
    sess.add(new_livestock_product)
    sess.commit()
    new_livestock_product_id = new_livestock_product.id
    sess.close()
    return new_livestock_product_id


def get_livestock_products() -> List[dict]:
    livestock_products = sess.query(LivestockProductDB).order_by(LivestockProductDB.id).all()
    livestock_products_dict = []
    for i in livestock_products:
        livestock_products_dict.append(i.to_dict())
    return livestock_products_dict


def get_livestock_product_by_id(_id: int) -> dict:
    livestock_product = sess.query(LivestockProductDB).filter(LivestockProductDB.id == _id).first()
    if livestock_product:
        return livestock_product.to_dict()
    return None


def update_livestock_product(_id: int, updated_livestock_product: dict) -> dict:
    livestock_product = sess.query(LivestockProductDB).filter(LivestockProductDB.id == _id).first()

    if "type" in updated_livestock_product:
        livestock_product.type = updated_livestock_product["type"]
    if "name" in updated_livestock_product:
        livestock_product.name = updated_livestock_product["name"]
    if "address" in updated_livestock_product:
        livestock_product.address = updated_livestock_product["address"]

    sess.commit()
    livestock_product_dict = livestock_product.to_dict()
    sess.close()
    return livestock_product_dict


def delete_livestock_product(_id: int) -> int:
    livestock_product = sess.query(LivestockProductDB).filter(LivestockProductDB.id == _id).first()
    sess.delete(livestock_product)
    sess.commit()
    sess.close()
    return _id
