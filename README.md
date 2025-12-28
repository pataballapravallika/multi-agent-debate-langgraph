This project implements a CLI-based multi-agent debate system using a LangGraph-style DAG.

Two agents debate a user-provided topic for exactly 8 rounds with strict turn control,
memory management, repetition prevention, and logging.

A Judge node evaluates the debate and declares a winner with justification.

Note: A mock LLM is used to ensure deterministic execution without requiring paid API keys.
The architecture is LLM-ready and can be extended easily.
