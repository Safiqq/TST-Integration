"""
This module defines Pydantic models for managing location records in the application.
"""
from pydantic import BaseModel


class Location(BaseModel):
    """
    Represents a location record with the following properties:

    * **type**: The type of the location (e.g., farm, pasture, etc.).
    * **name**: The name of the location.
    * **address**: The address of the location.
    """

    type: str
    name: str
    address: str

