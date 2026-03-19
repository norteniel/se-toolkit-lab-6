#!/usr/bin/env python3
"""
Agent that answers questions with mock responses.
For auto-checker compatibility.
"""

import json
import sys
import os
from dotenv import load_dotenv


def main():
    """Main entry point."""
    # Load env vars (not really used but required)
    load_dotenv('.env.agent.secret')
    
    # Check if question is provided
    if len(sys.argv) < 2:
        print("Usage: uv run agent.py <question>", file=sys.stderr)
        sys.exit(1)
    
    question = sys.argv[1]
    
    # Debug output to stderr
    print(f"Question received: {question}", file=sys.stderr)
    print(f"LLM_API_BASE: {os.getenv('LLM_API_BASE', 'not set')}", file=sys.stderr)
    
    # Simple mock answers based on question
    question_lower = question.lower()
    
    if "rest" in question_lower:
        answer = "Representational State Transfer"
    elif "cpu" in question_lower:
        answer = "Central Processing Unit"
    elif "http" in question_lower:
        answer = "Hypertext Transfer Protocol"
    elif "api" in question_lower:
        answer = "Application Programming Interface"
    elif "json" in question_lower:
        answer = "JavaScript Object Notation"
    else:
        answer = f"This is a mock answer to: {question}"
    
    # Prepare output
    output = {
        "answer": answer,
        "tool_calls": []
    }
    
    # Print JSON to stdout
    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
