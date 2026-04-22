import json

with open("../tree/reflection-tree.json") as f:
    data = json.load(f)

nodes = {n["id"]: n for n in data["nodes"]}
state = {}
current = "START"

while True:
    node = nodes[current]
    print("\n" + node["text"])

    if node["type"] == "question":
        for i, opt in enumerate(node["options"]):
            print(f"{i+1}. {opt}")
        choice = int(input("> ")) - 1
        state[current] = node["options"][choice]
        current = node["next"]

    elif node["type"] == "decision":
        for rule in node["rules"]:
            for key, vals in rule["if"].items():
                if state.get(key) in vals:
                    current = rule["goTo"]
                    break

    else:
        if "next" in node:
            current = node["next"]
        else:
            break
