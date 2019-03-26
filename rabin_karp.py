def rabin_karp_matcher(text, pattern, radix, prime):
    n = len(text)
    m = len(pattern)
    p = 0
    t = 0
    h = 1
    # The value of h would be "pow(d, M-1)%q"
    for i in range(m - 1):
        h = (h * radix) % prime

    for i in range(m):
        p = (radix * p + ord(pattern[i])) % prime
        t = (radix * t + ord(text[i])) % prime

    for s in range(n - m + 1):  # O(n-m)
        if p == t:
            if pattern == text[s:s + m]:  # O(m) operation
                print("pattern found at index {}".format(s))
        if s < n - m:
            t = (((t - ord(text[s]) * h) * radix) + ord(text[s + m])) % prime


text = "this is not good"
pattern = "good"
# search(text, pattern, 887)
rabin_karp_matcher(text, pattern, 256, 887)
