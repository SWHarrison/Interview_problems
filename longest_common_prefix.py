class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # first letter of first word in the list
        # initial prefix is whole word of the 0th element of the list
        prefix = strs[0]
        # iterate through list of words
        for i in range(1, len(strs)):
            word = strs[i]
            # compare the jth element of each word against the prefix[j]
            for j in range(len(word)):
                print(word, prefix)
                # print(f"prefix[j]: {prefix[j]}, word[j]: {word[j]}")
                # no common prefix when the 0th element doesnt match
                if prefix[j] != word[j] and j == 0:
                    print("missmatch")
                    return ""
                # unmatch
                elif prefix[j] != word[j]:
                    print("missmatch 2")
                    break
            # update the prefix, choose min of length
            print("pref",prefix)
            print(j)
            prefix = prefix if len(prefix) < len(word[0:j+1]) else word[0:j+1]
            print(f"pre: {prefix}")
        return prefix
# strs = ["flower", "flow", "flight", 'd']
strs = ["b", ""]
obj = Solution()
print("prefix: ", obj.longestCommonPrefix(strs))
