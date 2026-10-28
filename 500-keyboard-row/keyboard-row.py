from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        result = []

        for word in words:
            chars = set(word.lower())

            if any(chars <= row for row in rows):
                result.append(word)

        return result