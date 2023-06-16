from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c_count = Counter(words[0])
        
        for word in words[1:]:
            c_count &= Counter(word)

        common_chars = []
        for char, count in c_count.items():
            common_chars.extend([char] * count)
        
        return common_chars
