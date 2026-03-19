#!/usr/bin/env python3
"""
Agent that calls an LLM to answer questions.
Reads configuration from environment variables (required by auto-checker).
"""

import json
import os
import sys
import requests


def call_llm(question):
    """Call the LLM API with the given question using environment variables."""
    # Read configuration from environment variables (required by auto-checker)
    api_base = os.environ.get('LLM_API_BASE')
    api_key = os.environ.get('LLM_API_KEY')
    model = os.environ.get('LLM_MODEL')
    
    # Debug output to stderr
    print(f"LLM_API_BASE: {api_base}", file=sys.stderr)
    print(f"LLM_MODEL: {model}", file=sys.stderr)
    
    # Check if all required variables are present
    missing_vars = []
    if not api_base:
        missing_vars.append('LLM_API_BASE')
    if not api_key:
        missing_vars.append('LLM_API_KEY')
    if not model:
        missing_vars.append('LLM_MODEL')
    
    if missing_vars:
        print(f"Error: Missing required environment variables: {', '.join(missing_vars)}", file=sys.stderr)
        print("These variables must be set by the auto-checker", file=sys.stderr)
        sys.exit(1)
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Answer the user's question concisely."},
        {"role": "user", "content": question}
    ]
    
    payload = {
        'model': model,
        'messages': messages,
        'temperature': 0.7,
        'max_tokens': 500
    }
    
    try:
        # Make the API call
        response = requests.post(
            f"{api_base.rstrip('/')}/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        
        # Parse the response
        result = response.json()
        answer = result['choices'][0]['message']['content']
        return answer
        
    except requests.exceptions.RequestException as e:
        print(f"Error calling LLM API: {e}", file=sys.stderr)
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}", file=sys.stderr)
        sys.exit(1)
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"Error parsing LLM response: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point."""
    # Check if question is provided
    if len(sys.argv) < 2:
        print("Usage: python agent.py <question>", file=sys.stderr)
        sys.exit(1)
    
    question = sys.argv[1]
    
    # Call LLM
    answer = call_llm(question)
    
    # Prepare output
    output = {
        "answer": answer,
        "tool_calls": []
    }
    
    # Print JSON to stdout
    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
