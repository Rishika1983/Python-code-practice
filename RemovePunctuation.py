# Remove punctuation from string. Replace punctation with blank space


def remove_punctuation(input_str):
    punctuation = '''!@#$%^&*()£_{}[]|:;"'?<>.,'''
    new_str = input_str
    for s in input_str:
        if s in punctuation:
            new_str = new_str.replace(s,' ')
    return new_str


input_str = input('Enter your text')
new_str = remove_punctuation(input_str)
print(new_str)
