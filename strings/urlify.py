

def urlify(s):
    new_s = ""
    for c in s:
        if c == " ":
            new_s += "%20"
        else:
            new_s += c
    return new_s


urlify("something is missing")