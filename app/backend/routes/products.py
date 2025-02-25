from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
# from backend.database import get_db
from ..database.database import get_db
from ..models.product import Product
from ..schemas.product import ProductCreate, ProductResponse

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product