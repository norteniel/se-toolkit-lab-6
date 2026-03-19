# Task 1: Call an LLM from Code - Implementation Plan

## LLM Provider Choice
I will use Qwen Code API (qwen3-coder-plus) running on my VM because:
- It provides 1000 free requests per day
- Works from Russia without credit card
- Good tool-calling support (needed for future tasks)

## Architecture
The agent will:
1. Read configuration from `.env.agent.secret` (API key, base URL, model)
2. Get question from command-line argument
3. Send request to LLM API using OpenAI-compatible format
4. Parse response and output JSON with required fields:
   - `answer`: the LLM's response text
   - `tool_calls`: empty list (for now)

## Implementation Details
- Use `requests` library for HTTP calls
- Use `python-dotenv` for loading environment variables
- System prompt: simple instruction to answer questions
- Error handling: print errors to stderr, exit with non-zero code

## Testing Strategy
- Create one regression test that runs the agent with a simple question
- Verify JSON output has required fields
- Test will be in `tests/test_agent.py`
EOF
