import requests
import dotenv
import os
import pandas as pd
from openai import OpenAI

openai_api_key_from_env = "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"

# Đặt đường dẫn thư mục hiện tại là thư mục chứa file chương trình
current_dir = os.path.dirname(os.path.abspath(__file__))

# Tạo đường dẫn tuyệt đối cho các file CSV
data_1_path = os.path.join(current_dir, 'understand_rdf_system_for_sparql_class.csv')
data_2_path = os.path.join(current_dir, 'understand_rdf_system_for_sparql_object_properties.csv')
data_3_path = os.path.join(current_dir, 'understand_rdf_system_for_sparql_data_properties.csv')

# Đọc file CSV
data_1 = pd.read_csv(data_1_path)
data_2 = pd.read_csv(data_2_path)
data_3 = pd.read_csv(data_3_path)

data_1 = data_1.dropna()
data_2 = data_2.dropna()
data_3 = data_3.dropna()

endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"
# print("Hi3")

client = OpenAI(
    base_url=endpoint,
    api_key=openai_api_key_from_env,
)

base_messages = []
base_messages.append({
    "role": "system",
    "content": "You are an expert in converting natural language queries (NLQ) into SPARQL queries for university search.",
})
base_messages.append({
    "role": "system",
    "content": "Given the following classes in my RDF graph design: ",
})
for Properties_Name, Description in data_1.values:
    base_messages.append({
        "role": "system",
        "content": f"Class: {Properties_Name}\nClass Description: {Description}\n"
    })
base_messages.append({
    "role": "system",
    "content": "And given the following object properties in my RDF graph design: ",
})
for Properties_Name, Description in data_2.values:
    base_messages.append({
        "role": "system",
        "content": f"Object Properties: {Properties_Name}\nObject Properties Description: {Description}\n"
    })
base_messages.append({
    "role": "system",
    "content": "And given the following data properties in my RDF graph design: ",
})
for Properties_Name, Description in data_3.values:
    base_messages.append({
        "role": "system",
        "content": f"Data Properties: {Properties_Name}\nData Properties Description: {Description}\n"
    })


def convert_user_query(user_query):
    # print("Hi2")
    # Write content to a file
    # with open("test.txt", "a") as file:
    #     file.write("HI 2")
    messages = base_messages + [{
    "role": "user",
    "content": f"ALL data properties of the object should be OPTIONAL. Ensure that the class of main object of the user's question is selected directly in the query result, in addition to its properties. For each class object being returned in the answer, its name (or title) must also be returned. Also, if the class object is Person or its sub classes, BIND its first name and last name together instead of returning these two data properties separated in the answer. Lastly, ONLY provide the query without Prefix and use correct syntax, including the FILTER function for any Data Properties that require substring matching. Now, Convert the following NLQ into a SPARQL query : ```{user_query}```",
    }]

    response = client.chat.completions.create(
    messages=messages,
    temperature=0.3,
    top_p=1.0,
    max_tokens=4096,
    model=model_name
    )
    # with open("test.txt", "a") as file:
    #     file.write("HI 3")
    # print(response.choices[0].message.content)
    return response.choices[0].message.content
