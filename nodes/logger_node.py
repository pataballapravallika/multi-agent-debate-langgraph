import json
from datetime import datetime

def log_event(node, data):
    with open("logs/debate_log.jsonl", "a") as f:
        f.write(json.dumps({
            "time": datetime.utcnow().isoformat(),
            "node": node,
            "data": data
        }) + "\n")
