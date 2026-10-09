from collections.abc import Iterable
from typing import Any, cast

from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam


def generate_content(
    client: OpenAI, messages: list[dict[str, Any]], is_verbose: bool
) -> tuple[str, ChatCompletion]:
    valid_messages = cast(Iterable[ChatCompletionMessageParam], messages)
    user_prompt = messages[0].get("content", "")

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=valid_messages,
    )

    if response.usage is None:
        raise RuntimeError("API request faild.")

    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    content = response.choices[0].message.content or ""

    return content, response
