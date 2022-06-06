import os

from bson.objectid import ObjectId
import motor.motor_asyncio

# MONGO_DETAILS = "mongodb://docker:mongopw@localhost:55000"
MONGO_DETAILS = os.environ["DB_URL"]
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.payments

payments_collection = database.get_collection("payments_collection")


# Helpers

def payment_helper(payment) -> dict:
    return {
        "id": str(payment["_id"]),
        "amount": payment["amount"],
        "reason": payment["reason"],
        "receiver": payment["receiver"],
        "is_added": payment["is_added"],
    }


# CRUD

# Retrieve all payments present in the database
async def retrieve_objects():
    payments = []
    async for payment in payments_collection.find():
        payments.append(payment_helper(payment))
    return payments


# Add a new payment into to the database
async def add_object(payment_data: dict) -> dict:
    payment = await payments_collection.insert_one(payment_data)
    new_object = await payments_collection.find_one({"_id": payment.inserted_id})
    return payment_helper(new_object)


# Retrieve a payment with a matching ID
async def retrieve_object(id: str) -> dict:
    payment = await payments_collection.find_one({"_id": ObjectId(id)})
    if payment:
        return payment_helper(payment)


# Update a payment with a matching ID
async def update_object(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    payment = await payments_collection.find_one({"_id": ObjectId(id)})
    if payment:
        updated_object = await payments_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_object:
            return True
        return False


# Delete a payment from the database
async def delete_object(id: str):
    payment = await payments_collection.find_one({"_id": ObjectId(id)})
    if payment:
        await payments_collection.delete_one({"_id": ObjectId(id)})
        return True

