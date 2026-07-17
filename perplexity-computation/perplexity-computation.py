def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    p = []
    n = len(actual_tokens)
    H = sum([math.log(prob_distributions[i][actual_tokens[i]]) for i in range(n)])/-n
    return math.exp(H)