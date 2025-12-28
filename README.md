This project implements a CLI-based multi-agent debate system using a LangGraph-style DAG.

Two agents debate a user-provided topic for exactly 8 rounds with strict turn control,
memory management, repetition prevention, and logging.

A Judge node evaluates the debate and declares a winner with justification.

Note: A mock LLM is used to ensure deterministic execution without requiring paid API keys.
The architecture is LLM-ready and can be extended easily.
## Output Screenshots
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/96756d5e-a7ce-4cbb-94cd-4f90bfde6c99" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/77c91bc2-237f-434c-a801-49a57df5f91f" />
