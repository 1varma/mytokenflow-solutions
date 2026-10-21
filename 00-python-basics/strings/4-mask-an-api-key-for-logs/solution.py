def mask_key(key):
    if len(key) <= 10:
        return "***"
    return key[:3] + "..." + key[-4:]
