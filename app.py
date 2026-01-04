from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import gridfs
from bson.objectid import ObjectId
from datetime import datetime
from io import BytesIO

app = Flask(__name__)
CORS(app)

# MongoDB Atlas connection (TEMPORARILY hardcoded – secure later)
client = MongoClient(
    "mongodb+srv://Atharva13:Atharva13@multimediadiary.k9ikezm.mongodb.net/multimedia_diary"
)

db = client["multimedia_diary"]
fs = gridfs.GridFS(db)

# ------------------------
# Health check
# ------------------------
@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200


# ------------------------
# Upload diary entry (POST only)
# ------------------------
@app.route("/upload", methods=["POST"])
def upload():
    title = request.form.get("title")
    text_entry = request.form.get("text")
    tags = request.form.get("tags", "").split(",")
    date = datetime.utcnow()

    media_ids = []
    files = request.files.getlist("media")

    for f in files:
        if f and f.filename:
            file_id = fs.put(
                f,
                filename=f.filename,
                content_type=f.content_type
            )
            media_ids.append(str(file_id))

    db.entries.insert_one({
        "title": title,
        "text_entry": text_entry,
        "date": date,
        "tags": tags,
        "media_ids": media_ids
    })

    return jsonify({"message": "Entry uploaded successfully"}), 201


# ------------------------
# Fetch all diary entries
# ------------------------
@app.route("/entries", methods=["GET"])
def get_entries():
    entries = list(db.entries.find().sort("date", -1))

    for e in entries:
        e["_id"] = str(e["_id"])
        e["media_ids"] = [str(mid) for mid in e.get("media_ids", [])]

    return jsonify(entries), 200


# ------------------------
# Stream media from GridFS
# ------------------------
@app.route("/media/<file_id>", methods=["GET"])
def media(file_id):
    try:
        file = fs.get(ObjectId(file_id))
        return send_file(
            BytesIO(file.read()),
            download_name=file.filename,
            mimetype=file.content_type
        )
    except Exception:
        return jsonify({"error": "File not found"}), 404


if __name__ == "__main__":
    app.run()
