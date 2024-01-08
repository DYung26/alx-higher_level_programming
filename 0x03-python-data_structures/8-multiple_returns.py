#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        senLen = len(sentence)
        if senLen == 0:
            Fchar = None
        else:
            Fchar = sentence[0]
        return (senLen, Fchar)
