def check_word_presence(sentence, word):
    # Convert both the sentence and word to lowercase for case-insensitive comparison
    sentence_lower = sentence.lower()
    word_lower = word.lower()

    # Check if the word is present in the sentence
    is_present = word_lower in sentence_lower

    return is_present

# Example usage:
input_sentence = input("Enter a sentence: ")
input_word = input("Enter a word to check: ")

# Check if the word is present in the sentence
result = check_word_presence(input_sentence, input_word)

# Display the result
if result:
    print(f"The word '{input_word}' is present in the sentence.")
else:
    print(f"The word '{input_word}' is not present in the sentence.")
