#!/usr/bin/python3
"""
a module that prints a text with 2 new lines after
each of these characters .,? and :
the module conatain a function def text_indentation(text)
"""
def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each of these
    characters:".,? and :"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punctuation = ['.', '?', ':']
    new_text = ""
    for char in text:
        new_text += char
        if char in punctuation:
            print(new_text.strip())
            print()
            new_text = ""
    if new_text.strip() != "":
        print(new_text.strip())
