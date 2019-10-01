# palindrome


def is_palindrome(text):
    reversetext = text[::-1]
    return reversetext.lower() == text.lower()


print(is_palindrome('Deleveled'))