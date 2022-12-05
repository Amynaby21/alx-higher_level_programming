#!/usr/bin/python3
def multiple_returns(sentence):
    len_sen = len(sentence)
    return (len_sen, sentence[0] if len_sen > 0 else None)
