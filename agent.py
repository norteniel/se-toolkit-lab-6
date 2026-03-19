from typing import List
import os

read_file_schema = {
    "name": "read_file",
    "description": "Reads the content of a file at the given path",
    "parameters": {
        "type": "object",
        "properties": {"path": {"type": "string", "description": "Path to the file"}},
        "required": ["path"],
    },
}

list_files_schema = {
    "name": "list_files",
    "description": "Lists files in a directory",
    "parameters": {
        "type": "object",
        "properties": {
            "directory": {"type": "string", "description": "Directory path"}
        },
        "required": ["directory"],
    },
}


def read_file(path: str) -> str:
    """Reads the content of a file at the given path."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def list_files(directory: str) -> List[str]:
    """Lists files in a directory."""
    return os.listdir(directory)
