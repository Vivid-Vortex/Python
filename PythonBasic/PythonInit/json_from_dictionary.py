import json

my_dict = {
    "userName": "Deepak",
    "userId": 1000,
    "additionalInfo": {"city": "New York"}
}

# Create empty JSON string
json_string = "{"

# Loop through filtered keys and values
filtered_keys = ["userName", "userId"]  # Specify keys to include
for key, value in my_dict.items():
  if key in filtered_keys:
    # Use json.dumps for value serialization (if needed)
    if isinstance(value, (dict, list, int, float, str)):
      value_json = json.dumps(value)
    else:
      value_json = str(value)

    # Append key-value pair to the JSON string
    json_string += f"\"{key}\": {value_json},"

# Remove the trailing comma (if present)
json_string = json_string[:-1]

# Close the JSON structure
json_string += "}"

print(json_string)
