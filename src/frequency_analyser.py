#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
from typing import List
from textwrap import wrap
from collections import Counter
from typing import Dict

__author__ = "Henrique Kops"


class FrequencyAnalyser:

    def __init__(self, alphabet) -> None:
        self.__alphabet = alphabet

    def generate_blocks(self, ciphered_text, key_size) -> List:
        blocks = wrap(ciphered_text, key_size)
        return [''.join(map(lambda x: x[k], filter(lambda x: len(x) > k, blocks))) for k in range(key_size)]

    def discover_key(self, blocks: List):
        key = ""
        for block in blocks:
            frequencies: Dict = Counter(block)
            max_char = max(frequencies.items(), key=operator.itemgetter(1))[0]
            # TODO: mocado e, cuidado com pt
            key += chr(abs(ord(max_char)-ord('e'))+97)
        return key

    def decipher(self, ciphered_text, key):
        deciphered = ""
        for i in range(len(ciphered_text)):
            dist = ord(ciphered_text[i]) - ord(key[i % len(key)])
            if dist < 0:
                dist += 26
            deciphered += chr( dist + 97 )
        return deciphered