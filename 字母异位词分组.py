class Solution:
    def groupAnagrams(self, strs):
        d = dict()
        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
            if word not in d:
                d[word] = [strs[i]]
            else:
                d[word].append(strs[i])

        return list(d.values())

strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
s = Solution()
print(s.groupAnagrams(strs))
