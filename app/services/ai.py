import openai
from app.config import OPENAI_API_KEY

def process_user_query(query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )
    return response["choices"][0]["message"]["content"]
