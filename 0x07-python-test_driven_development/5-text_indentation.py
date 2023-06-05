#!/usr/bin/python3

def text_indentation(text):
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

if __name__ == "__main__":
    import doctest
    doctest.testfile("5-text_indentation.txt")
