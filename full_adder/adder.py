def add(a, b):
    c_in = 0
    res = 0
    pos = 1
    while a != 0 or b != 0 or c_in != 0:
        a_bit = (a & 1)
        b_bit = (b & 1)
        sum, c_out = add_bits(a_bit, b_bit, c_in)
        if sum:
            res |= pos
        c_in = c_out
        a >>= 1
        b >>= 1
        pos <<= 1

    return res


def add_bits(a: int, b: int, c_in: int) -> tuple[int, int]:   # sum, c_out
    sum = a ^ b ^ c_in
    c_out = (a & b) | (b & c_in) | (a & c_in)
    return sum, c_out
