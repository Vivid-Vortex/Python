import json

import pystache

from PythonInit.GetRelativePathForProjectFiles import get_data_path


def render_template(my_dict, template_file):
    """
    Renders a Mustache template with the given dictionary.

    Args:
    - my_dict (dict): The dictionary with data to render the template.
    - template_file (str): The path to the Mustache template file.

    Returns:
    - dict: The rendered template as a JSON object, or None if there is an error.
    """
    # def add_comma(context, _):
    #     """Helper function to add commas between address objects."""
    #     for i in range(len(context['address'])):
    #         context['address'][i]['comma'] = (i != len(context['address']) - 1)
    #     return context

    with open(template_file, 'r') as file:
        template = file.read()

    # my_dict = add_comma(my_dict, None)
    renderer = pystache.Renderer()
    rendered = renderer.render(template, my_dict)

    try:
        rendered_dict = json.loads(rendered)
        return rendered_dict
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Rendered content:\n{rendered}")
        return None

def add_commas(data):
    for key, value in data.items():
        if isinstance(value, list):
            for index, item in enumerate(value):
                if index < len(value) - 1:
                    item['isLast'] = False
                else:
                    item['isLast'] = True
    return data

# Example usage
# my_dict = {
#     "id": 100,
#     "name": "Deepak",
#     "address": [
#         {"city": "Delhi"},
#         {"city": "Bombay"}
#     ]
# }

my_dict = { "id": 1, "name": "morpheus", "job": "leader", "address1": [ { "city": "Delhi", "state": "Union Territory" }, { "city": "Bombay", "state": "Maharashtra" } ], "contact": [ { "phone": "9206918946", "email": "deepak.kumar@gmail.com" }, { "phone": "9206918947", "email": "kumar.deepak@gmail.com" } ] }
data_file_to_access = "sample_mustache_file_to_parse.mustache"
relative_path_from_current_file = "resources"
template_file = get_data_path(data_file_to_access, relative_path_from_current_file)

my_dict = add_commas(my_dict)
print(my_dict)
rendered_output = render_template(my_dict, template_file)
print(rendered_output)
