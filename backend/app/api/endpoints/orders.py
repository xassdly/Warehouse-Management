from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models import order as order_models
from app.models import item as item_models
from app.schemas.order import OrderCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/orders")
def read_orders(db: Session = Depends(get_db)):
    return db.query(order_models.Order).all()


@router.get("/orders/{order_id}")
def read_order(order_id: int, db: Session = Depends(get_db)):
    return db.query(order_models.Order).filter(order_models.Order.id == order_id).first()


@router.post("/orders")
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    new_order = order_models.Order(status="new")
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    order_items = [
        order_models.OrderItem(
            order_id=new_order.id,
            item_id=item.item_id,
            quantity=item.quantity
        )
        for item in order_data.items
    ]
    db.add_all(order_items)
    db.commit()

    return {
        "order_id": new_order.id,
        "status": new_order.status,
        "items": [{"item_id": oi.item_id, "quantity": oi.quantity} for oi in order_items]
    }
