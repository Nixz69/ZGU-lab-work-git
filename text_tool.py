def count_words(text):
    """Подсчитывает количество слов в тексте."""
    return len(text.split())

def longest_word(text):
    """Находит самое длинное слово в тексте."""
    words = text.split()
    return max(words, key=len) if words else None
