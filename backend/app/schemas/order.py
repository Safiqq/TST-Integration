import datetime
from pydantic import BaseModel

class Order(BaseModel):
    product_id: int
    quantity: int

class OrderOut(Order):
    order_id: int
    order_date: datetime
    order_status: str
    total_price: int