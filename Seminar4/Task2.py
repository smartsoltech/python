def unique_unicode_codes(text):
    unique_codes = sorted({ord(ch) for ch in text}, reverse=True)
    return unique_codes

print(unique_unicode_codes("This is a test string to check the function"))
