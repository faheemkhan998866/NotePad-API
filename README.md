# iNotes — FastAPI + Local MongoDB Server

A small notes application built with FastAPI, Jinja2, Bootstrap, and **MongoDB Community Server running locally**.

## Important

This version does **not** use MongoDB Atlas and does **not** require MongoDB Compass.

You only need:
- Python 3.10+
- MongoDB Community Server
- This project

MongoDB Compass is only a graphical database viewer. It is optional.

## 1. Install MongoDB Community Server

Install MongoDB Community Server for your operating system and make sure the MongoDB service is running.

### Windows

If MongoDB was installed as a Windows service:

```powershell
net start MongoDB
```

To check the service:

```powershell
Get-Service MongoDB
```

If you installed MongoDB without a service, start `mongod` manually using your MongoDB `bin` directory.

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

## 3. Install Python packages

```bash
pip install -r requirements.txt
```

## 4. Configure local MongoDB

Copy `.env.example` to `.env`.

Use:

```env
MONGO_URI=mongodb://127.0.0.1:27017
MONGO_DB_NAME=inotes
```

There is no Atlas connection string in this version.

## 5. Start the API

From the project folder:

```bash
uvicorn main:app --reload
```

Open:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/health

## 6. What runs where?

```text
Your browser
     |
     v
FastAPI (127.0.0.1:8000)
     |
     v
MongoDB Server (127.0.0.1:27017)
```

MongoDB Compass is not part of this connection.

## Troubleshooting

If `/health` returns:

```json
{"status":"error","mongodb":"not connected"}
```

make sure the MongoDB Server service is running and listening on port `27017`.

The database `inotes` and collection `notes` are created by MongoDB when the application first writes a note.

## Security

Do not put MongoDB credentials in source code. For this local-only version, the default connection has no username/password because it connects to your local MongoDB Server.
