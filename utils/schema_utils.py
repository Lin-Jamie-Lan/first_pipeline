from jsonschema import validate, ValidationError

def validate_schema(data, schema):
    # Convert DataFrame to List of Dictionaries
    data = data.to_dict(orient="records")
    print(schema)
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise ValueError(f"Schema validation failed: {e.message}, check lin!")