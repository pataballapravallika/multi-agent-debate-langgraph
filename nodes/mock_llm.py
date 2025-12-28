SCIENTIST_ARGUMENTS = [
    "AI can impact public safety, so regulation is necessary.",
    "High-risk AI systems require strict oversight.",
    "Scientific evidence shows unregulated AI can cause harm.",
    "Medical-style regulation ensures accountability."
]

PHILOSOPHER_ARGUMENTS = [
    "Overregulation limits human creativity and freedom.",
    "Ethical reasoning should evolve without rigid constraints.",
    "Too much control may slow societal progress.",
    "History shows innovation thrives with fewer restrictions."
]

def generate_argument(agent, used_arguments):
    pool = SCIENTIST_ARGUMENTS if agent == "AgentA" else PHILOSOPHER_ARGUMENTS
    for arg in pool:
        if arg not in used_arguments:
            return arg
    return pool[-1]
