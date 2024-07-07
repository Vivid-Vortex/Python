import json
from jsonpath_ng import parse

from PythonInit.BuildMoustascheJsonPayloadFromDictionary import build_structure_req_payload
from PythonInit.CallRestApis import make_request
from PythonInit.GetRelativePathForProjectFiles import get_data_path
from PythonInit.ReadExcel import get_sheet_data
from PythonInit.extract_value_from_json_path import extract_value_using_json_path


def combine_list_of_dict_to_single_dict(list_of_dicts):
    print("Input to comined dictionary function :", list_of_dicts)
    result_dict = {}
    for item in list_of_dicts:
        result_dict[item['RequestProperty']] = item['ResponseJsonPathExpression']
    return result_dict

# my_list = [{'RequestProperty': 'name', 'ResponseJsonPathExpression': 'data[0].first_name'}, {'RequestProperty': 'job', 'ResponseJsonPathExpression': 'data[0].last_name'}]
#
# print("", combine_list_of_dict_to_single_dict(my_list))

entity_list = ['tariff']

url = 'https://reqres.in/api/users'
headers = {'Content-Type': 'application/json'}

for entity in entity_list:
    file_path = get_data_path("test-data.xlsx", "resources")
    sheet_name = 'req-payload'
    req_payload_dict = get_sheet_data(file_path, sheet_name)

    for inputDict in req_payload_dict:
        template_file_file_path = get_data_path("sample_json_moustache_payload.json", "resources")
        req_payload = build_structure_req_payload(inputDict, template_file_file_path)
        print(req_payload)
        response = make_request(url, 'POST', headers=headers, json_data=req_payload)
        if response:
            print("POST response:", response)

# Invoke Build rate model Post Api
# Build rate model code will go here

# Invoke Get Rate Model
url = 'https://reqres.in/api/users'
# headers = ''
rate_model_response = make_request(url, 'GET', headers=headers)
if rate_model_response:
    print("GET response with pagination:", rate_model_response)

results = {"success": [], "failure": []}

for entity in entity_list:
    # List of dictionary. Each dictionary contains data from each row of excel
    file_path = get_data_path("test-data.xlsx", "resources")
    sheet_name = 'req-payload'
    req_payload_dict = get_sheet_data(file_path, sheet_name)
    print("Request payload sheet data: ", req_payload_dict)
    payload_sheet_name = 'json-path'
    print("Sheet------Data: ", get_sheet_data(file_path, payload_sheet_name))
    json_path_combined_dict = combine_list_of_dict_to_single_dict(get_sheet_data(file_path, payload_sheet_name))
    print("Json Path sheet data as dictionary list: ", json_path_combined_dict)

    for request_payload in req_payload_dict:
        count = 1
        print(request_payload)
        for key in json_path_combined_dict:
            expected = request_payload[key]
            assertion = json_path_combined_dict[key]
            actual = extract_value_using_json_path(rate_model_response, assertion)

            message = f"In Entity: '{entity}' and request payload row {count}, Expected value for '{key}' ({expected}) "
            if expected == actual:
                message += f"matches actual value ({actual})"
                results["success"].append(message)
            else:
                message += f"does not match actual value ({actual})"
                results["failure"].append(message)
        count += 1

print(len(results['failure']))