python
    import json

    # A JSON string
    json_string = '{"name": "Alice", "age": 25, "courses": ["Math", "Science"]}'

    # Parse the string into a Python dictionary
    data_dict = json.loads(json_string)
    print(type(data_dict))  # Output: <class 'dict'>
    print(data_dict['name'])  # Output: Alice
    print(data_dict['courses'][1])  # Output: Science