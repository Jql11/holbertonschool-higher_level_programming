#!/usr/bin/python3
def multiple_returns(sentence):
    if not len(sentence):
        sentence[0] = None
    else:
        return (len(sentence), sentence[0])
