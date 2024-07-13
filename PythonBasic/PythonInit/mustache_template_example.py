import mustache

def render_template(my_dict):
    template = '''
    {{#my_dict}}
      ID: {{id}}
      Name: {{name}}
      Job: {{job}}
      Address:
      {{#address}}
        {{city}}
      {{/address}}
      Contact:
      {{#contact}}
        Phone: {{phone}}
        Email: {{email}}
      {{/contact}}
    {{/my_dict}}
    '''
    return mustache.render(template, {"my_dict": my_dict})

# Example usage:
my_dict = [
    {
        "id": 1,
        "name": "morpheus",
        "job": "leader",
        "address": [{"city": "Delhi"}, {"city": "Bombay"}],
        "contact": [{"phone": "9206918946"}, {"email": "deepak.kumar@gmail.com"}, {"phone": "9206918947"}, {"email": "kumar.deepak@gmail.com"}]
    },
    {
        "id": 2,
        "name": "dorpheus",
        "job": "follower",
        "address": [],
        "contact": []
    }
]

print(render_template(my_dict))