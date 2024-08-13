# One span is zero, hence we can add
def add_spans(span1, span2):
    if span1 == 0 or span2 == 0:
        return span1 + span2
    
    # Additional logic for adding spans when neither is zero
    return span1 + span2

# Example usage
span_a = 0
span_b = 5
result = add_spans(span_a, span_b)
print(f"Result: {result}")  # Output: Result: 5
