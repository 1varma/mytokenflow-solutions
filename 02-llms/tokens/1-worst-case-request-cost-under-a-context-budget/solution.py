def max_request_cost(context_window, prompt_tokens, max_output, price_in_per_m, price_out_per_m):
    room = context_window - prompt_tokens
    if room < 1:
        raise ValueError("prompt leaves no room for output")
    budget = min(max_output, room)
    cost = (prompt_tokens * price_in_per_m + budget * price_out_per_m) / 1_000_000
    return {"output_budget": budget, "max_cost": cost}
