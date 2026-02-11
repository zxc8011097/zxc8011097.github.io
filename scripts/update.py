import json

data = {
    "teams": [
        {"name": "Arsenal", "points": 65},
        {"name": "Liverpool", "points": 64}
    ]
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ data.json 已生成")
