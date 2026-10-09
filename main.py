from agent import generate_content
from cli import get_user_input
from client import get_client


def main():
    client = get_client()
    messages, is_verbose = get_user_input()

    content, _ = generate_content(client, messages, is_verbose)

    print(content)


if __name__ == "__main__":
    main()
