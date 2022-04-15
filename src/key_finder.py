#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
from typing import List

# project dependencies
from src.common import generate_key_sequences

__author__ = "Henrique Kops"


class KeyFinder:

    """KeyFinder class is meant to find the key size for a ciphered text using Vigenere's Cipher"""

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    IC = 0.065

    def __coincidence_index(self, sequence: str) -> float:
        """Calculate the coincidence index for a given sequence of chars

        Args:
            sequence (str): A sequence of chars ciphered by the same key char 

        Returns:
            float: Coincidence index of the sequence
        """
        sum = 0
        n = len(sequence)
        for letter in list(self.ALPHABET):
            letter_frequency = sequence.count(letter)
            sum += letter_frequency * (letter_frequency - 1)
        return sum / (n * (n - 1))

    def __generate_ics(self, ciphered_text: str) -> List[str]:
        """Generate a list of average of coincidence indexes by key size

        Args:
            ciphered_text (str): Ciphered text by Vigenere's Cipher

        Returns:
            List[str]: A list of average of coincidence indexes by key size
        """
        ics = list()
        for key_size in range(1, len(self.ALPHABET)+1):
            sum = 0
            sequences = generate_key_sequences(ciphered_text, key_size)
            for sequence in sequences: sum += self.__coincidence_index(sequence)
            ics.append(sum/len(sequences))
        return ics

    def find_key_size(self, ciphered_text: str) -> int:
        """Find the key size that encrypts the ciphered text at given language 

        Args:
            ciphered_text (str):  Ciphered text by Vigenere's Cipher

        Returns:
            int: Length of the key used to cipher the text
        """
        ics = self.__generate_ics(ciphered_text)
        range = 0.01
        ic_diff = 1
        while (ic_diff > range):
            key_size = 0
            for ic in ics:
                if ic_diff > range:
                    ic_diff = self.IC - ic
                    key_size += 1
            range += range
        return key_size