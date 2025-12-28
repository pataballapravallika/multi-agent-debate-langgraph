from nodes.logger_node import log_event

def judge_node(state):
    verdict = {
        "summary": "8-round structured debate completed.",
        "winner": "AgentA",
        "reason": "Arguments were consistent and non-repetitive."
    }
    log_event("JudgeNode", verdict)
    return verdict
