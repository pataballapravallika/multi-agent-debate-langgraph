from nodes.logger_node import log_event

def user_input_node(state):
    topic = input("Enter topic for debate: ").strip()
    if len(topic) < 5:
        raise ValueError("Topic too short")

    state["topic"] = {"turns": []}
    state["round"] = 1
    state["current_turn"] = "AgentA"
    state["memory"] = {"turns": []}

    log_event("UserInputNode", topic)
    return state
