import json

from pystache import render

def render_template(my_dict, template):
    rendered = render(template, my_dict)
    return rendered


def clean_json(json_str):
    # Parse JSON string into a dictionary
    data = json.loads(json_str)

    # Convert dictionary back to JSON string without unnecessary commas
    cleaned_json = json.dumps(json_str, separators=(',', ':'), indent=2)

    return cleaned_json

# Example usage:
my_dict = {
    "title": "Sample Shopping List",
    "description": "A list of items with prices",
    "items": [
        {"name": "Apple", "quantity": 5, "price": 2.5},
        {"name": "Banana", "quantity": 3, "price": 1.2}
    ],
    "tags": ["fruit", "grocery"]
}

mustache_template = '''
{
  "title": "{{title}}",
  "description": "{{description}}",
  "items": [
    {{#items}}
    {
      "name": "{{name}}",
      "quantity": {{quantity}},
      "price": {{price}}
    },
    {{/items}}
  ],
  "tags": [
    {{#tags}}
    "{{.}}",
    {{/tags}}
  ]
}
'''

rendered_json = render_template(my_dict, mustache_template)
rendered_json= clean_json(rendered_json)
print(rendered_json)
