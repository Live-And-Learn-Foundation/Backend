import os
from dotenv import load_dotenv
import pandas as pd
from openai import OpenAI

load_dotenv("keys.env")

keys_string = os.getenv('OPENAI_KEYS')

openai_api_keys_from_env = keys_string.split(',') if keys_string else []

print(openai_api_keys_from_env)

# Đặt đường dẫn thư mục hiện tại là thư mục chứa file chương trình
current_dir = os.path.dirname(os.path.abspath(__file__))

# Tạo đường dẫn tuyệt đối cho các file CSV
data_1_path = os.path.join(current_dir, 'understand_rdf_system_for_sparql_class.csv')
data_2_path = os.path.join(current_dir, 'understand_rdf_system_for_sparql_object_properties.csv')
data_3_path = os.path.join(current_dir, 'understand_rdf_system_for_sparql_data_properties.csv')
triples_path = os.path.join(current_dir, 'Triples.txt')

with open(triples_path, 'r') as file:
    text = file.read()
    triples = [msg.strip() for msg in text.split('\n')]

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
message = "You are a languages specialist and an expert in converting natural language queries (NLQ) into SPARQL queries for university search.\n"

message += "Given the following classes in my RDF graph design: \n"
for Properties_Name, Description in data_1.values:
    message += f"Class: {Properties_Name} => Class Description: {Description}\n"

message += "Given the following object properties in my RDF graph design: \n"
for Properties_Name, Description in data_2.values:
    message += f"Object Properties: {Properties_Name} => Object Properties Description: {Description}\n"

message += "Given the following data properties in my RDF graph design: \n"
for Properties_Name, Description in data_3.values:
    message += f"Data Properties: {Properties_Name} => Data Properties Description: {Description}\n"

# rule_string = """Now, here is the rules you must follow when converting an NLQ to Sparql query:\n
#     First of all, convert user's query into English language, especially Vietnamese.\n
#     Acronyms must be expanded.\n
#     EVERY SINGLE OBJECT MUST HAVE NAME OR TITLE depending on their class and their NAME OR TITLE CANNOT BE OPTIONAL.\n
#     ONLY if the class object is Person or its sub classes (Student, Teacher,... ), BIND the class object's first name and last name together into full name instead of returning these two data properties separated in the answer.\n
#     Class Person and its subclasses (Student, Teacher, ...) CANNOT have ```:hasName``` or ```:hasTitle``` properties and must BIND from the ```:hasFirstName``` and ```:hasLastName``` properties into ```:fullName``` property.\n
#     Class Person and its subclasses (Student, Teacher, ...) MUST BE CHECK to have ```:hasFirstName``` and ```:hasLastName``` properties before BIND\n
#     Most data properties of the object HAVE TO BE OPTIONAL EXCEPT their NAME OR TITLE.\n
#     The class of main object of the user's question has to be SELECTED directly in the query result, in addition to its properties.\n
#     Conduct substring matching when the user is referring to a data property's value of a certain class by Including the FILTER function for any Data Properties searched in the query.\n
#     When performing substring matching, first extract the relevant named entities from the user's input before conducting the matching process. This ensures that specific entities are accurately targeted when locating data properties in the query.\n
#     Convert substring matching to English language before matching.\n
#     ONLY provide the query without Prefix and HAVE TO USE THE CORRECT SYNTAX.\n
#     Only return Sparql query without Prefix without explanation, and have to use the correct syntax.\n
#     """

rule_string = '''Now, here are the rules you must follow when converting an NLQ to SPARQL query:
    - Convert user's query into English language, especially Vietnamese.
    - Expand acronyms.
    - Every single object must have a name or title depending on their class, and their name or title cannot be optional.
    - If the class object is Person or its subclasses (Student, Teacher, etc.), bind the class object's first name and last name together into full name instead of returning these two data properties separately.
    - Class Person and its subclasses (Student, Teacher, etc.) cannot have ':hasName' or ':hasTitle' properties and must bind from the ':hasFirstName' and ':hasLastName' properties into ':fullName' property.
    - Class Person and its subclasses (Student, Teacher, etc.) must be checked to have ':hasFirstName' and ':hasLastName' properties before binding.
    - Most data properties of the object have to be optional except their name or title.
    - The class of the main object of the user's question has to be selected directly in the query result, in addition to its properties.
    - Conduct substring matching when the user is referring to a data property's value of a certain class by including the FILTER function for any data properties searched in the query.
    - When performing substring matching, first extract the relevant named entities from the user's input before conducting the matching process. This ensures that specific entities are accurately targeted when locating data properties in the query.
    - Convert substring matching to English language before matching.
    - Only filter for single words in any case, excluding compound nouns.
    - Expand abbreviations by providing their full forms.
    - SELECT statement must always include the name or title data properties of the main object in the query result.
    - Object variables must be consistently referenced throughout the query to avoid syntax errors (e.g., use ?department when binding `:hasDescription`).
    - When the user's query is in Vietnamese, translate relevant keywords (like "khóa học") to English ("course") and do not use these translations in FILTER functions.
    - Only provide the query without prefix and have to use the correct syntax.
    - Only return SPARQL query without prefix without explanation, and have to use the correct syntax.
    '''

message += rule_string

for triple in triples:
    base_messages.append({
        "role": "system",
        "content": f"Data: {triple}",
    })

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
            with open("Errors.txt", "a") as file:
                file.write('\n--------------------\n')
                file.write(user_query)
                file.write('\n\n')
                file.write(f"Error with {current_key}: {e}.")
                file.write('\n--------------------\n')
            
            current_key_index += 1
            if current_key_index >= keys_length:
                print("Max keys reached: {}".format(keys_length))
                success = True
                return {"message": "Max keys reached: {}".format(keys_length)}
