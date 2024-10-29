import requests
import dotenv
import os
import re
from .llm_sparql_generate import convert_user_query

dotenv.load_dotenv()  # Load environment variables from .env file
HOST_ADDRESS = os.getenv("HOST")


def generate_answer(user_query):
    try:
        # print(user_query)
        sparql_query = convert_user_query(user_query)
        # print(sparql_query)
        # with open("test.txt", "a") as file:
        #     file.write(sparql_query)
        # Xử lý chuỗi bằng regex để lấy câu truy vấn SPARQL đúng định dạng
        sparql_query_cleaned = re.sub(r"```(?:sparql)?\n?", "", sparql_query)  # Bỏ các đoạn ```sparql và ``` ở cuối
        sparql_query_cleaned = re.sub(r"\\n", "\n", sparql_query_cleaned)  # Thay thế các ký tự \n bằng newline thật
        # Thêm prefix vào đầu câu truy vấn
        prefix = "PREFIX : <http://www.semanticweb.org/nguye/ontologies/2024/8/university#>\n"
        sparql_query_final = prefix + sparql_query_cleaned.strip()
        # print(sparql_query_final)
        with open("test.txt", "a") as file:
            file.write(sparql_query_final)
        # return sparql_query

        response = requests.post(
            f"http://host.docker.internal:9090/sparql",
            data={"query": sparql_query_final}  # Form data with key "query"
        )
        response.raise_for_status()  # Raise an error for HTTP error responses
        return response.json()  # Parse and return JSON data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

#         sparql_query = """PREFIX : <http://www.semanticweb.org/nguye/ontologies/2024/8/university#>
# SELECT ?courseName ?instructorName ?studentName
# WHERE {
#   ?course a :Course .
#   ?course :hasName ?courseName .

#   OPTIONAL {
#     ?course :hasInstructor ?instructor .
#     ?instructor a :Student .
#     ?instructor :hasFirstName ?instructorFirstName .
#     ?instructor :hasLastName ?instructorLastName .
#     BIND(CONCAT(?instructorFirstName, " ", ?instructorLastName) AS ?instructorName)
#   }

#   OPTIONAL {
#     ?course :isStudiedBy ?student .
#     ?student a :Student .
#     ?student :hasFirstName ?studentFirstName .
#     ?student :hasLastName ?studentLastName .
#     BIND(CONCAT(?studentFirstName, " ", ?studentLastName) AS ?studentName)
#   }
# }
# LIMIT 5
# """
