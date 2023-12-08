from pydantic import BaseModel

class Product(BaseModel):
    product_id: int
    product_name: str
    product_price: int
    product_stock: int
    product_description: str
