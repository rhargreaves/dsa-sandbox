from similar import indicesToRemove


def test_returns_minus_1_array_if_strings_different():
    str1 = "bone"
    str2 = "dog"

    assert indicesToRemove(str1, str2) == [-1]


def test_returns_one_index_to_remove():
    str1 = "hind"
    str2 = "hid"

    assert indicesToRemove(str1, str2) == [2]


def test_returns_more_than_one_index_to_remove():
    str1 = "aabbb"
    str2 = "aabb"

    assert indicesToRemove(str1, str2) == [2, 3, 4]
