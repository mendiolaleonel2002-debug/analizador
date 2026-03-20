from analyzer.text_analyzer import (
    count_words,
    count_characters,
    count_sentences,
    count_paragraphs,
    longest_word,
    longest_sentences,
    longest_paragraph
)

text = """
Hola mundo. Esta es una frase de prueba escrita directamente en la programacion.

Esta es una prueba de parrafo.

Esta es otra prueba de parrafo.
"""

print("Palabras:", count_words(text))
print("Caracteres:", count_characters(text))
print("Oraciones:", count_sentences(text))
print("Párrafos:", count_paragraphs(text))
print("Palabra mas larga:", longest_word(text))
print("Oración más larga:", longest_sentences(text))
print("Párrafo más largo:", longest_paragraph(text))