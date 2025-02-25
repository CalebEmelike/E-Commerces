from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    description: str
    image_url: str
    category: str

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True