#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

__author__ = "Henrique Kops"


class KeyFinder:

    def __init__(self, alphabet: str) -> None:
        self.__max_key_size = len(alphabet)
        self.__alphabet: List = list(alphabet)

    def __generate_sequences(self, ciphered_text: str, key_size: int) -> List:
        sequences = list()
        for key in range(key_size):
            stringBuilder = str()
            for hop in range(0, len(ciphered_text[key:]), key_size):
                stringBuilder += ciphered_text[key + hop]
            sequences.append(stringBuilder)
        return sequences

    def __coincidence_index(self, sequence: str) -> float:
        sum = 0
        n = len(sequence)
        for letter in self.__alphabet:
            letter_frequency = sequence.count(letter)
            sum += letter_frequency * (letter_frequency - 1)
        return sum / (n * (n - 1))

    def __generate_ics(self, ciphered_text):
        ics = list()
        for key_size in range(1, self.__max_key_size+1):
            sum = 0
            sequences = self.__generate_sequences(ciphered_text, key_size)
            for sequence in sequences:
                sum += self.__coincidence_index(sequence)
            ics.append(sum/len(sequences))
        return ics

    def find_key_size(self, ciphered_text, language_ic):
        ics = self.__generate_ics(ciphered_text)
        range = 0.001
        flag = True
        while (flag):
            key_size = 1
            for ic in ics:
                if language_ic + range > ic and language_ic - range < ic:
                    flag = False
                    break
                key_size += 1
            range += 0.001
        return key_size