#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: . ? :
"""


def text_indentation(text):
    """ print text with 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    new_list = []
    for line in text.split('\n'):
        new_list.append(line.lstrip(' '))
    new_text = "\n".join(new_list)
    print(new_text, end="")
