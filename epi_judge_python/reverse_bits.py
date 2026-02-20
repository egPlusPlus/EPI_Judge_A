from test_framework import generic_test


def reverse_bits(n: int) -> int:
    n = ((n & 0xFFFFFFFF00000000) >> 32) | ((n & 0x00000000FFFFFFFF) << 32)
    n = ((n & 0xFFFF0000FFFF0000) >> 16) | ((n & 0x0000FFFF0000FFFF) << 16)
    n = ((n & 0xFF00FF00FF00FF00) >> 8) | ((n & 0x00FF00FF00FF00FF) << 8)
    n = ((n & 0xF0F0F0F0F0F0F0F0) >> 4) | ((n & 0x0F0F0F0F0F0F0F0F) << 4)
    n = ((n & 0xCCCCCCCCCCCCCCCC) >> 2) | ((n & 0x3333333333333333) << 2)
    n = ((n & 0xAAAAAAAAAAAAAAAA) >> 1) | ((n & 0x5555555555555555) << 1)

    return n


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
