from .json_validation import validate_json_schema


class Test_JSONValidation:
    def test_validate_json_schema_Should_return_True_when_valid_json_schema(self):
        valid_json_schema = {"name": "Widget", "price": 10.99, "quantity": 5}

        transaction_schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "price": {"type": "number", "minimum": 0},
                "quantity": {"type": "integer", "minimum": 1},
            },
            "required": ["name", "price", "quantity"],
        }

        is_valid_json_schema, message = validate_json_schema(
            valid_json_schema, my_schema=transaction_schema
        )

        assert is_valid_json_schema == True
        assert message == "JSON is valid"

    def test_validate_json_schema_Should_return_False_when_invalid_json_schema(self):
        invalid_json_schema = {"name": "Widget", "quantity": 5}

        transaction_schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "price": {"type": "number", "minimum": 0},
                "quantity": {"type": "integer", "minimum": 1},
            },
            "required": ["name", "price", "quantity"],
        }

        is_valid_json_schema, message = validate_json_schema(
            invalid_json_schema, my_schema=transaction_schema
        )

        assert is_valid_json_schema == False
        assert message == "Given JSON data is not valid"
