from collections import Counter



def is_perm_palin(s):
    c = Counter()
    for ch in s:
        if ch != ' ':
            c[ch] += 1

    number_of_odds = 0
    for v in c.values():
        if v % 2 == 1:
            number_of_odds += 1

        if number_of_odds > 1:
            return False

    return True


# data1 = "abbc abb"
# ans1 = True
# assert is_perm_palin(data1) == ans1

data2 = "abcd aa ecba"
ans2 = False
assert is_perm_palin(data2) == ans2