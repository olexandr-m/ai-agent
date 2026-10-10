from collections.abc import Iterable
from typing import Any, cast

from openai import OpenAI
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionToolUnionParam,
)

from call_function import available_functions


def generate_content(
    client: OpenAI, messages: list[dict[str, Any]], is_verbose: bool
) -> tuple[ChatCompletionMessage, ChatCompletion]:
    valid_messages = cast(Iterable[ChatCompletionMessageParam], messages)
    valid_available_functions = cast(
        Iterable[ChatCompletionToolUnionParam], available_functions
    )
    user_prompt = messages[0].get("content", "")

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=valid_messages,
        tools=valid_available_functions,
        temperature=0,
    )

    if response.usage is None:
        raise RuntimeError("API request faild.")

    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    message = response.choices[0].message

    return message, response
