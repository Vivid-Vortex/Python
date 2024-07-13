import json


def process_dictionary(my_dict):
    processed_dict = []

    for entry in my_dict:
        temp_dict = {}
        for key, value in entry.items():
            if isinstance(value, list):
                if all(isinstance(item, dict) for item in value):  # Check if all items in the list are dictionaries
                    temp_list = []
                    for item in value:
                        temp_item = {}
                        for k, v in item.items():
                            if isinstance(v, (str, int, float, bool)):
                                temp_item[k] = v
                        temp_list.append(temp_item)
                    temp_dict[key] = temp_list
            elif isinstance(value, dict):
                temp_sub_dict = {}
                for k, v in value.items():
                    if isinstance(v, (str, int, float, bool)):
                        temp_sub_dict[k] = v
                temp_dict[key] = temp_sub_dict
            else:
                temp_dict[key] = value

        processed_dict.append(temp_dict)

    return {"my_dict": processed_dict}

# Example usage
my_dict = [
    {'id': 1, 'name': 'morpheus', 'job': 'leader',
     'address': [{'city': 'Delhi', 'state': 'Union Territory'}, {'city': 'Bombay', 'state': 'Maharashtra'}],
     'contact': [{'phone': '9206918946', 'email': 'deepak.kumar@gmail.com'},
                 {'phone': '9206918947', 'email': 'kumar.deepak@gmail.com'}]},
    {'id': 2, 'name': 'dorpheus', 'job': 'follower'}
]

expected_dict = process_dictionary(my_dict)
print(json.dumps(expected_dict, indent=4))
