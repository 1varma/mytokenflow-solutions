def cost_line(model, tokens, price_per_1k):
    cost = tokens / 1000 * price_per_1k
    return f"{model}: {tokens:,} tokens = ${cost:.4f}"
