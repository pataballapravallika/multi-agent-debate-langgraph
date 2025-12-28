from nodes.user_input_node import user_input_node
from nodes.agent_node import agent_node
from nodes.memory_node import memory_node
from nodes.controller_node import controller_node
from nodes.judge_node import judge_node

def main():
    state = {}
    state = user_input_node(state)

    while state["round"] <= 8:
        if state["current_turn"] == "AgentA":
            text = agent_node(state, "AgentA")
            print(f"[Round {state['round']}] Scientist: {text}")
            state = memory_node(state, "AgentA", text)
        else:
            text = agent_node(state, "AgentB")
            print(f"[Round {state['round']}] Philosopher: {text}")
            state = memory_node(state, "AgentB", text)

        state = controller_node(state)

    verdict = judge_node(state)
    print("\n[Judge]")
    print(verdict)

if __name__ == "__main__":
    main()
