"""
This module defines Pydantic models for managing livestock records in the application.
"""
from datetime import date
from pydantic import BaseModel


class Livestock(BaseModel):
    """
    Represents a livestock record with the following properties:

    * **name**: The name of the livestock.
    * **breed**: The breed of the livestock.
    * **species**: The species of the livestock.
    * **birthplace_id**: The ID of the location where the livestock was born.
    * **birthdate**: The date of birth of the livestock.
    * **gender**: The gender of the livestock.
    * **location_id**: The ID of the current location of the livestock.
    """

    name: str
    breed: str
    species: str
    birthplace_id: int
    birthdate: date
    gender: str
    location_id: int
