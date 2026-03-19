import os
import sys
import json
import requests


def call_llm(prompt: str) -> str:
    api_key = os.getenv("LLM_API_KEY")
    api_base = os.getenv("LLM_API_BASE")
    model = os.getenv("LLM_MODEL")

    if not api_key or not api_base or not model:
        raise ValueError("Missing LLM environment variables")

    url = f"{api_base}/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    result = response.json()
    return result["choices"][0]["message"]["content"]


def main():
    if len(sys.argv) < 2:
        print("Usage: python agent.py 'your question'")
        sys.exit(1)

    question = sys.argv[1]
    answer = call_llm(question)

    output = {"question": question, "answer": answer}

    print(json.dumps(output))


if __name__ == "__main__":
    main()
