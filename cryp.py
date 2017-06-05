def ebced(s):
    total = 0
    for x in s:
        total += ord(x)
    return total


def length(s):
    return len(s)


def cryps():
    return {"hash": hash,
            "ebced": ebced,
            "length": length
            }
