#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

__author__ = "Henrique Kops"


class KeyFinder:

    def __init__(self, alphabet: str) -> None:
        self.__alphabet: List = list(alphabet)

    def generate_sequences(self, ciphered_text: str, key_size: int) -> List:
        sequences = list()
        for key in range(key_size):
            stringBuilder = str()
            for hop in range(0, len(ciphered_text[key:]), key_size):
                stringBuilder += ciphered_text[key + hop]
            sequences.append(stringBuilder)
        return sequences

    def coincidence(self, sequence: str) -> float:
        sum = 0
        n = len(sequence)
        for letter in self.__alphabet:
            letter_frequency = sequence.count(letter)
            sum += letter_frequency * (letter_frequency - 1)
        return sum / (n * (n - 1))