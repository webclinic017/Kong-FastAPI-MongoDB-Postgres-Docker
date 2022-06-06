from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import sys

from wallet.server.database import (
    add_object,
    retrieve_object,
    retrieve_objects,
    delete_object,
    update_object,
)

from wallet.server.models.payment import (
    ErrorResponseModel,
    ResponseModel,
    PaymentSchema,
    UpdatePaymentModel,
)

router = APIRouter()


@router.post('/', response_description="Payment stored in Database")
async def add_object_data(payment: PaymentSchema = Body(...)):
    payment = jsonable_encoder(payment)
    new_payment = await add_object(payment)
    return ResponseModel(new_payment, "Payment added successfully.")


@router.get('/', response_description="this is the response description for Retrieve all")
async def retrieve_payment_objects():
    print('------------', sys.getrecursionlimit())
    # sys.setrecursionlimit(1500)
    payments = await retrieve_objects()
    # payments = {}
    if payments:
        return ResponseModel(payments, "Payments data retrieved successfully")
    return ResponseModel(payments, "Empty list returned")


@router.get('/{id}', response_description="this is the response description for Retrieve by id")
async def get_payment_data(id):
    # payment = None
    try:
        payment = await retrieve_object(id)
    except Exception as e:
        return ErrorResponseModel("An Error from db", 600, str(e))
    if payment:
        return ResponseModel(payment, "This is the payment you want.")
    else:
        return ErrorResponseModel("An Error Occurred", 404, "Payment Doesn't exists.")


@router.delete('/{id}', response_description="this is the response description for DELETE")
async def delete_payment(id):
    try:
        deleted_payment = await delete_object(id)
    except Exception as e:
        return ErrorResponseModel("Error from DB", 600, str(e))
    if deleted_payment:
        return ResponseModel(deleted_payment, f'payment {id} is removed.')
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )
