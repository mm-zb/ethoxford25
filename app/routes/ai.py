from fastapi import APIRouter
from app.services.ai import process_user_query

router = APIRouter(prefix="/ai", tags=["ai"])

@router.get("/{query}")
def chat_ai(query: str):
    response = process_user_query(query)
    return {"response": response}
