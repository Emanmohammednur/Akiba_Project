def cleaned_text(text):
    """Convert text to lowercase and remove basic punctuation."""
    for mark in ",.?!:;/":
        text = text.replace(mark, "")

    return text.lower()


def count_words(text):
    """Count the words in the text."""
    cleaned = cleaned_text(text).split()
    return len(cleaned)


def count_characters_excluding_spaces(text):
    """Count characters without spaces or removed punctuation."""
    cleaned = cleaned_text(text).replace(" ", "")
    return len(cleaned)


def count_vowels_consonants(text):
    """Count vowels and consonants."""
    vowels = 0
    consonants = 0
    cleaned = cleaned_text(text)

    for letter in cleaned:
        if letter in "aeiou":
            vowels += 1
        elif letter.isalpha():
            consonants += 1

    return vowels, consonants


def find_longest_word(text):
    """Find the longest word."""
    words = cleaned_text(text).split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def most_frequent_word(text):
    """Count how often each word appears."""
    words = cleaned_text(text).split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def most_repeated_word(text):
    """Return words that appear more than once."""
    repeated_words = []
    frequency = most_frequent_word(text)

    for word, count in frequency.items():
        if count > 1:
            repeated_words.append(word)

    return repeated_words


def top_five_words(text):
    """Return up to five words with the highest frequencies."""
    frequency = most_frequent_word(text)

    sorted_words = sorted(
        frequency,
        key=lambda word: frequency[word],
        reverse=True
    )

    return sorted_words[:5]


def analyze_text(text):
    """Combine all text analysis results into one report."""
    vowels, consonants = count_vowels_consonants(text)

    report = {
        "Word count": count_words(text),
        "Character count (excluding spaces)": 
            count_characters_excluding_spaces(text),
        "Vowels": vowels,
        "Consonants": consonants,
        "Longest word": find_longest_word(text),
        "Word frequency": most_frequent_word(text),
        "Repeated words": most_repeated_word(text),
        "Top five words": top_five_words(text)
    }

    return report


if __name__ == "__main__":
    text = "Python is useful and Python is powerful."

    results = analyze_text(text)

    print("TEXT ANALYSIS REPORT")
    print("-" * 30)

    for label, result in results.items():
        print(f"{label}: {result}")
