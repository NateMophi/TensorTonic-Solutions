def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    p = []
    n = len(actual_tokens)
    H = 0
    for i in range(n):
        # for j in range(n):
        #     if i==j:
                # p.append(prob_distributions[i][j])
         H += math.log(prob_distributions[i][actual_tokens[i]])/-n
    
    PP = math.exp(H)
    return PP