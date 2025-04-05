from adder import add, add_bits


def test_adder_adds_two_numbers():
    assert add(0, 0) == 0
    assert add(0, 1) == 1
    assert add(1, 0) == 1
    assert add(1, 1) == 2
    assert add(1, 2) == 3
    assert add(25, 3) == 28
    assert add(33, 44) == 77


def test_single_bit_adder():
    assert add_bits(0, 1, 0) == (1, 0)
    assert add_bits(1, 0, 0) == (1, 0)


def test_single_bit_adder_overflow():
    assert add_bits(1, 1, 0) == (0, 1)


def test_single_bit_adder_zero():
    assert add_bits(0, 0, 0) == (0, 0)


def test_single_bit_overflow_and_carry():
    assert add_bits(1, 1, 1) == (1, 1)
