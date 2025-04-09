from similar import indicesToRemove


def test_returns_minus_1_array_if_strings_different():
    str1 = "bone"
    str2 = "dog"

    assert indicesToRemove(str1, str2) == [-1]
