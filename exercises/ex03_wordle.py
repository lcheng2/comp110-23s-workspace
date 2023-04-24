"""EX03 - Wordle."""

__author__ = "730517752"

def contains_char(guess: str, char: str) -> str:
    """finds if char is in guess"""
    idx: int = 0
    assert len(char) == 1
    while idx < len(guess):
        if guess[idx] == char:
            return True
        idx = idx + 1
    else:
            return False

def emojified()