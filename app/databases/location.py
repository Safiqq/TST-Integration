from typing import List
from app.models.model import LocationDB
from app.schemas.location import Location
from app.databases.connection import sess


def create_location(new_location: Location) -> int:
    sess.add(new_location)
    sess.commit()
    new_location_id = new_location.id
    sess.close()
    return new_location_id


def get_locations() -> List[dict]:
    locations = sess.query(LocationDB).order_by(LocationDB.id).all()
    locations_dict = []
    for i in locations:
        locations_dict.append(i.to_dict())
    return locations_dict


def get_location_by_id(_id: int) -> dict:
    location = sess.query(LocationDB).filter(LocationDB.id == _id).first()
    if location:
        return location.to_dict()
    return None


def update_location(_id: int, updated_location: dict) -> dict:
    location = sess.query(LocationDB).filter(LocationDB.id == _id).first()

    if "type" in updated_location:
        location.type = updated_location["type"]
    if "name" in updated_location:
        location.name = updated_location["name"]
    if "address" in updated_location:
        location.address = updated_location["address"]

    sess.commit()
    location_dict = location.to_dict()
    sess.close()
    return location_dict


def delete_location(_id: int) -> int:
    location = sess.query(LocationDB).filter(LocationDB.id == _id).first()
    sess.delete(location)
    sess.commit()
    sess.close()
    return _id
