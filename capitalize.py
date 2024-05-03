def capitalCase(input: str):
    if not isinstance(input, str):
        raise TypeError("Please provide string")
    return input.capitalize()