# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        ways = [0] * (n + 1)
        ways[0] = 0
        ways[1] = 1
        ways[2] = 2

        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]

    def fibonacci_with_memoization(self, n: int) -> int:
        fib_hash = {0: 0, 1: 1, 2: 1}
        if n in fib_hash:
            return n

        def fib_recur(n):
            if n in fib_hash:
                return fib_hash[n]
            fib_hash[n] = fib_recur(n - 2) + fib_recur(n - 1)
            return fib_hash[n]

        fib_recur(n)
        return fib_hash[n]

    def fib(self, n):
        def fib_memo(n, m):
            """
            Find the n'th fibonacci number. Uses memoization.

            :param n: the n'th fibonacci number to find
            :param m: dictionary used to store previous numbers
            :return: the value of the n'th fibonacci number
            """

            if n in m:
                return m[n]

            answer = fib_memo(n - 1, m) + fib_memo(n - 2, m)
            m[n] = answer
            return answer

        m = {1: 1, 2: 1}
        return fib_memo(n, m)


data1 = 4
answer1 = 5
assert Solution().climbStairs(data1) == answer1

data2 = 0
answer2 = 0
assert Solution().climbStairs(data2) == answer2

data2 = 5
answer2 = 8
assert Solution().climbStairs(data2) == answer2

data3 = 5
answer3 = 5
assert Solution().fibonacci_with_memoization(data3) == answer3

data4 = 7
answer4 = 13
assert Solution().fibonacci_with_memoization(data4) == answer4
