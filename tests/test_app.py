from fastapi.testclient import TestClient

import routes.note as note_routes
from main import app


class FakeCollection:
    def __init__(self):
        self.items = []

    def find(self, _query):
        class Cursor:
            def __init__(self, items):
                self.items = items

            def sort(self, *_args):
                return self

            def __iter__(self):
                return iter(self.items)

        return Cursor(self.items)

    def insert_one(self, item):
        item = {"_id": len(self.items) + 1, **item}
        self.items.append(item)


def test_health():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_note(monkeypatch):
    fake = FakeCollection()
    monkeypatch.setattr(note_routes, "notes_collection", fake)

    client = TestClient(app)

    response = client.post(
        "/",
        data={"title": "Test note", "desc": "Hello", "important": "on"},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/"

    response = client.get("/")
    assert response.status_code == 200
    assert "Test note" in response.text
    assert "Hello" in response.text
