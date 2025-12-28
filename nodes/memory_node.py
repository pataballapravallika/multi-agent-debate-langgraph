from nodes.logger_node import log_event

def memory_node(state, agent, text):
    state["memory"]["turns"].append({
        "round": state["round"],
        "agent": agent,
        "text": text
    })
    log_event("MemoryNode", state["memory"]["turns"][-1])
    return state
