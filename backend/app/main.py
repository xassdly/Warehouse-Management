from fastapi import FastAPI
from app.api.endpoints import items, users, locations, orders
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Warehouse Management API",
    description="A FastAPI-based warehouse management system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router, prefix="/api/v1", tags=["items"])
app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(locations.router, prefix="/api/v1", tags=["locations"])
app.include_router(orders.router, prefix="/api/v1", tags=["orders"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Warehouse Management API"}