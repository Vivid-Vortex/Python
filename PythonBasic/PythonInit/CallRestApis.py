import requests


def make_request(url, method, headers=None, params=None, data=None, json_data=None, page=None):
    """
    Perform an HTTP request (GET, POST, PUT, PATCH, DELETE) with optional pagination for GET requests.

    :param url: The URL to send the request to.
    :param method: The HTTP method ('GET', 'POST', 'PUT', 'PATCH', 'DELETE').
    :param headers: Optional headers to include in the request.
    :param params: Optional query parameters to include in the request.
    :param data: Optional form data to include in the request.
    :param json_data: Optional JSON data to include in the request.
    :param page: Optional page number for paginated GET requests.
    :return: Response content (JSON if possible, otherwise text).
    """
    try:
        method = method.upper()
        if method == 'GET' and page is not None:
            if params is None:
                params = {}
            params['page'] = page

        if method == 'GET':
            response = requests.get(url, headers=headers, params=params)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=data, json=json_data)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, data=data, json=json_data)
        elif method == 'PATCH':
            response = requests.patch(url, headers=headers, data=data, json=json_data)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers, params=params)
        else:
            raise ValueError("Invalid HTTP method. Use 'GET', 'POST', 'PUT', 'PATCH', or 'DELETE'.")

        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Try to return the response as JSON, fallback to text if JSON conversion fails
        try:
            return response.json()
        except ValueError:
            return response.text

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
# if __name__ == "__main__":
    # url = 'https://reqres.in/api/users'
    # headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
    # params = {'key1': 'value1', 'key2': 'value2'}

    # url = 'https://reqres.in/api/users'
    # page = 2
    # response = make_request(url, 'GET', page=page)
    # if response:
    #     print("GET response with pagination:", response)

    # GET request example with pagination
    # url = 'https://reqres.in/api/users'
    # page = 2
    # response = make_request(url, 'GET', headers=headers, params=params, page=page)
    # if response:
    #     print("GET response with pagination:", response)

    # # GET request example without pagination
    # url = 'https://reqres.in/api/users'
    # response = make_request(url, 'GET', headers=headers, params=params)
    # if response:
    #     print("GET response without pagination:", response)
    #
    # POST request example
    # url = 'https://reqres.in/api/users'
    # json_data = { "name": "morpheus", "job": "leader" }
    # headers = ''
    # response = make_request(url, 'POST', headers=headers, json_data=json_data)
    #
    # if response:
    #     print("POST response:", response)
    #
    # # PUT request example
    # url = 'https://api.example.com/update'
    # json_data = {'key1': 'new_value1', 'key2': 'new_value2'}
    # response = make_request(url, 'PUT', headers=headers, json_data=json_data)
    # if response:
    #     print("PUT response:", response)
    #
    # # PATCH request example
    # url = 'https://api.example.com/update_partial'
    # json_data = {'key1': 'partial_update_value'}
    # response = make_request(url, 'PATCH', headers=headers, json_data=json_data)
    # if response:
    #     print("PATCH response:", response)
    #
    # # DELETE request example with pagination
    # url = 'https://api.example.com/delete'
    # params = {'key1': 'value1'}
    # response = make_request(url, 'DELETE', headers=headers, params=params, page=page)
    # if response:
    #     print("DELETE response with pagination:", response)
