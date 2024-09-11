# Exercício 1

# Função recursiva para calcular a sequência de Fibonacci
def calc_fibonacci(x, y, stop): # x e y = últimos números da sequência; stop = número procurado
    next = x + y
    print(f"-> {next} ", end="")
    if next == stop: # Encontrou o número procurado
        print(f"\nO número {stop} pertence à sequência de Fibonacci!")
    elif next > stop: # Passou do número procurado sem encontrá-lo
        print(f"\nO número {stop} NÃO pertence à sequência de Fibonacci!")
    else: # Ainda não chegou no número procurado
        calc_fibonacci(y, next, stop)

# Este loop verifica se o dado inserido é um número inteiro
while True:
    try:
        num = int(input("Insira um número inteiro qualquer para verificar se ele está na sequência de Fibonacci: "))
        break # Sai do loop se a entrada de dado estiver correta
    except ValueError: # Exceção ao não reconhecer a entrada como um número inteiro
        print(f"Entrada inválida! Por favor, inserir um número inteiro.")

print("Calculando a sequência...")
print("-> 0 -> 1 ", end="")
calc_fibonacci(0, 1, num)
