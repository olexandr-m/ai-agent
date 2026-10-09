from collections.abc import Iterable
from typing import Any, cast

from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam


def generate_content(
    client: OpenAI, messages: list[dict[str, Any]]
) -> tuple[str, ChatCompletion]:
    valid_messages = cast(Iterable[ChatCompletionMessageParam], messages)

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=valid_messages,
    )

    if response.usage is not None:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    else:
        raise RuntimeError("API request faild.")

    content = response.choices[0].message.content or ""

    return content, response
