from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__, template_folder=".")
DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        default = {
            "medicines": [
                {"id": 1, "name": "Paracetamol 500mg", "category": "Analgesic", "stock": 240, "price": 12.50, "expiry": "2026-08-01", "supplier": "Sun Pharma", "min_stock": 50},
                {"id": 2, "name": "Amoxicillin 250mg", "category": "Antibiotic", "stock": 85, "price": 45.00, "expiry": "2026-03-15", "supplier": "Cipla", "min_stock": 30},
                {"id": 3, "name": "Metformin 500mg", "category": "Antidiabetic", "stock": 18, "price": 22.00, "expiry": "2027-01-10", "supplier": "Dr. Reddy's", "min_stock": 40},
                {"id": 4, "name": "Atorvastatin 10mg", "category": "Cardiovascular", "stock": 130, "price": 35.00, "expiry": "2026-11-20", "supplier": "Lupin", "min_stock": 25},
                {"id": 5, "name": "Omeprazole 20mg", "category": "Antacid", "stock": 9, "price": 18.75, "expiry": "2025-12-31", "supplier": "Zydus", "min_stock": 30},
                {"id": 6, "name": "Cetirizine 10mg", "category": "Antihistamine", "stock": 310, "price": 8.00, "expiry": "2027-05-15", "supplier": "Mankind", "min_stock": 60},
            ],
            "sales": [
                {"id": 1, "medicine_id": 1, "medicine_name": "Paracetamol 500mg", "quantity": 10, "unit_price": 12.50, "total": 125.00, "date": "2025-06-01", "customer": "Ravi Kumar"},
                {"id": 2, "medicine_id": 4, "medicine_name": "Atorvastatin 10mg", "quantity": 5, "unit_price": 35.00, "total": 175.00, "date": "2025-06-02", "customer": "Priya Sharma"},
                {"id": 3, "medicine_id": 6, "medicine_name": "Cetirizine 10mg", "quantity": 20, "unit_price": 8.00, "total": 160.00, "date": "2025-06-02", "customer": "Walk-in"},
                {"id": 4, "medicine_id": 2, "medicine_name": "Amoxicillin 250mg", "quantity": 15, "unit_price": 45.00, "total": 675.00, "date": "2025-06-03", "customer": "Anjali Reddy"},
                {"id": 5, "medicine_id": 3, "medicine_name": "Metformin 500mg", "quantity": 30, "unit_price": 22.00, "total": 660.00, "date": "2025-06-03", "customer": "Suresh Rao"},
            ],
            "next_med_id": 7,
            "next_sale_id": 6
        }
        save_data(default)
        return default
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def index():
<<<<<<< HEAD
    return render_template("index.html")
=======
    return render_template("meditrack-fixed.html")
>>>>>>> f31cbe00435b9ea8786374f6360deb77df82be42

@app.route("/api/dashboard")
def dashboard():
    data = load_data()
    meds = data["medicines"]
    sales = data["sales"]
    total_stock_value = sum(m["stock"] * m["price"] for m in meds)
    total_revenue = sum(s["total"] for s in sales)
    low_stock = [m for m in meds if m["stock"] <= m["min_stock"]]
    today = datetime.now().strftime("%Y-%m-%d")
    expiring_soon = [m for m in meds if m["expiry"] <= "2026-01-01"]
    return jsonify({
        "total_medicines": len(meds),
        "total_stock_value": round(total_stock_value, 2),
        "total_revenue": round(total_revenue, 2),
        "total_sales": len(sales),
        "low_stock_count": len(low_stock),
        "low_stock_items": low_stock,
        "expiring_soon": expiring_soon,
        "recent_sales": sorted(sales, key=lambda x: x["date"], reverse=True)[:5]
    })

@app.route("/api/medicines", methods=["GET"])
def get_medicines():
    data = load_data()
    return jsonify(data["medicines"])

@app.route("/api/medicines", methods=["POST"])
def add_medicine():
    data = load_data()
    body = request.json
    med = {
        "id": data["next_med_id"],
        "name": body["name"],
        "category": body["category"],
        "stock": int(body["stock"]),
        "price": float(body["price"]),
        "expiry": body["expiry"],
        "supplier": body["supplier"],
        "min_stock": int(body.get("min_stock", 20))
    }
    data["medicines"].append(med)
    data["next_med_id"] += 1
    save_data(data)
    return jsonify(med), 201

@app.route("/api/medicines/<int:med_id>", methods=["PUT"])
def update_medicine(med_id):
    data = load_data()
    body = request.json
    for m in data["medicines"]:
        if m["id"] == med_id:
            m.update({k: body[k] for k in body if k != "id"})
            save_data(data)
            return jsonify(m)
    return jsonify({"error": "Not found"}), 404

@app.route("/api/medicines/<int:med_id>", methods=["DELETE"])
def delete_medicine(med_id):
    data = load_data()
    data["medicines"] = [m for m in data["medicines"] if m["id"] != med_id]
    save_data(data)
    return jsonify({"ok": True})

@app.route("/api/sales", methods=["GET"])
def get_sales():
    data = load_data()
    return jsonify(sorted(data["sales"], key=lambda x: x["date"], reverse=True))

@app.route("/api/sales", methods=["POST"])
def add_sale():
    data = load_data()
    body = request.json
    med = next((m for m in data["medicines"] if m["id"] == int(body["medicine_id"])), None)
    if not med:
        return jsonify({"error": "Medicine not found"}), 404
    qty = int(body["quantity"])
    if med["stock"] < qty:
        return jsonify({"error": "Insufficient stock"}), 400
    med["stock"] -= qty
    total = round(qty * med["price"], 2)
    sale = {
        "id": data["next_sale_id"],
        "medicine_id": med["id"],
        "medicine_name": med["name"],
        "quantity": qty,
        "unit_price": med["price"],
        "total": total,
        "date": body.get("date", datetime.now().strftime("%Y-%m-%d")),
        "customer": body.get("customer", "Walk-in")
    }
    data["sales"].append(sale)
    data["next_sale_id"] += 1
    save_data(data)
    return jsonify(sale), 201

if __name__ == "__main__":
<<<<<<< HEAD
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode, host="0.0.0.0", port=port)
=======
    app.run(debug=True, port=5000)
>>>>>>> f31cbe00435b9ea8786374f6360deb77df82be42
