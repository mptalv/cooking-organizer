from fastapi import APIRouter
from services.manager import KitchenManager
from schemas.order_schema import OrderRequest

router = APIRouter()

manager = KitchenManager()


@router.post("/orders")
def create_order(order: OrderRequest):

    result = manager.process_order(
        order.recipe_name,
        order.quantity
    )

    return result