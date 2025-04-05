from adder import add, add_bits


def test_adder_adds_two_numbers():
    assert add(1, 2) == 3


def test_single_bit_adder():
    assert add_bits(0, 1, 0) == (1, 0)
    assert add_bits(1, 0, 0) == (1, 0)


def test_single_bit_adder_overflow():
    assert add_bits(1, 1, 0) == (0, 1)


def test_single_bit_adder_zero():
    assert add_bits(0, 0, 0) == (0, 0)


def test_single_bit_overflow_and_carry():
    assert add_bits(1, 1, 1) == (1, 1)
