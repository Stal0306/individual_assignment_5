def clean_text_simple(text):
    """
    Cleans text by:
    - Lowercasing
    - Removing digits
    - Removing punctuation
    - Removing extra spaces
    
    Args:
        text (str): The string to clean.

    Returns:
        str: Cleaned string.
    """
    # Define basic punctuation characters to remove
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    digits = "0123456789"
    
    # Lowercase
    text = text.lower()
    
    # Remove digits
    text = ''.join([char for char in text if char not in digits])
    
    # Remove punctuation
    text = ''.join([char for char in text if char not in punctuation])
    
    # Remove extra spaces
    words = text.split()
    cleaned = ' '.join(words)
    
    return cleaned