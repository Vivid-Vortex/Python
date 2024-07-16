import json


def construct_json_from_paths(data):
    def set_nested_item(data_dict, keys, value):
        for key in keys[:-1]:
            if key.isdigit():
                key = int(key)
                if isinstance(data_dict, dict):
                    if key not in data_dict:
                        data_dict[key] = {}
                    data_dict = data_dict[key]
                elif isinstance(data_dict, list):
                    while len(data_dict) <= key:
                        data_dict.append({})
                    data_dict = data_dict[key]
            else:
                if isinstance(data_dict, dict):
                    data_dict = data_dict.setdefault(key, {})
                elif isinstance(data_dict, list):
                    data_dict = data_dict[int(key)]

        last_key = keys[-1]
        if last_key.isdigit():
            last_key = int(last_key)
            if isinstance(data_dict, dict):
                while len(data_dict) <= last_key:
                    data_dict[last_key] = {}
            elif isinstance(data_dict, list):
                while len(data_dict) <= last_key:
                    data_dict.append(None)
            data_dict[last_key] = value
        else:
            data_dict[last_key] = value

    def parse_key(key):
        # This function splits the key by dots and converts array indices to int
        parts = []
        temp = ""
        in_brackets = False
        for char in key:
            if char == '[':
                if temp:
                    parts.append(temp)
                temp = ""
                in_brackets = True
            elif char == ']':
                if temp:
                    parts.append(temp)
                temp = ""
                in_brackets = False
            elif char == '.' and not in_brackets:
                if temp:
                    parts.append(temp)
                temp = ""
            else:
                temp += char
        if temp:
            parts.append(temp)
        return parts

    request_json = {}
    for path, value in data['requestJsonPaths'].items():
        keys = parse_key(path)
        set_nested_item(request_json, keys, value)

    return request_json


def convert_dict_to_list(obj):
    if isinstance(obj, dict):
        # If all keys are integers, convert to list
        if all(isinstance(key, int) for key in obj.keys()):
            obj = [convert_dict_to_list(obj[key]) for key in sorted(obj.keys())]
        else:
            for key in obj.keys():
                obj[key] = convert_dict_to_list(obj[key])
    elif isinstance(obj, list):
        obj = [convert_dict_to_list(elem) for elem in obj]
    return obj


# Example usage
data = {
    'id': 1,
    'requestJsonPaths': {
        'request[0].identity': 123,
        'request[0].name': 'John Doe',
        'request[0].address[0].city': 'New York',
        'request[0].address[0].state': 'NY',
        'request[0].contact[0].phone': '123-456-7890',
        'request[0].contact[0].email': 'johndoe@example.com',
        'request[0].address[1].city': 'Los Angeles',
        'request[0].address[1].state': 'CA',
        'request[0].contact[1].phone': '987-654-3210',
        'request[0].contact[1].email': 'johndoe2@example.com'
    }
}

constructed_json = construct_json_from_paths(data)
structured_json = convert_dict_to_list(constructed_json)

# Ensure the top-level object is an array
if 'request' in structured_json:
    structured_json = structured_json['request']

print(json.dumps(structured_json, indent=4))
