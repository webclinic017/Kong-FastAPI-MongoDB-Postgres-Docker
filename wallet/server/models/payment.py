from typing import Optional
from pydantic import EmailStr, Field, BaseModel


class PaymentSchema(BaseModel):
    amount: float = Field(..., gt=0)
    reason: str = Field(...)
    receiver: str = Field(..., min_length=5)
    is_added: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "amount": 45000000.00,
                "reason": "Lend Money",
                "receiver": "6063606360636063",
                "is_added": True,
            }
        }


class UpdatePaymentModel(BaseModel):
    amount: Optional[float]
    reason: Optional[str]
    receiver: Optional[str]
    is_added: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "amount": 45000000.00,
                "reason": "Lend Money",
                "receiver": "6063606360636063",
                "is_added": True,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
