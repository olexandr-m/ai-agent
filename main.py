import argparse

from agent import generate_content
from client import get_client

client = get_client()


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    content, _ = generate_content(client, messages)

    print(content)


if __name__ == "__main__":
    main()
