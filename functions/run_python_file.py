import os
import subprocess
from subprocess import CompletedProcess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        )

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        result: list = []

        command = ["python", target_file]
        if args:
            command.extend(args)

        process: CompletedProcess = subprocess.run(
            command,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )

        if process.returncode != 0:
            result.append(f"Process exited with code {process.returncode}")

        if not process.stdout and not process.stderr:
            result.append("No output produced")

        if process.stdout:
            result.append(f"STDOUT: {process.stdout}")

        if process.stderr:
            result.append(f"STDERR: {process.stderr}")

        return "\n".join(result)

    except Exception as e:
        return f"Error: executing Python file: {e}"
