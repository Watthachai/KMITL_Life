def test_shuffle_string():
    # Test case 1: Even length string
    s1 = "abcd"
    expected1 = "acbd"
    assert shuffle_string(s1) == expected1

    # Test case 2: Odd length string
    s2 = "abcde"
    expected2 = "acebd"
    assert shuffle_string(s2) == expected2

    # Test case 3: Empty string
    s3 = ""
    expected3 = ""
    assert shuffle_string(s3) == expected3

    # Test case 4: String with only one character
    s4 = "a"
    expected4 = "a"
    assert shuffle_string(s4) == expected4

    # Test case 5: String with repeated characters
    s5 = "aabbbccc"
    expected5 = "acbacbcb"
    assert shuffle_string(s5) == expected5

    print("All test cases pass")

test_shuffle_string()