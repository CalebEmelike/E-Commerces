from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..models.product import Product
from sqlalchemy import desc

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    # Get products sorted alphabetically for featured section
    featured_products = db.query(Product)\
        .order_by(Product.name)\
        .all()
    
    # Get latest products sorted by creation time
    latest_products = db.query(Product)\
        .order_by(desc(Product.created_at))\
        .all()
    
    return templates.TemplateResponse("pages/home.html", {
        "request": request,
        "featured_products": featured_products,
        "latest_products": latest_products
    })

@router.get("/shop")
async def shop(request: Request, db: Session = Depends(get_db)):
    products = db.query(Product).all()
    
    return templates.TemplateResponse("pages/shop.html", {
        "request": request,
        "products": products
    })

@router.get("/product/{product_id}")
async def product_detail(request: Request, product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return templates.TemplateResponse("pages/product-detail.html", {
        "request": request,
        "product": product
    })