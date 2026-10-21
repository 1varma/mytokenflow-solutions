def first_over(lengths, limit):
    for i, n in enumerate(lengths):
        if n > limit:
            return i
    return -1
