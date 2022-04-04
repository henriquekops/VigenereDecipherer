#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from src.key_finder import KeyFinder
from src.frequency_analyser import FrequencyAnalyser

__author__ = "Henrique Kops"

ENGLISH_ALPHA = "abcdefghijklmnopqrstuvwxyz"
ENGLISH_IC = 0.065

PORTUGUESE_ALPHA = "abcdefghijklmnopqrstuvwxyz"
PORTUGUESE_IC = 0.072723


if __name__ == "__main__":

    ciphered_text = open("test/english.txt", "r").read().rstrip()

    kf = KeyFinder(ENGLISH_ALPHA)
    key_size = kf.find_key_size(ciphered_text, ENGLISH_IC)

    fa = FrequencyAnalyser(key_size)
    key, deciphered = fa.decipher(ciphered_text)

    print(f"key size = {key_size}")
    print(f"key found = {key}")
    print(f"deciphered text = {deciphered[:100]}")