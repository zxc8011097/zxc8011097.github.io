# scripts/update.py
import json
import os
from datetime import datetime
import random

def generate_football_data():
    base_data = {
        "热那亚": {"elo": 0.92, "form": "LWDL", "attack": 0.98, "defense": 1.05, "trend": "防守尚可"},
        "那不勒斯": {"elo": 1.15, "form": "WWLD", "attack": 1.18, "defense": 0.92, "trend": "攻击强势"},
        "皇马": {"elo": 1.13, "form": "DWWW", "attack": 1.22, "defense": 0.88, "trend": "状态正佳"},
        "曼城": {"elo": 1.14, "form": "WWWD", "attack": 1.25, "defense": 0.85, "trend": "控场为主"},
        "利物浦": {"elo": 1.12, "form": "WLWW", "attack": 1.20, "defense": 0.90, "trend": "攻势足球"},
        "拜仁慕尼黑": {"elo": 1.16, "form": "WWLW", "attack": 1.23, "defense": 0.87, "trend": "德甲霸主"},
    }
    
    today_str = datetime.now().strftime("%Y%m%d")
    for team, stats in base_data.items():
        random.seed(f"{today_str}{team}")
        change = random.uniform(-0.015, 0.015)
        stats["elo"] = round(stats["elo"] + change, 3)
    
    return base_data

def main():
    print("开始生成最新足球数据...")
    team_data = generate_football_data()
    
    output_data = {
        "success": True,
        "message": "数据更新成功 (GitHub Actions)",
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": team_data
    }
    
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(repo_root, 'data.json')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 数据已保存至: {output_path}")
    print(f"🕒 更新时间: {output_data['update_time']}")

if __name__ == '__main__':
    main()
