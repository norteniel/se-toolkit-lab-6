# Task 1: Call an LLM from Code

## Goal

Implement a CLI agent that calls an LLM and returns a JSON response.

## Steps

1. Create CLI entry point (agent.py)
2. Read config from environment:
   - LLM_API_KEY
   - LLM_API_BASE
   - LLM_MODEL
3. Send user input to LLM
4. Return structured JSON:
   {
     "question": "...",
     "answer": "..."
   }
5. Add regression test
6. Document architecture in AGENT.md

## Risks

- Missing environment variables
- Invalid JSON output

## Success Criteria

- CLI works
- Uses env variables
- Test passes
