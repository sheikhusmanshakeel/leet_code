# https://leetcode.com/problems/unique-morse-code-words/
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        seen_dict = {}
        code = {'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....','i': '..','j': '.---','k': '-.-','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.','q': '--.-','r': '.-.','s': '...','t': '-','u': '..-','v': '...-','w': '.--','x': '-..-','y': '-.--','z': '--..'}
        for word in words:            
            t = ""
            for c in word:
                t += code[c]
            if not seen_dict.__contains__(t):
                seen_dict[t] = t
        
        return len(seen_dict)


print(Solution().uniqueMorseRepresentations(["rwjje","aittjje","auyyn","lqtktn","lmjwn"]))




