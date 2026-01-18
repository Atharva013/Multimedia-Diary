# Multimedia Diary

A personal multimedia journaling application that lets users create daily diary entries with rich media — images, audio, video — in addition to text. Entries are organized by date and can be reviewed or played back later.

This repository contains the full backend (Flask) and frontend (HTML templates & static assets) required to run the diary locally.

---

## Features

* Text-based diary entries
* Upload and attach photos, audio, and video
* Date-wise organization of entries
* Browser-based UI using Flask templates
* Store large files using MongoDB *GridFS*
* Retrieve and stream media from the database

---

## Tech Stack

| Layer    | Technology                   |
| -------- | ---------------------------- |
| Backend  | Python 3, Flask              |
| Database | MongoDB with GridFS          |
| Frontend | HTML, CSS, JavaScript        |
| Storage  | GridFS for large media files |

---

## Repository Structure

```
Multimedia-Diary/
├── .devcontainer/
├── static/               # CSS, JS, media assets
├── templates/            # Jinja2 templates (UI)
├── app.py                # Main Flask application
├── README.md             # Project overview
├── requirements.txt      # Python dependencies
└── .gitignore
```

The repository contains two commits, and templates & static indicate a web application. ([GitHub][1])

---

## Installation

### Prerequisites

Install the following on your system:

* Python 3.8+
* MongoDB server (local or cloud)
* Git

### Clone and Setup

```bash
git clone https://github.com/Atharva013/Multimedia-Diary.git
cd Multimedia-Diary
```

### Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root with:

```
FLASK_APP=app.py
FLASK_ENV=development
MONGO_URI=mongodb://localhost:27017/multimedia_diary
GRIDFS_BUCKET=media
SECRET_KEY=your_secret_key_here
```

Replace the `MONGO_URI` with your MongoDB connection string if using MongoDB Atlas.

---

## Running the Application

Start the server using Flask:

```bash
flask run
```

By default the app will be at:

```
http://127.0.0.1:5000/
```

You can navigate in a web browser to create and view diary entries.

---

## Usage

### Creating Entries

* Navigate to “New Entry”
* Enter a title and text
* Attach one or more media files
* Save

### Viewing Entries

* Navigate to “Entries” or “Home”
* Click on any entry to see text + attached media
* Images will display inline
* Audio and video will have play controls

---

## Media Storage

This application uses **MongoDB GridFS** to handle large binary files:

* Files are stored in the `fs.files` and `fs.chunks` collections
* File metadata is stored in your MongoDB database
* Diary entries store references to media Object IDs

---

## Dependencies

Example `requirements.txt` typically contains:

```
Flask
pymongo
flask_pymongo
python-dotenv
gridfs
werkzeug
```

(This aligns with a Flask + MongoDB project setup.)

---

## Notes & Tips

* Use modern browsers for media playback
* Ensure MongoDB is running and reachable before starting Flask
* If uploading large files, adjust Flask upload limits

---

## Next Steps (Optional Enhancements)

* Add user accounts and authentication
* Implement search by tags or date range
* Add pagination for browsing entries
* Migrate to a full API + SPA frontend
* Add cloud storage options (S3 or similar)

---

## License

This repository currently does not list a license. You may consider adding one if you intend to share or open-source it.

---
