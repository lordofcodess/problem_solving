class Solution:
    def similarPairs(self, words: List[str]) -> int:
        num_similar_pairs = 0

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if set(words[i]) == set(words[j]):
                    num_similar_pairs += 1

        return num_similar_pairs
