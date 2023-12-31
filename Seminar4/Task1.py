def print_sorted_words(text:str):
    words = text.split()
    words.sort()
    max_length = max([len(word) for word in words]) + 1
    for i, word in enumerate(words, start=1):
        print(f"{i} {word:>{max_length - len(str(i))}}")

print_sorted_words("This is a test string to check the function to check our possibilities")
