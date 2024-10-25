from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

# Sample in-memory data
items_db = [
    {"id": 1, "name": "Laptop", "description": "A portable computer"},
    {"id": 2, "name": "Mouse", "description": "A wireless mouse"},
    {"id": 3, "name": "Keyboard", "description": "A mechanical keyboard"},
    {"id": 4, "name": "Monitor", "description": "A 4K monitor"},
]

@app.get("/search/", response_model=List[dict])
async def search_items(q: Optional[str] = Query(None, min_length=2, title="Search query", description="The term to search for in items' names")):
    # Perform a case-insensitive search on item names
    results = [item for item in items_db if q.lower() in item["name"].lower()] if q else items_db
    return results
