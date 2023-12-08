from typing import List
from app.models.model import LivestockDB
from app.schemas.livestock import Livestock
from app.databases.connection import sess


def create_livestock(new_livestock: Livestock) -> int:
    sess.add(new_livestock)
    sess.commit()
    new_livestock_id = new_livestock.id
    sess.close()
    return new_livestock_id


def get_livestocks() -> List[dict]:
    livestocks = sess.query(LivestockDB).order_by(LivestockDB.id).all()
    livestocks_dict = []
    for i in livestocks:
        livestocks_dict.append(i.to_dict())
    return livestocks_dict


def get_livestock_by_id(_id: int) -> dict:
    livestock = sess.query(LivestockDB).filter(LivestockDB.id == _id).first()
    if livestock:
        return livestock.to_dict()
    return None


def update_livestock(_id: int, updated_livestock: dict) -> dict:
    livestock = sess.query(LivestockDB).filter(LivestockDB.id == _id).first()

    if "name" in updated_livestock:
        livestock.name = updated_livestock["name"]
    if "breed" in updated_livestock:
        livestock.breed = updated_livestock["breed"]
    if "species" in updated_livestock:
        livestock.species = updated_livestock["species"]
    if "birthplace_id" in updated_livestock:
        livestock.birthplace_id = updated_livestock["birthplace_id"]
    if "birthdate" in updated_livestock:
        livestock.birthdate = updated_livestock["birthdate"]
    if "gender" in updated_livestock:
        livestock.gender = updated_livestock["gender"]
    if "location_id" in updated_livestock:
        livestock.location_id = updated_livestock["location_id"]

    sess.commit()
    livestock_dict = livestock.to_dict()
    sess.close()
    return livestock_dict


def delete_livestock(_id: int) -> int:
    livestock = sess.query(LivestockDB).filter(LivestockDB.id == _id).first()
    sess.delete(livestock)
    sess.commit()
    sess.close()
    return _id
