def format_strings(*args):
    combined_string = ''.join(args)
    formatted_string = combined_string.upper()
    if ' ' in combined_string:
        formatted_string = formatted_string.replace(' ', '-')
    return formatted_string

if __name__ == '__main__':
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python", "is", "fun")
    print(result)  # Output: "PYTHONISFUN"

    result = format_strings("Hello world")
    print(result)  # Output: "HELLO-WORLD"