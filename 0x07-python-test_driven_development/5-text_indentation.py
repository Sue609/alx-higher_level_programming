#!/usr/bin/python3
"""We introduce the function text_indentation in this function"""


def text_indentation(text):
    """
    Prints the given text with indentation based on certain delimiters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the text is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if len(text) == 0:
        return

    new_text = ""
    delimiter = [".", "?", ":"]
    i = 0

    while i < len(text):
        new_text += text[i]
        if text[i] in delimiter and i < len(text) - 1 and text[i+1] == ' ':
            new_text += "\n\n"
            i += 1

        i += 1

    print(new_text)
