class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def canTransform(word1, word2):
            different = 0
            for i in range(len(word1)):
                if different > 1:
                    break
                if word1[i] != word2[i]:
                    different += 1
            return different == 1
        explorables = set(wordList)
        queue = [(beginWord, 1)]
        i = 0
        while i < len(queue):
            curWord, dist = queue[i]
            i += 1
            removed = set()
            for word in explorables:
                if not canTransform(curWord, word):
                    continue
                if word == endWord:
                    return dist+1
                else:
                    queue.append((word, dist+1))
                    removed.add(word)
            for word in removed:
                explorables.remove(word)
        return 0

    


