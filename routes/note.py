from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pymongo.errors import PyMongoError

from config.db import notes_collection

note = APIRouter()
templates = Jinja2Templates(directory="templates")


def get_notes() -> list[dict]:
    """Read notes from MongoDB and convert ObjectId to strings."""
    try:
        docs = notes_collection.find({}).sort("_id", -1)
        return [
            {
                "id": str(doc["_id"]),
                "title": doc.get("title", ""),
                "desc": doc.get("desc", ""),
                "important": bool(doc.get("important", False)),
            }
            for doc in docs
        ]
    except PyMongoError as exc:
        raise HTTPException(
            status_code=503,
            detail="Database is unavailable. Check MONGO_URI and MongoDB access.",
        ) from exc


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"newDocs": get_notes()},
    )


@note.post("/", response_class=RedirectResponse, status_code=303)
async def create_item(request: Request):
    form = await request.form()
    title = str(form.get("title", "")).strip()
    desc = str(form.get("desc", "")).strip()
    important = form.get("important") == "on"

    if not title:
        raise HTTPException(status_code=400, detail="Title is required.")

    try:
        notes_collection.insert_one(
            {
                "title": title,
                "desc": desc,
                "important": important,
            }
        )
    except PyMongoError as exc:
        raise HTTPException(
            status_code=503,
            detail="Database is unavailable. Check MONGO_URI and MongoDB access.",
        ) from exc

    return RedirectResponse(url="/", status_code=303)
