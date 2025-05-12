from typing import List

# 809. Expressive Words (medium)
# https://leetcode.com/problems/expressive-words/


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def is_stretchy(s, word):
            i = 0
            j = 0
            while i < len(word) and j < len(s):
                if word[i] != s[j]:
                    return False

                conseq_word_chars = 0
                prev_char = word[i]
                while i < len(word) and word[i] == prev_char:
                    conseq_word_chars += 1
                    i += 1

                conseq_s_chars = 0
                prev_char = s[j]
                while j < len(s) and s[j] == prev_char:
                    conseq_s_chars += 1
                    j += 1

                if conseq_word_chars > conseq_s_chars:
                    return False

                if conseq_word_chars != conseq_s_chars and conseq_s_chars < 3:
                    return False

            return i == len(word) and j == len(s)

        count = 0
        for word in words:
            if is_stretchy(s, word):
                count += 1

        return count
