from test_framework import generic_test


def parity(x: int) -> int:
    even_indicator = 0
    while x:
        even_indicator ^= (x & 1)
        x >>= 1
    return even_indicator


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
