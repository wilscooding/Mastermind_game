from extensions.hints_extension import provide_hint
# from hints_extension import provide_hint


def test_hint_generation():
    # Test case 1: All incorrect guess
    secret_code = [1, 2, 3, 4]
    previous_guesses = [[5, 6, 7, 8]]
    previous_feedback = [(0, 0)]
    actual_hint = provide_hint(
        secret_code, previous_guesses, previous_feedback)
    print("Test case 1:")
    print("Actual Hint:", actual_hint)
    assert isinstance(actual_hint, list)
    if actual_hint:
        assert any("should be higher" in hint or "should be lower" in hint for hint in actual_hint) or \
            any(f"at position {i + 1}" in hint for i in range(4)
                for hint in actual_hint)

    # Test case 2: Correct numbers but in wrong positions
    secret_code = [1, 2, 3, 4]
    previous_guesses = [[5, 1, 6, 7]]
    previous_feedback = [(1, 0)]
    actual_hint = provide_hint(
        secret_code, previous_guesses, previous_feedback)
    print("Test case 2:")
    print("Actual Hint:", actual_hint)
    assert isinstance(actual_hint, list)
    if actual_hint:
        assert any("should be higher" in hint or "should be lower" in hint for hint in actual_hint) or \
            any(f"at position {i + 1}" in hint for i in range(4)
                for hint in actual_hint)

    # Test case 3: Some numbers in correct positions
    secret_code = [1, 2, 3, 4]
    previous_guesses = [[1, 5, 6, 7]]
    previous_feedback = [(1, 1)]
    actual_hint = provide_hint(
        secret_code, previous_guesses, previous_feedback)
    print("Test case 3:")
    print("Actual Hint:", actual_hint)
    assert isinstance(actual_hint, list)
    if actual_hint:
        assert any("should be higher" in hint or "should be lower" in hint for hint in actual_hint) or \
            any(f"at position {i + 1}" in hint for i in range(4)
                for hint in actual_hint)

    # Test case 4: All correct numbers but in wrong positions
    secret_code = [1, 2, 3, 4]
    previous_guesses = [[4, 3, 2, 1]]
    previous_feedback = [(4, 0)]
    actual_hint = provide_hint(
        secret_code, previous_guesses, previous_feedback)
    print("Test case 4:")
    print("Actual Hint:", actual_hint)
    assert isinstance(actual_hint, list)
    if actual_hint:
        assert any("should be higher" in hint or "should be lower" in hint for hint in actual_hint) or \
            any(f"at position {i + 1}" in hint for i in range(4)
                for hint in actual_hint)

    # Add more test cases as needed


if __name__ == '__main__':
    test_hint_generation()
