def common_prefix(prompts):
    if not prompts:
        return ""
    prefix = prompts[0]
    for p in prompts[1:]:
        i = 0
        while i < len(prefix) and i < len(p) and prefix[i] == p[i]:
            i += 1
        prefix = prefix[:i]
    return prefix
