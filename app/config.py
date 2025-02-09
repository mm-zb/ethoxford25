import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
