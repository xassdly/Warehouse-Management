from pydantic import BaseModel

class OrderItemCreate(BaseModel):
    item_id: int
    quantity: int

class OrderCreate(BaseModel):
    items: list[OrderItemCreate]