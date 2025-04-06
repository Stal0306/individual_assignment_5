from individual_assignment_5 import clean_text_simple

def test_clean_text_simple():
    assert clean_text_simple("  Hello, WORLD!123  ") == "hello world"
    assert clean_text_simple("This... is fine!!") == "this is fine"
    assert clean_text_simple("  42 is THE answer?? ") == "is the answer"
    assert clean_text_simple("") == ""
    assert clean_text_simple("!!@@##") == ""
    print("All tests passed.")

# Run the tests if this file is executed directly
if __name__ == "__main__":
    test_clean_text_simple()