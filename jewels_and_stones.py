# https://leetcode.com/problems/jewels-and-stones/

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        output = 0
        jewel_dict = {}
        for j in J:
            jewel_dict[j] = j

        for s in S:
            # Since this is a hash map, lookup is O(1), espeicially since J doesn't have repititions
            if jewel_dict.__contains__(s):
                output += 1
        return output

# O(len(J) + len(S)) i.e. O(m+n)
# print(Solution().numJewelsInStones("aABbnmJ","aosdfoiOIGDASDOIFPaoifdsjoijOPDGLJqowierjAOSIGJLBNMPOIJIUSE"))
print(Solution().numJewelsInStones("Jj","aaaaaaaabbbbbbbbbbbjJaaaaaaaZPOKIIUY"))
