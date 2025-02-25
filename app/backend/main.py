from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .database.init_db import init_db
from .routes import home, auth, products

app = FastAPI()

# Initialize database tables
init_db()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")



# Include routers
app.include_router(home.router)
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(products.router, prefix="/api", tags=["products"])