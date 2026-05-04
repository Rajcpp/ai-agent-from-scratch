def convert_value(value, expected_type):
    if value is None:
        return None
    try:
        return expected_type(value)
    except ValueError:
        print(f"Error: Could not convert '{value}' to {expected_type.__name__}.")
        return None
