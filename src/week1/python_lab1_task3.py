def analyze_sentence(text: str) -> tuple[int, int, bool]:
    characters = len(text)
    words = len(text.split())
    has_python = "python" in text.lower()
    return characters, words, has_python


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    characters, words, has_python = analyze_sentence(sentence)
    print(f"Characters: {characters}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {has_python}")
