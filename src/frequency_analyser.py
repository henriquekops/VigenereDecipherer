#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
from typing import List, Dict
from textwrap import wrap
from collections import Counter

__author__ = "Henrique Kops"


class FrequencyAnalyser:

    def __init__(self, key_size: int) -> None:
        self.__key_size = key_size

    def __generate_key_blocks(self, ciphered_text: str) -> List:
        blocks = wrap(ciphered_text, self.__key_size)
        return [''.join(map(lambda x: x[k], filter(lambda x: len(x) > k, blocks))) for k in range(self.__key_size)]

    # TODO: mocked character 'e', watch out for portuguese
    def __discover_key(self, blocks: List) -> str:
        key = str()
        for block in blocks:
            char_frequencies: Dict = Counter(block)
            most_frequent = max(char_frequencies.items(), key=operator.itemgetter(1))[0]
            char_distance = ord(most_frequent) - ord('e')
            if char_distance < 0: char_distance += 26
            key += chr(char_distance + 97)
        return key

    def decipher(self, ciphered_text: str) -> List[str]:
        blocks = self.__generate_key_blocks(ciphered_text)
        key = self.__discover_key(blocks)
        deciphered = str()
        for letter_idx in range(len(ciphered_text)):
            char_distance = ord(ciphered_text[letter_idx]) - ord(key[letter_idx % len(key)])
            if char_distance < 0: char_distance += 26
            deciphered += chr( char_distance + 97 )
        return key, deciphered