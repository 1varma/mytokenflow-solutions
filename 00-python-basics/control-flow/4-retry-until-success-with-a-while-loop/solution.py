def calls_needed(attempts, max_calls):
    calls = 0
    while calls < max_calls:
        ok = calls < len(attempts) and attempts[calls]
        calls += 1
        if ok:
            return calls
    return -1
