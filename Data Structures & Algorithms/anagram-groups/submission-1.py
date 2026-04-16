class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def letter_dict(word):
            dictionary = {}
            for letter in word:
                if letter in dictionary:
                    dictionary[letter] += 1
                else:
                    dictionary[letter] = 1
            return dictionary
        
        def check_word(i, j):
            copy_dict = original_dict.copy()
            # Length must be the same
            if len(strs[j]) != len(strs[i]):
                return

            for letter in strs[j]:
                if letter not in copy_dict:
                    break
                elif copy_dict[letter] == 0:
                    break
                else:
                    copy_dict[letter] -= 1
            else:
                group.append(strs[j])
                is_in_a_group.add(j)

        is_in_a_group = set()

        out = []
        for i in range(len(strs)):
            # Check if this element has already been added to a group
            if i in is_in_a_group:
                continue

            group = [strs[i]]

            original_dict = letter_dict(strs[i])

            # Loop until all words until i
            for j in range(0, i):
                check_word(i, j)

            # Loop through all words starting from i + 1
            for j in range(i + 1, len(strs)):
                check_word(i, j)

            out.append(group)

        return out
        