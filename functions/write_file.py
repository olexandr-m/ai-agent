import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Creates a new file or overwrites an existing file with the provided text content. It automatically creates missing directories if they do not exist.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path where the file should be saved, relative to the working directory. Must resolve inside the allowed workspace.",
                },
                "content": {
                    "type": "string",
                    "description": "The text content to be written into the file.",
                },
            },
            "required": ["file_path", "content"],
            "additionalProperties": False,
        },
    },
}


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        )

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {e}"
