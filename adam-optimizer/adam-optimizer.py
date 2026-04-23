import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    param = np.array(param)
    g = np.array(grad)
    m, v = np.array(m), np.array(v)
    # 1st Moment
    m_t = beta1 * m + (1 - beta1) * g

    # 2nd Moment
    v_t = beta2 * v + (1 - beta2) * g**2

    # Bias
    M = m_t / (1 - beta1**t)
    V = v_t / (1 - beta2**t)

    # Params
    param_t = param - lr * (M /(np.sqrt(V) + eps))
    return (param_t, m_t, v_t)
    