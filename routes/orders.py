from fastapi import APIRouter
from services.manager import KitchenManager

router = APIRouter()

@router.post("/orders")
def create_order():

    manager = KitchenManager()

    result = manager.process_sample_order()

    return result