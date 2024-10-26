import re

# Hàm lấy Individual_type và Individual_id từ URI
def extract_individual_info(uri):
    match = re.search(r"#(\w+)_(\w+)", uri)
    if match:
        individual_type, individual_id = match.groups()
        return individual_type, individual_id
    return None, None

# Hàm chuyển đổi dữ liệu
def convert_sparql_output(sparql_output):
    converted_data = []
    for binding in sparql_output['results']['bindings']:
        entry = {
            "name": [],
            "additional_info": "",
            "url": []
        }
        
        additional_info_parts = []
        
        for key, value in binding.items():
            if value['type'] == 'uri':
                individual_type, individual_id = extract_individual_info(value['value'])
                if individual_type and individual_id:
                    # Thêm cả tên và url từ các URI
                    entry["name"].append(f"{individual_type} {individual_id}")
                    entry["url"].append(f"/{individual_type}/{individual_id}")
            else:
                # Ghép các phần dữ liệu khác thành additional_info
                key = re.sub(r'(?<!^)(?=[A-Z])', ' ', key).lower()
                additional_info_parts.append(f"{key}: {value['value']}")
        
        # Nối các phần của additional_info thành một chuỗi với dấu chấm phẩy
        entry["additional_info"] = ' ; '.join(additional_info_parts)
        converted_data.append(entry)
    
    return converted_data

# # Gọi hàm và in kết quả
# converted_output = convert_sparql_output(sparql_output)
# print(converted_output)


# # Dữ liệu đầu vào (SPARQL query output)
# sparql_output = {
#     "head": {
#         "vars": [
#             "teacher",
#             "teacher2",
#             "firstName",
#             "lastName",
#             "email",
#             "academicTitle",
#             "biography",
#             "degree"
#         ]
#     },
#     "results": {
#         "bindings": [
#             {
#                 "teacher": {
#                     "type": "uri",
#                     "value": "http://www.semanticweb.org/nguye/ontologies/2024/8/university#Person_9ebe9cf43b2f463bae612a8c1f1ef776"
#                 },
#                 "teacher2": { 
#                     "type": "uri",
#                     "value": "http://www.semanticweb.org/nguye/ontologies/2024/8/university#Person_9ebe9cf43b2f463bae612a8c1f1ef776"
#                 },
#                 "firstName": {
#                     "type": "literal",
#                     "value": "Teacher"
#                 },
#                 "lastName": {
#                     "type": "literal",
#                     "value": "Two"
#                 },
#                 "academicTitle": {
#                     "type": "literal",
#                     "value": "Software Engineer"
#                 },
#                 "biography": {
#                     "type": "literal",
#                     "value": "Passionate about developing innovative software solutions."
#                 },
#                 "degree": {
#                     "type": "literal",
#                     "value": "Bachelor of Science in Computer Science"
#                 }
#             },
#             {
#                 "teacher": {
#                     "type": "uri",
#                     "value": "http://www.semanticweb.org/nguye/ontologies/2024/8/university#Person_9ebe9cf43b2f463bae612a8c1f1ef777"
#                 },
#                 "firstName": {
#                     "type": "literal",
#                     "value": "Teacher"
#                 },
#                 "lastName": {
#                     "type": "literal",
#                     "value": "Three"
#                 },
#                 "academicTitle": {
#                     "type": "literal",
#                     "value": "Software Engineer"
#                 },
#                 "biography": {
#                     "type": "literal",
#                     "value": "Passionate about developing innovative software solutions."
#                 },
#                 "degree": {
#                     "type": "literal",
#                     "value": "Bachelor of Science in Computer Science"
#                 }
#             },
#             {
#                 "teacher": {
#                     "type": "uri",
#                     "value": "http://www.semanticweb.org/nguye/ontologies/2024/8/university#Person_9ebe9cf43b2f463bae612a8c1f1ef775"
#                 },
#                 "teacher2": { 
#                     "type": "uri",
#                     "value": "http://www.semanticweb.org/nguye/ontologies/2024/8/university#Person_9ebe9cf43b2f463bae612a8c1f1ef776"
#                 },
#                 "firstName": {
#                     "type": "literal",
#                     "value": "Teacher"
#                 },
#                 "lastName": {
#                     "type": "literal",
#                     "value": "One"
#                 },
#                 "academicTitle": {
#                     "type": "literal",
#                     "value": "Software Engineer"
#                 },
#                 "biography": {
#                     "type": "literal",
#                     "value": "Passionate about developing innovative software solutions."
#                 },
#                 "degree": {
#                     "type": "literal",
#                     "value": "Bachelor of Science in Computer Science"
#                 }
#             }
#         ]
#     }
# }
