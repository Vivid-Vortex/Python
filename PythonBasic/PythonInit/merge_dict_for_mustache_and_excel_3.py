# import json
#
#
# def process_list(my_dict):
#     """
#     Processes a dictionary, handling list values by grouping their elements based on common keys.
#
#     Args:
#         my_dict: The input dictionary.
#
#     Returns:
#         The modified dictionary with processed list values.
#     """
#
#     def group_by_keys(data_list):
#         result = []
#         for item in data_list:
#             found = False
#             for group in result:
#                 if any(key in item for key in group):
#                     group.update(item)
#                     found = True
#                     break
#             if not found:
#                 result.append(dict(item))
#         return result
#
#     for key, value in my_dict.items():
#         if isinstance(value, list):
#             my_dict[key] = group_by_keys(value)
#
#     return my_dict
#
#
# # Example usage:
# my_dict = {
#     'id': 1,
#     'name': 'morpheus',
#     'job': 'leader',
#     'address': [{'city': 'Delhi'}, {'city': 'Bombay'}, {'lane': 'lane 1'}, {'lane': 'lane 2'}],
#     'contact': [{'phone': '9206918946'}, {'email': 'deepak.kumar@gmail.com'}, {'phone': '9206918947'},
#                 {'email': 'kumar.deepak@gmail.com'}]
# }
#
# processed_dict = process_list(my_dict)
# print(json.dumps(processed_dict, indent=2))
def count_unique_keys(data):
  if not data:
      return 0

  total_keys = 0
  for d in data:
      total_keys += len(d.keys())
  return total_keys

def is_dict_in_list(list_of_dicts, target_dict):
  for item in list_of_dicts:
    for key, value in target_dict.items():
      if key not in item or item[key] != value:
        break  # Key not found or value doesn't match
    else:
      return True  # All key-value pairs matched

  return False  # No match found


# Example usage:
# my_list = [{'city': 'Delhi', 'lane': 'lane 1'}]
# target_dict = {'lane': 'lane 1'}
# result = is_dict_in_list(my_list, target_dict)
# print(result)  # Output: True

def process_keys_with_list(lst):
    temp_list = []
    current_dict = {}
    temp_list_size = count_unique_keys(temp_list)
    target_list_size  = count_unique_keys(lst)
    while temp_list_size < target_list_size:
        for item in lst:
            key = next(iter(item))  # Get the key of the current item
            if key not in current_dict and len(temp_list) == 0:
                # is_dict_in_list(temp_list, current_dict)
                current_dict.update(item)
            elif key not in current_dict and not(is_dict_in_list(temp_list, item)):
                current_dict.update(item)
            # temp_list.append(current_dict)

        temp_list.append(current_dict)  # Append the last dictionary
        current_dict = {}
        temp_list_size = count_unique_keys(temp_list)
        target_list_size = count_unique_keys(lst)

    return temp_list


# address= [{'city': 'Delhi'}, {'city': 'Bombay'}, {'lane': 'lane 1'}, {'lane': 'lane 2'}]
# respone = process_keys_with_list(address)
# print(respone)

def process_dictionary(data):

  list_keys = []
  for item in data:
    for key, value in item.items():
      if isinstance(value, list):
          processed_list = process_keys_with_list(value)
          item[key] = processed_list
  return data

my_list = [{'id': 1, 'name': 'morpheus', 'job': 'leader', 'address': [{'city': 'Delhi'}, {'city': 'Bombay'}], 'contact': [{'phone': '9206918946'}, {'email': 'deepak.kumar@gmail.com'}, {'phone': '9206918947'}, {'email': 'kumar.deepak@gmail.com'}]}, {'id': 2, 'name': 'dorpheus', 'job': 'follower'}]

result = process_dictionary(my_list)
print(result)  # Output: ['address', 'contact']


