import sys

from agent import generate_content
from call_function import call_function
from cli import get_user_input
from client import get_client


def main():
    client = get_client()
    messages, is_verbose = get_user_input()
    is_task_finished: bool = False

    for _ in range(20):
        message, _ = generate_content(client, messages, is_verbose)
        messages.append(message.model_dump())
        content = message.content or ""

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, is_verbose)
                messages.append(result_message)
                if is_verbose:
                    print(f"-> {result_message['content']}")
                else:
                    print(result_message)
        else:
            print(content)
            is_task_finished = True
            break

    if not is_task_finished:
        print(
            "\nError: Maximum number of iterations (20) reached. "
            "The model failed to produce a final response.",
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
