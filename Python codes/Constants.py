import os
from dotenv import load_dotenv

load_dotenv()
API_KEY_SERVICE = os.getenv("OPENAI_API_KEY", "")

