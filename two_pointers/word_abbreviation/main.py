# https://leetcode.com/problems/valid-word-abbreviation


def debug(context="", **kwargs):
    print(
        (context + ": " if context else "")
        + " ".join(f"{k}={v}" for k, v in kwargs.items())
    )


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            if word[i] != abbr[j] and not abbr[j].isnumeric():
                return False

            subst_len_str = ""
            while abbr[j].isnumeric():
                if abbr[j] == "0" and len(subst_len_str) == 0:
                    return False
                subst_len_str += abbr[j]
                j += 1
                if j > len(abbr) - 1:
                    break
            i += int(subst_len_str)
            if i > len(word):
                debug("returning false - subst too far", i=i, j=j, word=word, abbr=abbr)
                return False

        debug("loop ended", i=i, j=j, word=word, abbr=abbr)
        if j < len(abbr):
            debug("there was more subst data")
            return False
        if i < len(word):
            debug("there was more word data")
            return False

        return True
