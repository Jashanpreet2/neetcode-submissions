class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        longest = 1
        characters = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        counts = dict()
        for i in range(len(s)):
            for j in range(i, len(s)):
                for c in characters:
                    counts[c] = 0
                for l in range(i, j+1):
                    counts[s[l]] += 1
                most_freq = None
                for c in characters:
                    if counts[c] > 0 and (most_freq == None or counts[c] > counts[most_freq]):
                        most_freq = c
                if l - i + 1 - counts[most_freq] <= k:
                    longest = max(l - i + 1, longest)
        return longest
