#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.common import generate_key_sequences

# built-in dependencies
import operator
from typing import List, Dict
from collections import Counter

__author__ = "Henrique Kops"


class FrequencyAnalyser:

    def __init__(self, key_size: int) -> None:
        """FrequencyAnalyser class is meant to decipher a ciphered text by a given key size

        Args:
            key_size (int): Size of the key used to cipher the text
        """
        self.__key_size = key_size

    # TODO: mocked character 'e', watch out for portuguese
    def __discover_key(self, sequences: List) -> str:
        """Key discovery by frequency analisys over ciphered sequences by same key

        Args:
            sequencies (List): List of sequences where each is ciphered by same key

        Returns:
            str: Key used to cipher the text
        """
        key = str()
        for sequence in sequences:
            char_frequencies: Dict = Counter(sequence)
            most_frequent = max(char_frequencies.items(), key=operator.itemgetter(1))[0]
            char_distance = ord(most_frequent) - ord('e')
            if char_distance < 0: char_distance += 26
            key += chr(char_distance + 97)
        return key

    def decipher(self, ciphered_text: str) -> List[str]:
        """Decipher the ciphered text by Vigenere's cipher

        Args:
            ciphered_text (str): Ciphered text by Vigenere's Cipher

        Returns:
            List[str]: List containing the discovered key and deciphered text
        """
        sequences = generate_key_sequences(ciphered_text, self.__key_size)
        key = self.__discover_key(sequences)
        deciphered = str()
        for letter_idx in range(len(ciphered_text)):
            char_distance = ord(ciphered_text[letter_idx]) - ord(key[letter_idx % len(key)])
            if char_distance < 0: char_distance += 26
            deciphered += chr( char_distance + 97 )
        return key, deciphered