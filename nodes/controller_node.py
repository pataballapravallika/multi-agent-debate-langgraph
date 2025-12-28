from nodes.logger_node import log_event

def controller_node(state):
    state["current_turn"] = "AgentB" if state["current_turn"] == "AgentA" else "AgentA"
    state["round"] += 1
    log_event("ControllerNode", {
        "round": state["round"],
        "next_turn": state["current_turn"]
    })
    return state
