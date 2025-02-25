# E-Commerce Web Application

A modern e-commerce platform built with FastAPI and SQLite, featuring a responsive frontend design.

## Features

- Product catalog with detailed product pages
- User authentication system
- Shopping cart functionality
- Responsive design for mobile and desktop
- Real-time product search
- Category-based product filtering

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy, SQLite
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Template Engine**: Jinja2

## Getting Started

1. Clone the repository:

git clone <repository-url>
cd ECommerce

2. Create and activate virtual environment:

python -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate  # For Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run the application:
uvicorn app.backend.main:app --reload
