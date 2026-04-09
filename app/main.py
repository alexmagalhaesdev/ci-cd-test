from typing import Annotated

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="CI/CD Test API")


class HealthResponse(BaseModel):
    status: str


class Item(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=100)]
    quantity: Annotated[int, Field(ge=1, le=1000)]


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.post("/items", response_model=Item)
def create_item(item: Item) -> Item:
    return item

