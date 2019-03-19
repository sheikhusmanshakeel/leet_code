def str_search_bf(text, pattern):
    n = len(text)
    m = len(pattern)
    for s in range(0, n - m):
        string_found = True
        for k in range(0, m):
            if text[k + s] != pattern[k]:
                string_found = False
                break

        if string_found:
            break

    return (s, s + m - 1)


text = "usman shakeel is mansour's nephew"
pattern = "mansour"
t = str_search_bf(text, pattern)
print(text[t[0]:t[1] + 1])
print(t)
