from analyzer.text_analyzer import (
    count_words,
    count_characters,
    count_sentences,
    longest_word
)

text = "Hola mundo, esta es una frase de prueba escrita directamente en el codigo."

print(f"Palabras:", count_words(text))
print(f"Caracteres:", count_characters(text))
print(f"Oraciones:", count_sentences(text))
print(f"Palabra mas larga:", longest_word(text))
