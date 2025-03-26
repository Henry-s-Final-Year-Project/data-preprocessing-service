from fastapi import FastAPI
from app.models.card_transaction import CardTransaction
from app.services.preprocess import preprocess_transaction

app = FastAPI()


@app.post("/preprocess")
def preprocess(tx: CardTransaction):
    print("Received:", tx.dict())
    return {"features": preprocess_transaction(tx.dict())}
