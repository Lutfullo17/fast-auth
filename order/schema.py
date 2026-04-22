from pydantic import BaseModel
from typing import Optional


class CardItemschema(BaseModel):
    product_id: int
    quantity: int
    