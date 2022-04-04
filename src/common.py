#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
from typing import List

__author__ = "Henrique Kops"


def generate_key_sequences(ciphered_text: str, key_size: int) -> List[str]:
    """Generate all ciphered sequences for a given key size

    Args:
        ciphered_text (str): Ciphered text by Vigenere's Cipher
        key_size (int): Key size to slice the ciphered text

    Returns:
        List[str]: List of ciphered text slices by key's size
    """
    sequences = list()
    for key in range(key_size):
        stringBuilder = str()
        for hop in range(0, len(ciphered_text[key:]), key_size):
            stringBuilder += ciphered_text[key + hop]
        sequences.append(stringBuilder)
    return sequences
