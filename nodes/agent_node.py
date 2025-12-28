from nodes.mock_llm import generate_argument
from nodes.logger_node import log_event

def agent_node(state, agent_name):
    if state["current_turn"] != agent_name:
        raise Exception("Out of turn")

    used = [t["text"] for t in state["memory"]["turns"]]
    response = generate_argument(agent_name, used)

    log_event(agent_name, response)
    return response
