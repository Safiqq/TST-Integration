"""
This API provides functionalities to manage location records, including creating, retrieving,
updating, and deleting records.
"""
from typing import List

import requests
from fastapi import APIRouter, Body, Depends

from app.schemas.location import Location
from app.auth.jwt import get_user
from app.config import config

location_router = APIRouter(tags=["Locations"])


@location_router.post("/", response_model=dict)
async def create_location(
    location: Location = Body(...), _: str = Depends(get_user)
) -> dict:
    """
    Creates a new location record in the database.

    Args:
        location: A Location object containing information about the new location.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message and the ID of the newly created location record.
    
    Raises:
        HTTPException 500: If an error occurs while creating the location record.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.post(
            config.get("LIVESTOCK_ID_URL") + "/locations",
            headers={'Authorization': 'Bearer ' + f.read()},
            json=dict(location),
        ).json()


@location_router.get("/", response_model=List[dict])
async def retrieve_all_locations(_: str = Depends(get_user)) -> List[dict]:
    """
    Retrieves a list of all location records from the database.

    Args:
        current_user: The currently authenticated user.

    Returns:
        A list of dictionaries, each representing a location record.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.get(
            config.get("LIVESTOCK_ID_URL") + "/locations",
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()


@location_router.get("/{_id}", response_model=dict)
async def retrieve_location(_id: int, _: str = Depends(get_user)) -> dict:
    """
    Retrieves a specific location record by its ID.

    Args:
        _id: The ID of the location record to retrieve.
        current_user: The currently authenticated user.

    Returns:
        A dictionary representing the location record.

    Raises:
        HTTPException 404: If the location record with the given ID is not found.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.post(
            config.get("LIVESTOCK_ID_URL") + "/locations/" + str(_id),
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()


@location_router.patch("/{_id}", response_model=dict)
async def update_location(
    _id: int, updated_location: dict = Body(...), _: str = Depends(get_user)
) -> dict:
    """
    Updates an existing location record in the database.

    Args:
        _id: The ID of the location record to update.
        updated_location: A dictionary containing updated information for the location.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message.

    Raises:
        HTTPException 404: If the location record with the given ID is not found.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.patch(
            config.get("LIVESTOCK_ID_URL") + "/locations/" + str(_id),
            headers={'Authorization': 'Bearer ' + f.read()},
            json=dict(updated_location),
        ).json()


@location_router.delete("/{_id}", response_model=dict)
async def delete_location(_id: int, _: str = Depends(get_user)) -> dict:
    """
    Deletes a location record from the database.

    Args:
        _id: The ID of the location record to delete.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message.

    Raises:
        HTTPException 404: If the location record with the given ID is not found.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.delete(
            config.get("LIVESTOCK_ID_URL") + "/locations/" + str(_id),
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()
