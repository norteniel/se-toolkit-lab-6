# Task 2: Documentation Agent Implementation Plan

## Goal
Create a Documentation Agent that can:
1. Read files from a repository
2. List files in directories
3. Summarize or document code automatically

## Tools
- `read_file(path: str) -> str`  
- `list_files(directory: str) -> List[str]`

## Agent Workflow
1. Receive a prompt from the user asking for documentation.
2. Determine relevant files.
3. Use `list_files` to explore directories.
4. Use `read_file` to read file contents.
5. Generate documentation.

## Output
- Markdown documentation summarizing the code.
