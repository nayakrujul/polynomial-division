def polynomial_divide(dividend, divisor):
    if len(divisor) >= len(dividend):
        raise ValueError('divisor bigger than dividend')
    l = len(divisor)
    r = ()
    d = divisor
    for i in range(len(dividend) - l + 1):
        r += (d[0] / divisor[0],)
        d = tuple(x * r[-1] for x in divisor)
        _d = ()
        for j, n in enumerate(d[1:]):
            _d += (dividend[i+j+1] - n,)
        try:
            _d += (dividend[i+l],)
        except:
            pass
        d = _d
    return r
