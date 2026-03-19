# Agent Architecture

## Overview

This agent is a CLI tool that sends a user question to an LLM and returns a JSON response.

## Components

- agent.py — main entry point
- call_llm() — handles API communication

## Configuration

The agent reads configuration from environment variables:

- LLM_API_KEY — API key
- LLM_API_BASE — API base URL
- LLM_MODEL — model name

## Flow

1. User runs CLI with a question
2. agent.py reads environment variables
3. Sends request to LLM API
4. Parses response
5. Outputs JSON

## Output format

```json
{
  "question": "...",
  "answer": "..."
}
