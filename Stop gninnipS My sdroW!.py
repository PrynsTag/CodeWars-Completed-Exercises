def spin_words(sentence):
    return ' '.join([word if len(word) < 5 else word[::-1] for word in sentence.split()])


if __name__ == '__main__':
    print(spin_words("Welcome") == "emocleW")