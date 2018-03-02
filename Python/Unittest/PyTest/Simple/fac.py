#!/usr/bin/env python

def fac(n):
    if (n == 0 or n == 1):
        return 1;
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i;
        return result

if __name__ == '__main__':
    from argparse import ArgumentParser
    arg_parser = ArgumentParser(description='compute factorials')
    arg_parser.add_argument('n', type=int, default=5,
                            help='maximum argument')
    options = arg_parser.parse_args()
    for i in range(options.n + 1):
        print(f'fac({i}) = {fac(i)}')