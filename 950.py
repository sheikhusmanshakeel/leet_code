# https://leetcode.com/problems/reveal-cards-in-increasing-order/
import collections


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N
        sorted_deck = sorted(deck)

        for card in sorted_deck:
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans


data = [17,13,11,2,3,5,7]
Solution().deckRevealedIncreasing(data)