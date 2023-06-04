#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    txt = text.strip()
    line_break_chars = ['.', '?', ':']

    result = ""

    for char in text:
        result += char

        if char in line_break_chars:
            result += '\n\n'

    lines = result.split('\n')
    formatted_lines = [line.strip() for line in lines]

    if formatted_lines[-1] == "":
        formatted_lines = formatted_lines[:-1]
    result = '\n'.join(formatted_lines)

    print(result)
if __name__ == "__main__":
    import doctest
    doctest.testfile("5-text_indentation.txt")
