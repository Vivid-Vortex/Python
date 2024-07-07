import json
from jsonpath_ng import parse


def extract_value_using_json_path(json_data, jsonpath_expr_str):
    # Convert to string if json_data is not already a string
    if not isinstance(json_data, str):
        json_data = json.dumps(json_data)

    # Parse JSON string into Python dictionary
    data_dict = json.loads(json_data)

    # JSONPath query
    jsonpath_expr = parse(jsonpath_expr_str)

    # Execute the query against the data_dict
    matches = [match.value for match in jsonpath_expr.find(data_dict)]

    # Return the first match (assuming single result)
    if matches:
        return matches[0]
    else:
        return None  # Return None if no match found


# Code Testing
# json_data = '''
# {
#     "page": 1,
#     "per_page": 6,
#     "total": 12,
#     "total_pages": 2,
#     "data": [
#         {
#             "id": 1,
#             "email": "george.bluth@reqres.in",
#             "first_name": "George",
#             "last_name": "Bluth",
#             "avatar": "https://reqres.in/img/faces/1-image.jpg"
#         },
#         {
#             "id": 2,
#             "email": "janet.weaver@reqres.in",
#             "first_name": "Janet",
#             "last_name": "Weaver",
#             "avatar": "https://reqres.in/img/faces/2-image.jpg"
#         }
#     ]
# }
# '''
#
# # Example usage
# jsonpath_expr_str = '$.data[0].first_name'
# first_name = extract_value_using_json_path(json_data, jsonpath_expr_str)
# print("First Name (using JSONPath):", first_name)
