from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

# ==========================================
# MONGODB CONFIGURATION
# ==========================================
MONGO_URI = "mongodb://vangaridinesh60_db_user:Dinesh60@cluster0-shard-00-00.hbc24vk.mongodb.net:27017/student_db?ssl=true&authSource=admin&directConnection=true&tlsAllowInvalidCertificates=true"
client = MongoClient(MONGO_URI)
db = client["student_db"]
collection = db["students"]

def format_student(s):
    return {
        "_id": str(s["_id"]),
        "name": s.get("name", ""),
        "email": s.get("email", ""),
        "phone": s.get("phone", ""),
        "course": s.get("course", ""),
        "department": s.get("department", ""),
        "year": s.get("year", "")
    }

# ==========================================
# ROUTES
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/students", methods=["GET"])
def get_students():
    try:
        students = list(collection.find())
        return jsonify([format_student(s) for s in students]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/students/<id>", methods=["GET"])
def get_student(id):
    try:
        student = collection.find_one({"_id": ObjectId(id)})
        if not student:
            return jsonify({"error": "Student not found"}), 404
        return jsonify(format_student(student)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/students", methods=["POST"])
def add_student():
    try:
        data = request.get_json()
        student_data = {
            "name": data.get("name", ""),
            "email": data.get("email", ""),
            "phone": data.get("phone", ""),
            "course": data.get("course", ""),
            "department": data.get("department", ""),
            "year": data.get("year", "")
        }
        result = collection.insert_one(student_data)
        student_data["_id"] = str(result.inserted_id)
        return jsonify(student_data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/students/<id>", methods=["PUT"])
def update_student(id):
    try:
        data = request.get_json()
        update_data = {
            "name": data.get("name", ""),
            "email": data.get("email", ""),
            "phone": data.get("phone", ""),
            "course": data.get("course", ""),
            "department": data.get("department", ""),
            "year": data.get("year", "")
        }
        result = collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.matched_count == 0:
            return jsonify({"error": "Student not found"}), 404
        return jsonify({"message": "Student updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/students/<id>", methods=["DELETE"])
def delete_student(id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Student not found"}), 404
        return jsonify({"message": "Student deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=False)