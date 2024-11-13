
def reverse_text(text):
    """Reverses the given text."""
    return text[::-1]

# Test cases
def test_reverse_text():
    assert reverse_text("hello") == "olleh", "Test Case 1 Failed"
    assert reverse_text("world") == "dlrow", "Test Case 2 Failed"
    assert reverse_text("Python") == "nohtyP", "Test Case 3 Failed"
    assert reverse_text("12345") == "54321", "Test Case 4 Failed"
    assert reverse_text("") == "", "Test Case 5 Failed"  # Test with empty string
    # assert reverse_text("A man, a plan, a canal, Panama!") == "!amanaP ,analp a ,nam A", "Test Case 6 Failed"  # Palindrome test
    assert reverse_text("A man, a plan, a canal, Panama!") == "!amanaP ,lanac a ,nalp a ,nam A", "Test Case 6 Failed"  # Palindrome test

    print("All test cases passed!")

# Run the tests
if __name__ == "__main__":
    test_reverse_text()
