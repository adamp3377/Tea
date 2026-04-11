from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)
DATA_FILE = "tea_data.json"
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "tea_admin")


def check_auth():
    auth_header = request.headers.get("Authorization", "")
    return auth_header == ADMIN_PASSWORD


@app.route("/api/auth", methods=["POST"])
def check_password():
    password = request.json.get("password", "")
    if password == ADMIN_PASSWORD:
        return jsonify({"success": True})
    return jsonify({"success": False}), 401


DEFAULT_DATA = {
    "categories": [
        {"id": 1, "name": "Japanese Green Tea"},
        {"id": 2, "name": "Black Tea"},
        {"id": 3, "name": "Oolong Tea"},
        {"id": 4, "name": "White Tea"},
        {"id": 5, "name": "Chinese Green Tea"},
        {"id": 6, "name": "Yellow Tea"},
    ],
    "methods": [
        {"id": 1, "name": "Kyusu (120ml)", "volume": "120ml"},
        {"id": 2, "name": "Kyusu (240ml)", "volume": "240ml"},
        {"id": 3, "name": "Gaiwan (120ml)", "volume": "120ml"},
        {"id": 4, "name": "Casual (500ml)", "volume": "500ml"},
        {"id": 5, "name": "Chawan (Koicha)", "volume": "100ml"},
        {"id": 6, "name": "Chawan (Usucha)", "volume": "150ml"},
        {"id": 7, "name": "Chawan (Casual)", "volume": "300ml"},
    ],
    "teas": [
        {
            "id": 1,
            "name": "Matcha",
            "category_id": 1,
            "method_id": 5,
            "leaf_amount": "2 scoops",
            "temperature": "80°C",
            "steeping_time": "Whisk slowly until smooth",
        },
        {
            "id": 2,
            "name": "Matcha",
            "category_id": 1,
            "method_id": 6,
            "leaf_amount": "1 scoop",
            "temperature": "80°C",
            "steeping_time": "Whisk vigorously in W shape",
        },
        {
            "id": 3,
            "name": "Matcha",
            "category_id": 1,
            "method_id": 7,
            "leaf_amount": "0.5 scoops",
            "temperature": "Room temp",
            "steeping_time": "Shake or whisk briefly",
        },
        {
            "id": 4,
            "name": "Sencha",
            "category_id": 1,
            "method_id": 2,
            "leaf_amount": "5g",
            "temperature": "80°C",
            "steeping_time": "1st: 1min, 2nd: 20s, 3rd: ≥1min",
        },
        {
            "id": 3,
            "name": "Sencha",
            "category_id": 1,
            "method_id": 4,
            "leaf_amount": "2g",
            "temperature": "~80°C",
            "steeping_time": "2min",
        },
        {
            "id": 4,
            "name": "Shincha",
            "category_id": 1,
            "method_id": 1,
            "leaf_amount": "3g",
            "temperature": "80°C",
            "steeping_time": "1st: 40s, 2nd: 20s, 3rd: ≥30s",
        },
        {
            "id": 5,
            "name": "Shincha",
            "category_id": 1,
            "method_id": 4,
            "leaf_amount": "3g",
            "temperature": "~80°C",
            "steeping_time": "2min",
        },
        {
            "id": 6,
            "name": "Gyokuro",
            "category_id": 1,
            "method_id": 1,
            "leaf_amount": "4g",
            "temperature": "60°C",
            "steeping_time": "1st: 1min 30s, 2nd: 50s, 3rd: ≥1min 30s",
        },
        {
            "id": 7,
            "name": "Gyokuro",
            "category_id": 1,
            "method_id": 4,
            "leaf_amount": "2g",
            "temperature": "~80°C",
            "steeping_time": "2min",
        },
        {
            "id": 8,
            "name": "Kukicha",
            "category_id": 1,
            "method_id": 2,
            "leaf_amount": "5g",
            "temperature": "80°C",
            "steeping_time": "1st: 30s, 2nd: 20s, 3rd: ≥30s",
        },
        {
            "id": 9,
            "name": "Kukicha",
            "category_id": 1,
            "method_id": 4,
            "leaf_amount": "2g",
            "temperature": "~80°C",
            "steeping_time": "2min",
        },
        {
            "id": 10,
            "name": "Bancha",
            "category_id": 1,
            "method_id": 2,
            "leaf_amount": "5g",
            "temperature": "~80°C",
            "steeping_time": "1st: 20s, 2nd: 15s, next: +5s",
        },
        {
            "id": 11,
            "name": "Bancha",
            "category_id": 1,
            "method_id": 4,
            "leaf_amount": "4g",
            "temperature": "~80°C",
            "steeping_time": "2min",
        },
        {
            "id": 12,
            "name": "Hojicha",
            "category_id": 1,
            "method_id": 3,
            "leaf_amount": "4g",
            "temperature": "80°C",
            "steeping_time": "1st: 15s, 2nd: 10s, next: +5s",
        },
        {
            "id": 13,
            "name": "Hojicha",
            "category_id": 1,
            "method_id": 4,
            "leaf_amount": "3g",
            "temperature": "~80°C",
            "steeping_time": "30s",
        },
        {
            "id": 14,
            "name": "Genmaicha",
            "category_id": 1,
            "method_id": 3,
            "leaf_amount": "4g",
            "temperature": "80°C",
            "steeping_time": "1st: 15s, 2nd: 10s, next: +5s",
        },
        {
            "id": 15,
            "name": "Genmaicha",
            "category_id": 1,
            "method_id": 4,
            "leaf_amount": "4g",
            "temperature": "~80°C",
            "steeping_time": "1min",
        },
        {
            "id": 16,
            "name": "Ceylon",
            "category_id": 2,
            "method_id": 3,
            "leaf_amount": "5g",
            "temperature": "90°C",
            "steeping_time": "1st: 20s, 2nd: 15s, next: +5s",
        },
        {
            "id": 17,
            "name": "Ceylon",
            "category_id": 2,
            "method_id": 4,
            "leaf_amount": "3g",
            "temperature": "~100°C",
            "steeping_time": "3min",
        },
        {
            "id": 18,
            "name": "Wakocha",
            "category_id": 2,
            "method_id": 3,
            "leaf_amount": "5g",
            "temperature": "90°C",
            "steeping_time": "1st: 15s, 2nd: 10s, next: +5s",
        },
        {
            "id": 19,
            "name": "Wakocha",
            "category_id": 2,
            "method_id": 4,
            "leaf_amount": "~2g",
            "temperature": "~100°C",
            "steeping_time": "2min",
        },
        {
            "id": 20,
            "name": "Darjeeling First Flush",
            "category_id": 2,
            "method_id": 3,
            "leaf_amount": "5g",
            "temperature": "90°C",
            "steeping_time": "1st: 15s, 2nd: 10s, next: +5s",
        },
        {
            "id": 21,
            "name": "Darjeeling First Flush",
            "category_id": 2,
            "method_id": 4,
            "leaf_amount": "3g",
            "temperature": "~100°C",
            "steeping_time": "3min",
        },
        {
            "id": 22,
            "name": "Yin Ya (Golden Bud)",
            "category_id": 2,
            "method_id": 3,
            "leaf_amount": "5g",
            "temperature": "90°C",
            "steeping_time": "1st: 15s, 2nd: 10s, next: +5s",
        },
        {
            "id": 23,
            "name": "Yin Ya (Golden Bud)",
            "category_id": 2,
            "method_id": 4,
            "leaf_amount": "3g",
            "temperature": "~100°C",
            "steeping_time": "3min",
        },
        {
            "id": 24,
            "name": "Tie Guan Yin",
            "category_id": 3,
            "method_id": 3,
            "leaf_amount": "5g",
            "temperature": "80°C",
            "steeping_time": "1st: 20s, 2nd: 15s, next: +5s",
        },
        {
            "id": 25,
            "name": "Tie Guan Yin",
            "category_id": 3,
            "method_id": 4,
            "leaf_amount": "~2.5g",
            "temperature": "~80°C",
            "steeping_time": "5min",
        },
        {
            "id": 26,
            "name": "Vietnam Oolong",
            "category_id": 3,
            "method_id": 3,
            "leaf_amount": "5g",
            "temperature": "80°C",
            "steeping_time": "1st: 20s, 2nd: 15s, next: +5s",
        },
        {
            "id": 27,
            "name": "Vietnam Oolong",
            "category_id": 3,
            "method_id": 4,
            "leaf_amount": "~2.5g",
            "temperature": "~80°C",
            "steeping_time": "5min",
        },
        {
            "id": 28,
            "name": "Jin Xuan (Milk Oolong)",
            "category_id": 3,
            "method_id": 3,
            "leaf_amount": "5g",
            "temperature": "80°C",
            "steeping_time": "1st: 20s, 2nd: 15s, next: +5s",
        },
        {
            "id": 29,
            "name": "Jin Xuan (Milk Oolong)",
            "category_id": 3,
            "method_id": 4,
            "leaf_amount": "~2.5g",
            "temperature": "~80°C",
            "steeping_time": "5min",
        },
        {
            "id": 30,
            "name": "Phoenix Pearl",
            "category_id": 3,
            "method_id": 3,
            "leaf_amount": "6g",
            "temperature": "80°C",
            "steeping_time": "1st: 20s, 2nd: 15s, next: +5s",
        },
        {
            "id": 31,
            "name": "Phoenix Pearl",
            "category_id": 3,
            "method_id": 4,
            "leaf_amount": "~2.5g",
            "temperature": "~80°C",
            "steeping_time": "5min",
        },
        {
            "id": 32,
            "name": "Bai Hao Yin Zhen",
            "category_id": 4,
            "method_id": 3,
            "leaf_amount": "4g",
            "temperature": "80°C",
            "steeping_time": "1st: 25s, 2nd: 20s, next: +5s",
        },
        {
            "id": 33,
            "name": "Bai Hao Yin Zhen",
            "category_id": 4,
            "method_id": 4,
            "leaf_amount": "3g",
            "temperature": "~80°C",
            "steeping_time": "6min",
        },
        {
            "id": 34,
            "name": "Pai Mu Tan",
            "category_id": 4,
            "method_id": 3,
            "leaf_amount": "4g",
            "temperature": "80°C",
            "steeping_time": "1st: 25s, 2nd: 20s, next: +5s",
        },
        {
            "id": 35,
            "name": "Pai Mu Tan",
            "category_id": 4,
            "method_id": 4,
            "leaf_amount": "3g",
            "temperature": "~80°C",
            "steeping_time": "2min",
        },
        {
            "id": 36,
            "name": "Zhu Cha (Gunpowder)",
            "category_id": 5,
            "method_id": 3,
            "leaf_amount": "4g",
            "temperature": "80°C",
            "steeping_time": "1st: 20s, 2nd: 15s, next: +5s",
        },
        {
            "id": 37,
            "name": "Zhu Cha (Gunpowder)",
            "category_id": 5,
            "method_id": 4,
            "leaf_amount": "3g",
            "temperature": "~80°C",
            "steeping_time": "1min",
        },
        {
            "id": 38,
            "name": "Chun Mee",
            "category_id": 5,
            "method_id": 3,
            "leaf_amount": "4g",
            "temperature": "80°C",
            "steeping_time": "1st: 20s, 2nd: 15s, next: +5s",
        },
        {
            "id": 39,
            "name": "Chun Mee",
            "category_id": 5,
            "method_id": 4,
            "leaf_amount": "2g",
            "temperature": "~80°C",
            "steeping_time": "1min",
        },
        {
            "id": 40,
            "name": "Huang Xiao",
            "category_id": 6,
            "method_id": 3,
            "leaf_amount": "4g",
            "temperature": "80°C",
            "steeping_time": "1st: 25s, 2nd: 20s, next: +5s",
        },
        {
            "id": 41,
            "name": "Huang Xiao",
            "category_id": 6,
            "method_id": 4,
            "leaf_amount": "3g",
            "temperature": "~80°C",
            "steeping_time": "1min",
        },
    ],
    "next_category_id": 7,
    "next_method_id": 8,
    "next_tea_id": 44,
}


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_DATA.copy()


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.route("/")
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.route("/api/categories", methods=["GET"])
def get_categories():
    data = load_data()
    result = []
    for cat in data["categories"]:
        teas = [t for t in data["teas"] if t["category_id"] == cat["id"]]
        teas_dict = {}
        for tea in teas:
            tea_name = tea["name"]
            if tea_name not in teas_dict:
                teas_dict[tea_name] = {
                    "id": tea["id"],
                    "name": tea_name,
                    "variations": [],
                }
            method = next(
                (m for m in data["methods"] if m["id"] == tea["method_id"]), None
            )
            teas_dict[tea_name]["variations"].append(
                {
                    "id": tea["id"],
                    "method": method["name"] if method else None,
                    "method_volume": method["volume"] if method else None,
                    "leaf_amount": tea.get("leaf_amount"),
                    "temperature": tea.get("temperature"),
                    "steeping_time": tea.get("steeping_time"),
                }
            )
        result.append(
            {"id": cat["id"], "name": cat["name"], "teas": list(teas_dict.values())}
        )
    return jsonify(result)


@app.route("/api/categories", methods=["POST"])
def add_category():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401
    data = load_data()
    new_cat = {
        "id": data["next_category_id"],
        "name": request.json.get("name", "").strip(),
    }
    data["categories"].append(new_cat)
    data["next_category_id"] += 1
    save_data(data)
    return jsonify({"id": new_cat["id"], "name": new_cat["name"], "teas": []}), 201


@app.route("/api/categories/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401
    data = load_data()
    data["teas"] = [t for t in data["teas"] if t["category_id"] != category_id]
    data["categories"] = [c for c in data["categories"] if c["id"] != category_id]
    save_data(data)
    return jsonify({"success": True})


@app.route("/api/teas", methods=["POST"])
def add_tea():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401
    data = load_data()
    req = request.json
    method = next(
        (m for m in data["methods"] if m["name"] == req.get("method_name", "").strip()),
        None,
    )
    new_tea = {
        "id": data["next_tea_id"],
        "name": req.get("name", "").strip(),
        "category_id": int(req.get("category_id")),
        "method_id": method["id"] if method else None,
        "leaf_amount": req.get("leaf_amount") or None,
        "temperature": req.get("temperature") or None,
        "steeping_time": req.get("steeping_time") or None,
    }
    data["teas"].append(new_tea)
    data["next_tea_id"] += 1
    save_data(data)
    return jsonify({"id": new_tea["id"], "name": new_tea["name"]}), 201


@app.route("/api/teas/<int:tea_id>", methods=["PUT"])
def update_tea(tea_id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401
    data = load_data()
    req = request.json
    for tea in data["teas"]:
        if tea["id"] == tea_id:
            method = next(
                (
                    m
                    for m in data["methods"]
                    if m["name"] == req.get("method_name", "").strip()
                ),
                None,
            )
            tea["name"] = req.get("name", "").strip()
            tea["category_id"] = int(req.get("category_id"))
            tea["method_id"] = method["id"] if method else None
            tea["leaf_amount"] = req.get("leaf_amount") or None
            tea["temperature"] = req.get("temperature") or None
            tea["steeping_time"] = req.get("steeping_time") or None
            break
    save_data(data)
    return jsonify({"success": True})


@app.route("/api/teas/<int:tea_id>", methods=["DELETE"])
def delete_tea(tea_id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401
    data = load_data()
    data["teas"] = [t for t in data["teas"] if t["id"] != tea_id]
    save_data(data)
    return jsonify({"success": True})


@app.route("/api/methods", methods=["GET"])
def get_methods():
    data = load_data()
    return jsonify(data["methods"])


@app.route("/api/stats", methods=["GET"])
def get_stats():
    data = load_data()
    return jsonify(
        {"teaCount": len(data["teas"]), "categoryCount": len(data["categories"])}
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
