class SearchController:
    def __init__(self):
        pass

    def get(self, query: str = ""):
        if query:
            return {"message": f"Search results for '{query}'"}
        else:
            return {"message": "No query provided"}
