# Warehouse Management API

A FastAPI-based warehouse management system with SQLite database.

## Features

- **User Management**: Create and authenticate users with different roles
- **Item Management**: Track items with their locations
- **Location Management**: Organize warehouse locations (rows, shelves, bins)
- **Order Management**: Create and track orders with order items
- **RESTful API**: Full CRUD operations for all entities
- **Interactive Documentation**: Auto-generated API docs with Swagger UI

## Project Structure

```
warehouse/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── endpoints/
│   │   │       ├── users.py      # User endpoints
│   │   │       ├── items.py      # Item endpoints
│   │   │       ├── locations.py  # Location endpoints
│   │   │       └── orders.py     # Order endpoints
│   │   ├── core/
│   │   │   └── database.py       # Database configuration
│   │   ├── models/
│   │   │   ├── user.py           # User model
│   │   │   ├── item.py           # Item model
│   │   │   ├── location.py       # Location model
│   │   │   └── order.py          # Order and OrderItem models
│   │   ├── schemas/
│   │   │   ├── user.py           # User Pydantic schemas
│   │   │   └── order.py          # Order Pydantic schemas
│   │   └── main.py               # FastAPI application
│   ├── requirements.txt          # Python dependencies
│   ├── setup.py                  # Database initialization script
│   └── warehouse.db              # SQLite database (created after setup)
└── frontend/                     # Frontend application (to be developed)
```

## Setup Instructions

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Initialize Database

```bash
cd backend
python setup.py
```

This will:
- Create all database tables
- Seed the database with warehouse locations (rows 10-40, shelves 1-40, bins 1-4)

### 3. Run the API Server

```bash
cd backend
uvicorn app.main:app --reload
```

The API will be available at:
- **API Base URL**: http://localhost:8000
- **Interactive Documentation**: http://localhost:8000/docs
- **Alternative Documentation**: http://localhost:8000/redoc

## API Endpoints

### Users
- `GET /api/v1/users` - Get all users
- `POST /api/v1/users` - Create a new user
- `POST /api/v1/login` - User login

### Items
- `GET /api/v1/items` - Get all items
- `POST /api/v1/items` - Create a new item

### Locations
- `GET /api/v1/locations` - Get all locations
- `POST /api/v1/locations` - Create a new location

### Orders
- `GET /api/v1/orders` - Get all orders
- `POST /api/v1/orders` - Create a new order

## Database Models

### User
- `id`: Primary key
- `username`: Unique username
- `password`: User password
- `role`: User role (e.g., "admin", "worker")

### Item
- `id`: Primary key
- `name`: Item name
- `location_id`: Foreign key to Location

### Location
- `id`: Primary key
- `name`: Location name (format: "row-shelf-bin")

### Order
- `id`: Primary key
- `user_id`: Foreign key to User
- `status`: Order status (default: "new")

### OrderItem
- `id`: Primary key
- `order_id`: Foreign key to Order
- `item_id`: Foreign key to Item
- `quantity`: Item quantity

## Development

### Adding New Endpoints

1. Create your endpoint in the appropriate file under `app/api/endpoints/`
2. Add the router to `app/main.py`
3. Create Pydantic schemas in `app/schemas/` if needed

### Database Migrations

The project uses SQLAlchemy with SQLite. For production, consider using Alembic for database migrations.

## Next Steps

- [ ] Add password hashing for security
- [ ] Implement JWT authentication
- [ ] Add input validation and error handling
- [ ] Create frontend application
- [ ] Add unit tests
- [ ] Implement inventory tracking
- [ ] Add reporting features

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **SQLite**: Lightweight database
- **Uvicorn**: ASGI server for running FastAPI applications 