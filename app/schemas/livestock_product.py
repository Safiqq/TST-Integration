import uuid
from pydantic import BaseModel

from app.models.model import LivestockProductDB


class LivestockProduct(BaseModel):
    # livestock_id: uuid
    product_id: int

    def to_db(self):
        return LivestockProductDB(**self.model_dump())
