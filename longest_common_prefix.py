import unittest


def longest_common_prefix(strs: list[str]) -> str:
    min_word = min(strs, key=len)
    min_length = len(min_word)
    for i in range(min_length):
        for word in strs:
            if word[i] != strs[0][i]:
                return word[:i]
    return min_word
