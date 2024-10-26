def analyze_sentence(sentence):
    # Initialize counters
    length_counter = 0
    word_counter = 0
    vowel_counter = 0
    vowels = "aeiouAEIOU"

    # Iterate over each character
    for i, char in enumerate(sentence):
        # Count the length
        length_counter += 1

        # Count words: Check for spaces or end period for words
        if char == ' ' and i > 0 and sentence[i - 1] != ' ':
            word_counter += 1
        elif char == '.':
            if i > 0 and sentence[i - 1] != ' ':
                word_counter += 1

        # Count vowels
        if char in vowels:
            vowel_counter += 1

    # Output the results
    print("Sentence length (characters including period):", length_counter)
    print("Number of words:", word_counter)
    print("Number of vowels:", vowel_counter)

# Example use
sentence = "This is a test sentence."
analyze_sentence(sentence)
