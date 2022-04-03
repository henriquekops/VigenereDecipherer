#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from xmlrpc.client import MAXINT
from src.frequency_analyser import FrequencyAnalyser
from src.key_finder import KeyFinder

__author__ = "Henrique Kops"

PORTUGUESE_IC = 0.072723
ENGLISH_IC = 0.065

ENGLISH_ALPHA = "abcdefghijklmnopqrstuvwxyz"
PORTUGUESE_ALPHA = "abcdefghijklmnopqrstuvwxyz"


if __name__ == "__main__":

    max_key_size = len(PORTUGUESE_ALPHA)

    ciphered_text = open("portuguese.txt", "r").read().rstrip()

    kf = KeyFinder(PORTUGUESE_ALPHA)

    ics = list()

    for key_size in range(1, max_key_size+1):
        sum = 0
        sequences = kf.generate_sequences(ciphered_text, key_size)
        for sequence in sequences:
            sum += kf.coincidence(sequence)
        ics.append(sum/len(sequences))

    range = 0.001
    flag = True
    while (flag):
        key_size = 1
        for ic in ics:
            if PORTUGUESE_IC + range > ic and PORTUGUESE_IC - range < ic:
                flag = False
                break
            key_size += 1
        range += 0.001

    fa = FrequencyAnalyser(PORTUGUESE_ALPHA)
    blocks = fa.generate_blocks(ciphered_text, key_size)
    key = fa.discover_key(blocks)
    deciphered = fa.decipher(ciphered_text, key)

    print(f"key size = {key_size}")
    print(f"key = {key}")
    print(f"deciphered = {deciphered[:30]}")
    
    
    # d = dict(enumerate(ics))
    # x = {k: d[k] for k in sorted(d, key=d.get)}

    # print(x)

    # best_k: int = 10000000
    # best_v: float = 10000000

    # for k, v in x.items():
    #     if v - ENGLISH_IC < best_v:
    #         best_v = v
    #         best_k = k

    # print(best_k)
    # print(best_v)