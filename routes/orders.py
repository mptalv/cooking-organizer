from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.order_schema import OrderCreate
from services.manager import KitchenManager

router = APIRouter()

manager = KitchenManager()


@router.post("/orders")
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):

    return manager.process_order(db, order)