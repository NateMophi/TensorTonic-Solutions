def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0) -> float:
    """
    Linear warmup (0→initial_lr) then linear decay (initial_lr→final_lr).
    Steps are 0-based; clamp at final_lr after total_steps.
    """
    t = step
    if t>total_steps:
        return final_lr
    if t == total_steps:
        return final_lr

    while t<total_steps:
        if t < warmup_steps:
            LR = (t * initial_lr) / warmup_steps
            return LR
        if warmup_steps <= t <= total_steps:
            LR = final_lr + (initial_lr-final_lr) * (total_steps-t)/(total_steps-warmup_steps)
            return LR
        if t > total_steps:
            return final_lr
        t+=1
    