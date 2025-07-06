from fastapi import FastAPI
from app.api.endpoints import items, users, locations, orders

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)
app.include_router(locations.router)
app.include_router(orders.router)