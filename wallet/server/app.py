from fastapi import FastAPI
from .routes.payment import router as PaymentRouter

app = FastAPI()


app.include_router(PaymentRouter, tags=["Payment"], prefix="/wallet/payment")


@app.get("/wallet", tags=["Root"])
async def read_root():
    return {"message": "This Is The Wallet Service"}