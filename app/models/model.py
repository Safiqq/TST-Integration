"""
This module defines the SQLAlchemy models used to manage location and livestock data within the
application.
"""
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship, mapped_column

Base = declarative_base()


# pylint: disable-next=too-few-public-methods
class LocationDB(Base):
    """
    Represents a location record in the database.

    Attributes:
        id: The unique identifier of the location.
        type: The type of the location (farm, market, warehouse).
        name: The name of the location.
        address: The address of the location.
    """

    __tablename__ = "location"
    id = mapped_column(sa.Integer, primary_key=True)
    type = mapped_column(sa.Enum("farm", "market", "warehouse"), nullable=False)
    name = mapped_column(sa.String(100), nullable=False)
    address = mapped_column(sa.String(255), nullable=False)

    # pylint: disable-next=too-few-public-methods
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "livestock_id": self.type,
            "product_id": self.name,
        }
