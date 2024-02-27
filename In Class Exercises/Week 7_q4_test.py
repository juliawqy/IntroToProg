import q4

# Test case 1 - Pangram
sentence = "The quick brown fox jumps over the lazy dog."
print(q4.is_pangram(sentence))

# Test case 2 - Not a Pangram
sentence = "The quick brown fox jumps over the lazy cat."
print(q4.is_pangram(sentence))