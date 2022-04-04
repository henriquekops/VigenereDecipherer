#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
import time
from sys import argv, exit

# project dependencies
from src.key_finder import KeyFinder
from src.frequency_analyser import FrequencyAnalyser

__author__ = "Henrique Kops"

ALPHABET = "alphabet"
IC = "ic"

args = {
    "english": {
        "ic": 0.065,
        "alphabet": "abcdefghijklmnopqrstuvwxyz"
    },
    "portuguese": {
        "ic": 0.072723,
        "alphabet": "abcdefghijklmnopqrstuvwxyz"
    }
}


if __name__ == "__main__":

    if len(argv) != 3:
        print("Usage:\n\tpython main.py < ciphered file > <english | portuguese>")
        exit(0)

    file_path = argv[1]
    language = argv[2]

    s = time.time()

    ciphered_text = open(file_path, "r").read().rstrip()

    kf = KeyFinder(args.get(language).get(ALPHABET))
    key_size = kf.find_key_size(ciphered_text, args.get(language).get(IC))

    fa = FrequencyAnalyser(key_size)
    key, deciphered = fa.decipher(ciphered_text)

    e = time.time()

    print(f"key size = {key_size}")
    print(f"key found = {key}")
    print(f"deciphered text = {deciphered[:100]}")
    print(f"time elapsed = {e-s}")