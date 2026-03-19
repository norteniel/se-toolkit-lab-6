import json
import subprocess
import os


def test_agent_runs():
    env = os.environ.copy()
    env["LLM_API_KEY"] = "test"
    env["LLM_API_BASE"] = "https://api.openai.com/v1"
    env["LLM_MODEL"] = "gpt-3.5-turbo"

    result = subprocess.run(
        ["python", "agent.py", "Hello"], capture_output=True, text=True, env=env
    )

    assert result.returncode == 0

    output = json.loads(result.stdout)
    assert "question" in output
    assert "answer" in output
