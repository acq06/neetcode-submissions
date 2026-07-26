class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        def counter(s):
            count = [0] * 26
            for c in s:
                count[ord(c) -97] += 1

            return tuple(count)

        for word in strs:
            count = counter(word)
            if count in grouped:
                grouped[count].append(word)
            else:
                grouped[count] = [word]

        return list(grouped.values())