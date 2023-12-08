"""
This API provides functionalities to manage livestock records, including creating, retrieving,
updating, and deleting records.
"""
from typing import List

import requests
from fastapi import APIRouter, Body, Depends

import app.databases.location as db_lo
import app.databases.livestock as db_li
from app.schemas.livestock import Livestock
from app.auth.jwt import get_user
from app.config import config

livestock_router = APIRouter(tags=["Livestocks"])


@livestock_router.post("/")
async def create_livestock(
    livestock: Livestock = Body(...), _: str = Depends(get_user)
) -> dict:
    """
    Creates a new livestock record in the database.

    Args:
        livestock: A Livestock object containing information about the new livestock.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message and the ID of the newly created livestock record.
    
    Raises:
        HTTPException 404: If the specified location IDs (birthplace or current) do not exist.
        HTTPException 500: If an error occurs while creating the livestock record.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.post(
            config.get("LIVESTOCK_ID_URL") + "/livestocks",
            headers={'Authorization': 'Bearer ' + f.read()},
            json=dict(livestock),
        ).json()


@livestock_router.get("/", response_model=List[dict])
async def retrieve_all_livestocks(_: str = Depends(get_user)) -> List[dict]:
    """
    Retrieves a list of all livestock records from the database.

    Args:
        current_user: The currently authenticated user.

    Returns:
        A list of dictionaries, each representing a livestock record.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.get(
            config.get("LIVESTOCK_ID_URL") + "/livestocks",
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()


@livestock_router.get("/{_id}", response_model=dict)
async def retrieve_livestock(_id: int, _: str = Depends(get_user)) -> dict:
    """
    Retrieves a specific livestock record by its ID.

    Args:
        _id: The ID of the livestock record to retrieve.
        current_user: The currently authenticated user.

    Returns:
        A dictionary representing the livestock record.

    Raises:
        HTTPException 404: If the livestock record with the given ID is not found.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.get(
            config.get("LIVESTOCK_ID_URL") + "/livestocks/" + _id,
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()


@livestock_router.patch("/{_id}", response_model=dict)
async def update_livestock(
    _id: int, updated_livestock: dict = Body(...), _: str = Depends(get_user)
) -> dict:
    """
    Updates an existing livestock record in the database.

    Args:
        _id: The ID of the livestock record to update.
        updated_livestock: A dictionary containing updated information for the livestock.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message.

    Raises:
        HTTPException 404: If the livestock record with the given ID is not found.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.patch(
            config.get("LIVESTOCK_ID_URL") + "/livestocks",
            headers={'Authorization': 'Bearer ' + f.read()},
            json=dict(updated_livestock),
        ).json()


@livestock_router.delete("/{_id}", response_model=dict)
async def delete_livestock(_id: int, _: str = Depends(get_user)) -> dict:
    """
    Deletes a livestock record from the database.

    Args:
        _id: The ID of the livestock record to delete.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message.

    Raises:
        HTTPException 404: If the livestock record with the given ID is not found.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.delete(
            config.get("LIVESTOCK_ID_URL") + "/livestocks/" + _id,
            headers={'Authorization': 'Bearer ' + f.read()},
        ).json()
