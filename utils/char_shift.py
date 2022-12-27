from typing import *


def shift(b: bytes, n: int = 1, wrap26: bool = False) -> bytes:
    """shift each char in b of n"""
    buffer = bytearray()

    for c in b:
        first_letter = None
        if wrap26:
            if ord("a") <= c <= ord("z"):
                first_letter = ord("a")
            if ord("A") <= c <= ord("Z"):
                first_letter = ord("A")

            if first_letter:
                new_c = c - first_letter
                new_c += n
                new_c %= 26
                new_c += first_letter
            else:
                new_c = c
        else:
            new_c = c + n

        buffer.append(new_c)
    return bytes(buffer)


def pico13(b: bytes) -> bytes:
    return shift(b, n=13, wrap26=True)
