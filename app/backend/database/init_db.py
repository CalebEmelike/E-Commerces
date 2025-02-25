from .database import engine, Base, SessionLocal
from ..models.user import User
from ..models.product import Product
from ..initial_data import sample_products

def init_db():
    Base.metadata.create_all(bind=engine)
    
    # Initialize sample products
    db = SessionLocal()
    try:
        # Check if products already exist
        if db.query(Product).count() == 0:
            for product_data in sample_products:
                product = Product(**product_data)
                db.add(product)
            db.commit()
    finally:
        db.close()