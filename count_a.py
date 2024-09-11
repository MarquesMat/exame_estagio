# Exercício 2

import unicodedata # Esta biblioteca permite remover os acentos das letras

# Verifica cada letra da sentença, contando a quantidade de 'a' e 'A'
def counter(sentence):
    lowercase = 0
    uppercase = 0
    for letter in sentence:
        if letter == 'a':
            lowercase += 1
        elif letter == 'A':
            uppercase += 1
    return lowercase, uppercase

sentence = input("Digite uma sentença (palavra ou frase): ")
lower, upper = counter(unicodedata.normalize('NFKD', sentence)) # Passa a sentença sem os acentos
print(f"\nAnálise da sentença: {sentence}")
print(f"Quantidade de 'a': {lower}")
print(f"Quantidade de 'A': {upper}")
print(f"Total ('a' + 'A'): {lower + upper}")
