from fastapi import Depends, FastAPI

from dependencies import get_query_token, get_token_header
from controllers import room_controller, booking_controller, customer_controller

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(room_controller.router)
app.include_router(booking_controller.router)
app.include_router(customer_controller.router)

