def add_commas(data, is_outermost=True):
    def process_dict(d):
        for key, value in d.items():
            if isinstance(value, list):
                process_list(value)
            elif isinstance(value, dict):
                process_dict(value)

    def process_list(lst):
        for index, item in enumerate(lst):
            if index < len(lst) - 1:
                item['isLast'] = False
            else:
                item['isLast'] = True
            if isinstance(item, dict):
                process_dict(item)

    if isinstance(data, list):
        process_list(data)
    elif isinstance(data, dict):
        process_dict(data)
        if not is_outermost:
            data['isLast'] = True

    return data

# Example usage
data_list = [{
    "id": 1,
    "name": "morpheus",
    "job": "leader",
    "address1": [
        {"city": "Delhi", "state": "Union Territory"},
        {"city": "Bombay", "state": "Maharashtra"}
    ],
    "contact": [
        {"phone": "9206918946", "email": "deepak.kumar@gmail.com"},
        {"phone": "9206918947", "email": "kumar.deepak@gmail.com"}
    ]
}]

data_dict = {
    "id": 1,
    "name": "morpheus",
    "job": "leader",
    "address1": [
        {"city": "Delhi", "state": "Union Territory"},
        {"city": "Bombay", "state": "Maharashtra"}
    ],
    "contact": [
        {"phone": "9206918946", "email": "deepak.kumar@gmail.com"},
        {"phone": "9206918947", "email": "kumar.deepak@gmail.com"}
    ]
}

nested_data_dict = {
    "request": [{
        "id": 1,
        "name": "morpheus",
        "job": "leader",
        "address1": [
            {"city": "Delhi", "state": "Union Territory"},
            {"city": "Bombay", "state": "Maharashtra"}
        ],
        "contact": [
            {"phone": "9206918946", "email": "deepak.kumar@gmail.com"},
            {"phone": "9206918947", "email": "kumar.deepak@gmail.com"}
        ]
    }]
}

print(add_commas(data_list))
print(add_commas(data_dict))
print(add_commas(nested_data_dict))
