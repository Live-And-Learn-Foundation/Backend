from ..services.sparql_generate_json_answer import generate_answer
from ..services.convert_json_data import convert_sparql_output
class SearchController:
    def __init__(self):
        pass

    def get(self, query: str = ""):
        if query:
            #Todo: get LLM interfere and using Sparql generated from LLM to call request to sparql endpoint and then return Data (JSON format).
            return convert_sparql_output(generate_answer(query))
        else:
            return {"message": "No query provided"}
