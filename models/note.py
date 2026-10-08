from pydantic import BaseModel, Field


class Note(BaseModel):
    title: str = Field(min_length=1)
    desc: str = ""
    important: bool = False
