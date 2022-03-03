def vector_affinity(a, b):
    if a == b:
        res = 1.0
    else:
        min_ = min(len(a),len(b))
        max_ = max(len(a),len(b))
        cnt = 0
        for i in range(min_):
            if a[i] == b[i]:
                cnt += 1
        res = cnt/max_ if max_ != 0 else 0.0
    return res
