import argparse
import ast

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

def cmdline():
    parser = argparse.ArgumentParser(prog ='divide',
                                     description ='Divide polynomials: use the divide command')
    parser.add_argument('dividend', metavar ='dividend', type=str, nargs=1, help= 'Dividend, like 2,-1,7,4')
    parser.add_argument('divisor', metavar ='divisor', type=str, nargs=1, help= 'Divisor, like 2,1')
    args = parser.parse_args()
    try:
        print("Result:", end=' ')
        res = polynomial_divide(ast.literal_eval(args.dividend[0]), ast.literal_eval(args.divisor[0]))
        for i, n in enumerate(res[:-1]):
            print(n, 'x^', len(res)-i-1, sep='', end=' + ')
        print(res[-1])
        return 0
    except:
        print("ERROR")
        return 1
