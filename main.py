from agent import generate_content
from call_function import call_function
from cli import get_user_input
from client import get_client


def main():
    client = get_client()
    messages, is_verbose = get_user_input()

    message, _ = generate_content(client, messages, is_verbose)
    content = message.content or ""

    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, is_verbose)
            if is_verbose:
                print(f"-> {result_message['content']}")
            else:
                print(result_message)
    else:
        print(content)


if __name__ == "__main__":
    main()
