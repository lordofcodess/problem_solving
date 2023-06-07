class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
       
        alphabet_order = {c: i for i, c in enumerate(order)}

        def compare_words(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
                if word1[i] != word2[i]:
                    if alphabet_order[word1[i]] > alphabet_order[word2[i]]:
                        return False
                    else:
                        return True
                i += 1
        
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not compare_words(words[i], words[i + 1]):
                return False

        return True

       
