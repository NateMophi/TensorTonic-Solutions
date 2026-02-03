def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    step = chunk_size - overlap
    slice = []
    n = len(tokens)

    for i in range(0, n, step):
        slice.append(tokens[i:i + chunk_size])
        if i + chunk_size >= n:
            break

    return slice
