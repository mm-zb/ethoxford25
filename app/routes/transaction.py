from fastapi import APIRouter
from app.services.blockchain import send_transaction

router = APIRouter(prefix="/transaction", tags=["transaction"])

@router.post("/")
def execute_transaction(sender: str, private_key: str, receiver: str, amount: float):
    tx_hash = send_transaction(sender, private_key, receiver, amount)
    return {"status": "success", "transaction_hash": tx_hash}
