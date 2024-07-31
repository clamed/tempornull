# Method 2: Using list comprehension
cleaned_string = ''.join([char for char in example_string if char not in PUNCT_TO_REMOVE])
print(cleaned_string)
