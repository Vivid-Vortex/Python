import json

import pystache

from PythonInit.GetRelativePathForProjectFiles import get_data_path


def build_structure_req_payload(my_dict, template_file_path):
    with open(template_file_path, 'r') as template_file:
        template = template_file.read()

    template = str(template)

    # Render the template with values from my_dict
    rendered_json = pystache.render(template, my_dict)

    # Convert the rendered JSON string to a dictionary and back to a JSON string
    try:
        rendered_dict = json.loads(rendered_json)
        return rendered_dict
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


# my_dict = {"name": "morpheus", "job": "leader"}
# tempfile_file_path = get_data_path("sample_json_moustache_payload.json", "resources")
# req_payload = build_structure_req_payload(my_dict, tempfile_file_path)

