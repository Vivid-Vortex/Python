def merge_dictionaries(dict_list):
    # Dictionary to store the merged results
    merged_dict = {}

    for d in dict_list:
        id = d['id']

        # Initialize the merged dictionary for this id if not already present
        if id not in merged_dict:
            merged_dict[id] = {}

        for key, value in d.items():
            if value is not None:
                if '.' in key:
                    outer_key, inner_key = key.split('.')
                    if outer_key not in merged_dict[id]:
                        merged_dict[id][outer_key] = []
                    merged_dict[id][outer_key].append({inner_key: value})
                else:
                    if key not in merged_dict[id]:
                        merged_dict[id][key] = value

    # Remove any duplicates in nested lists
    for id in merged_dict:
        for key in merged_dict[id]:
            if isinstance(merged_dict[id][key], list):
                seen = set()
                unique_list = []
                for item in merged_dict[id][key]:
                    t_item = tuple(item.items())
                    if t_item not in seen:
                        seen.add(t_item)
                        unique_list.append(item)
                merged_dict[id][key] = unique_list

    return list(merged_dict.values())

# Example usage
# dict_list = [
#     {'id': 1, 'name': 'morpheus', 'job': 'leader', 'address.city': 'Delhi'},
#     {'id': 1, 'name': None, 'job': None, 'address.city': 'Bombay'},
#     {'id': 2, 'name': 'dorpheus', 'job': 'follower', 'address.city': None}
# ]
dict_list = [
    {'id': 1, 'name': 'morpheus', 'job': 'leader', 'address.city': 'Delhi', 'contact.phone' : '9206918946', 'contact.email': 'deepak.kumar@gmail.com'},
    {'id': 1, 'name': None, 'job': None, 'address.city': 'Bombay', 'contact.phone' : '9206918947', 'contact.email': 'kumar.deepak@gmail.com'},
    {'id': 2, 'name': 'dorpheus', 'job': 'follower', 'address.city': None}
]
merged_result = merge_dictionaries(dict_list)
print(merged_result)
