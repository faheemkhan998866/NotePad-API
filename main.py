from fastapi import FastAPI
from fastapi.responses import JSONResponse

from config.db import check_database
from routes.note import note

app = FastAPI(
    title="iNotes API",
    description="FastAPI notes API using a local MongoDB Server.",
    version="1.1.0",
)

app.include_router(note)


@app.get("/health", tags=["Health"])
async def health():
    """Application and MongoDB health check."""
    database_ok = check_database()
    return JSONResponse(
        status_code=200 if database_ok else 503,
        content={
            "status": "ok" if database_ok else "error",
            "mongodb": "connected" if database_ok else "not connected",
        },
    )
