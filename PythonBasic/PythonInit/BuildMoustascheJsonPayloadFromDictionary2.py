import pystache
import json

from PythonInit.GetRelativePathForProjectFiles import get_data_path


import json
import pystache

def render_template(my_dict, template_file):
    def add_commas(data_list):
        for i in range(len(data_list)):
            if i < len(data_list) - 1:
                data_list[i]["comma"] = True
            else:
                data_list[i]["comma"] = False
        return data_list

    for key, value in my_dict.items():
        if isinstance(value, list):
            my_dict[key] = add_commas(value)

    with open(template_file, 'r') as file:
        template = file.read()

    renderer = pystache.Renderer()
    rendered = renderer.render(template, my_dict)

    try:
        rendered_dict = json.loads(rendered)
        return rendered_dict
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Rendered content:\n{rendered}")
        return None


# Example usage
# my_dict = {
#     "id": 100,
#     "name": "Deepak",
#     "address": [
#         {"city": "Delhi"},
#         {"city": "Bombay"}
#     ]
# }

my_dict = { "id": 1, "name": "morpheus", "job": "leader", "address": [ { "city": "Delhi", "state": "Union Territory" }, { "city": "Bombay", "state": "Maharashtra" } ], "contact": [ { "phone": "9206918946", "email": "deepak.kumar@gmail.com" }, { "phone": "9206918947", "email": "kumar.deepak@gmail.com" } ] }

# template_file = 'template.mustache'
template_file = get_data_path("sample_mustache_file_to_parse.mustache", "resources")
rendered_output = render_template(my_dict, template_file)
print(rendered_output)
