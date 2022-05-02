#!/usr/bin/python3
def multiple_returns(sentence):
    if not len(sentence):
        return (len(sentnece), None)
    else:
        return (len(sentence), sentence[0])
