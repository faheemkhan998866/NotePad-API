"""Backward-compatible entry point.

Run the application with:
    uvicorn main:app --reload
"""

from main import app

__all__ = ["app"]
