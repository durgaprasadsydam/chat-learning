import os

import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not configured.")


genai.configure(
    api_key=GOOGLE_API_KEY
)


model = genai.GenerativeModel(
    "gemini-3.6-flash"
)


def ask_gemini(question: str) -> str:

    response = model.generate_content(
        question
    )

    return response.text