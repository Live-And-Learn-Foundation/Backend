import requests
import dotenv
import os
import pandas as pd
from openai import OpenAI

openai_api_keys_from_env = [
    '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', 
    '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', 
    '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',
    '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',
    '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',
    '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',
    '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',
    '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',
    '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',
    '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',
    ]

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
model_name = "gpt-4o"

base_messages = []
message = "You are an expert in converting natural language queries (NLQ) into SPARQL queries for university search.\n"

message += "Given the following classes in my RDF graph design: \n"
for Properties_Name, Description in data_1.values:
    message += f"Class: {Properties_Name} => Class Description: {Description}\n"

message += "Given the following object properties in my RDF graph design: \n"
for Properties_Name, Description in data_2.values:
    message += f"Object Properties: {Properties_Name} => Object Properties Description: {Description}\n"

message += "Given the following data properties in my RDF graph design: \n"
for Properties_Name, Description in data_3.values:
    message += f"Data Properties: {Properties_Name} => Data Properties Description: {Description}\n"

rule_string = """Now, here is the rule you must follow when converting an NLQ to Sparql query:\n
    EVERY SINGLE OBJECT MUST HAVE NAME OR TITLE depending on their class and their NAME OR TITLE CANNOT BE OPTIONAL.\n
    ONLY if the class object is Person or its sub classes (Student, Teacher,... ), BIND the class object's first name and last name together into full name instead of returning these two data properties separated in the answer.\n
    Class Person and its subclasses (Student, Teacher, ...) CANNOT have ```:hasName``` or ```:hasTitle``` properties and must BIND from the ```:hasFirstName``` and ```:hasLastName``` properties into ```:fullName``` property.\n
    Class Person and its subclasses (Student, Teacher, ...) MUST BE CHECK to have ```:hasFirstName``` and ```:hasLastName``` properties before BIND\n
    Most data properties of the object HAVE TO BE OPTIONAL EXCEPT their NAME OR TITLE.\n
    Ensure that the class of main object of the user's question is SELECTED directly in the query result, in addition to its properties.\n
    Conduct subtring matching by Including the FILTER function for any Data Properties searched in the query.\n
    ONLY provide the query without Prefix and HAVE TO USE THE CORRECT SYNTAX\n
    """

message += rule_string

base_messages.append({
    "role": "system",
    "content": message,
})
# For each class object being returned in the answer, the class object's name or title must also be returned depending on the class object's class.\n
base_messages.append({
    "role": "user",
    "content": rule_string,
})

def convert_user_query(user_query):
    keys_length = len(openai_api_keys_from_env)
    current_key_index = 0
    success = False
    while not success: 
        try:
            current_key = openai_api_keys_from_env[current_key_index]
            client = OpenAI(
                base_url=endpoint,
                api_key=current_key,
            )

            messages = base_messages + [{
                "role": "user",
                # "content": f"All objects MUST HAVE NAME OR TITLE depending on their class and CANNOT BE OPTIONAL. \n ONLY if the class object is Person or its sub classes (Student, Teacher,... ), BIND the class object's first name and last name together into full name instead of returning these two data properties separated in the answer. \n Class Person and its subclasses (Student, Teacher, ...) CANNOT have ```:hasName``` or ```:hasTitle``` properties and must BIND from the ```:hasFirstName``` and ```:hasLastName``` properties into ```:fullName``` property. \n Most data properties of the object should be OPTIONAL. \n Ensure that the class of main object of the user's question is selected directly in the query result, in addition to its properties. \n For each class object being returned in the answer, the class object's name or title must also be returned depending on the class object's class. \n Also, ONLY if the class object is Person or its sub classes (Student, Teacher,... ), BIND the class object's first name and last name together into full name instead of returning these two data properties separated in the answer. \n Lastly, ONLY provide the query without Prefix and use correct syntax, including the FILTER function for any Data Properties that require substring matching. \n Now, Convert the following NLQ into a SPARQL query : \n```\n{user_query}\n```\n",
                "content": f"Now, Convert the following NLQ into a SPARQL query : \n```\n{user_query}\n```"
            }]

            response = client.chat.completions.create(
                messages=messages,
                temperature=0.3,
                top_p=1.0,
                max_tokens=4096,
                model=model_name
            )

            success = True
            return response.choices[0].message.content
        except Exception as e:
            # Print the error and continue to the next key
            print(f"Error with {current_key}: {e}. Start using new key.")
            current_key_index += 1
            if current_key_index >= keys_length:
                print("Max keys reached: {}".format(keys_length))
                success = True
                return {"message": "Max keys reached: {}".format(keys_length)}
