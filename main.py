#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
from io import IOBase
import time
from sys import argv, exit
from typing import final

# project dependencies
from src.key_finder import KeyFinder
from src.frequency_analyser import FrequencyAnalyser

__author__ = "Henrique Kops"

HELP = "Usage:\n\tpython main.py < ciphered file >"


def open_file(file_path: str) -> str:
    """Tries to open file's content as string, validating if it exists

    Args:
        file_path (str): Path of the file to open

    Returns:
        str: File's content
    """
    file = IOBase()
    try:
        file = open(file_path, "r")
        return file.read().rstrip()
    except FileNotFoundError:
        print("ERROR: Ciphered text not found!")
        print(HELP)
        exit(0)
    finally:
        file.close()


if __name__ == "__main__":

    if len(argv) != 2:
        print(HELP)
        exit(0)

    file_path = argv[1]

    ciphered_text: str = open_file(file_path)

    s = time.time()

    kf = KeyFinder()
    key_size = kf.find_key_size(ciphered_text)

    fa = FrequencyAnalyser(key_size)
    key, deciphered = fa.decipher(ciphered_text)

    e = time.time()

    print(f"key size = {key_size}")
    print(f"key found = {key}")
    print(f"deciphered text = {deciphered[:100]}")
    print(f"time elapsed = {e-s}")