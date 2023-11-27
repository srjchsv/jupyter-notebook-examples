import jsonschema


def validate_json_schema(json_data, my_schema):
    """https://json-schema.org/"""
    try:
        jsonschema.validate(instance=json_data, schema=my_schema)
    except jsonschema.ValidationError as err:
        print(err)
        return False, "Given JSON data is not valid"
    return True, "JSON is valid"
