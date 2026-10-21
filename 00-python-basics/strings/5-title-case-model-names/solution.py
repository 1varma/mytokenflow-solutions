def display_name(slug):
    parts = slug.replace("_", "-").split("-")
    return " ".join(p[0].upper() + p[1:] for p in parts if p)
