from flask import Flask, render_template, request, redirect, send_file
from pymongo import MongoClient
import gridfs
from bson.objectid import ObjectId
from datetime import datetime
from io import BytesIO

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client["multimedia_diary"]
fs = gridfs.GridFS(db)

# Homepage to view entries
@app.route('/')
def index():
    entries = db.entries.find().sort("date", -1)
    return render_template("index.html", entries=entries)

# Upload form
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        title = request.form['title']
        text_entry = request.form['text']
        tags = request.form['tags'].split(',')
        date = datetime.utcnow()

        media_ids = []
        files = request.files.getlist("media")
        for f in files:
            if f.filename != '':
                file_type = f.content_type.split('/')[0]  # image, audio, video
                file_id = fs.put(f, filename=f.filename, file_type=file_type)
                media_ids.append(file_id)

        entry_id = db.entries.insert_one({
            "title": title,
            "text_entry": text_entry,
            "date": date,
            "tags": tags,
            "media_ids": media_ids
        }).inserted_id

        return redirect('/')
    
    return render_template("upload.html")

# Media viewer
@app.route('/media/<file_id>')
def media(file_id):
    file = fs.get(ObjectId(file_id))
    return send_file(BytesIO(file.read()), download_name=file.filename, mimetype=file.content_type)



if __name__ == '__main__':
    app.run(debug=True)

