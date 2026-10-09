import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("OPENROUTER_API_KEY")


def get_client() -> OpenAI:
    if api_key is None:
        raise RuntimeError("Fail to load api key.")

    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
