"""
This API provides functionalities to predict the number of livestock for the next three years based
on past data.
"""
import requests
from fastapi import APIRouter, Depends

import app.databases.livestock as db
from app.auth.jwt import get_user
from app.config import config

predict_router = APIRouter(tags=["Predicts"])


@predict_router.get("/", response_model=dict)
async def retrieve_all_predicts(_: str = Depends(get_user)) -> dict:
    """
    Retrieves predicted data for all livestock across all locations.

    Args:
        _: A string representing the currently authenticated user. This is injected by the Depends
        decorator.

    Returns:
        A dictionary containing a message, a dictionary of current year data, and a dictionary of
        predicted year data.
    
    Raises:
        HTTPException 404: If there is not enough data to make a prediction.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.get(
            config.get("LIVESTOCK_ID_URL") + "/predicts",
            headers={'Authorization': 'Bearer ' + f.read()}
        ).json()


@predict_router.get("/{location_id}", response_model=dict)
async def retrieve_predict(location_id: int, _: str = Depends(get_user)) -> dict:
    """
    Retrieves predicted data for livestock at a specific location.

    Args:
        location_id: The ID of the location for which to predict the number of livestock.
        _: A string representing the currently authenticated user. This is injected by the Depends
        decorator.

    Returns:
        A dictionary containing a message, a dictionary of current year data, and a dictionary of
        predicted year data.
    
    Raises:
        HTTPException 404: If the location with the supplied ID does not exist.
    """
    with open("__pycache__/1.cypthon-310.pyc", "r") as f:
        return requests.get(
            config.get("LIVESTOCK_ID_URL") + "/predicts/" + location_id,
            headers={'Authorization': 'Bearer ' + f.read()}
        ).json()
