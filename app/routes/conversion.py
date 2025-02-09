from fastapi import APIRouter
from app.services.exchange import get_crypto_price

router = APIRouter(prefix="/convert", tags=["conversion"])

@router.get("/{amount}/{from_currency}/{to_currency}")
def convert_crypto(amount: float, from_currency: str, to_currency: str):
    price = get_crypto_price(f"{from_currency}/{to_currency}")
    converted_amount = amount * price
    return {"from": from_currency, "to": to_currency, "amount": amount, "converted": converted_amount}
