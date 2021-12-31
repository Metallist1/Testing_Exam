from fastapi import APIRouter

from services.implementations.customer_service import Customer_Service

router = APIRouter()

customer_service = Customer_Service()


@router.get("/customer/", tags=["customer"])
async def read_all_customers():
    return customer_service.get_all_customers()
