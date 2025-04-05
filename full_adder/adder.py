
def add(x, y):
    return x + y


def add_bits(a: int, b: int, c_in: int) -> tuple[int, int]:   # sum, c_out
    sum = a ^ b ^ c_in
    c_out = (a & b) | (b & c_in) | (a & c_in)
    return sum, c_out
