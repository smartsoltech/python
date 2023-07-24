def unique_unicode_codes(text):
    unique_codes = sorted({(i, ch, ord(ch)) for i, ch in enumerate(text)}, key=lambda x: x[2], reverse=True)
    return {i: [ch, code] for i, ch, code in unique_codes}

print(unique_unicode_codes("This is a test string to check the function"))
