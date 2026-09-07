from flask import Flask, request, jsonify, send_from_directory
import os
import secrets

app = Flask(__name__, static_folder="static")

# بيانات المستخدمين التجريبية
USERS = {
    "خالد": {"password": "12", "amount": 150000},
    "اسعد": {"password": "13", "amount": 250000},
    "صديق": {"password": "14", "amount": 350000},
    "الرشيد": {"password": "15", "amount": 0},
}

def money(value):
    return f"{value:,.0f}".replace(",", "،")

@app.get("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.post("/api/login")
def login():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    password = str(data.get("password", "")).strip()
    user = USERS.get(name)

    if not user or not secrets.compare_digest(password, user["password"]):
        return jsonify({"ok": False, "message": "الاسم أو كلمة السر غير صحيحة."}), 401

    amount = user["amount"]
    message = (
        "لقد صرفت هذا الشهر 0 جنيه سوداني."
        if amount == 0
        else f"لقد صرفت في هذا الشهر {money(amount)} جنيه سوداني."
    )

    return jsonify({"ok": True, "name": name, "amount": amount, "message": message})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
