def fibonacci_check(num):
    a, b = 0, 1

    # Se o número for 0 ou 1, ele pertence à sequência
    if num == 0 or num == 1:
        return True

    # Calcula a sequência de Fibonacci até o número informado
    while b <= num:
        if b == num:
            return True
        # Atualiza os valores
        a, b = b, a + b

    return False

# Solicita ao usuário um número
number = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if fibonacci_check(number):
    print(f"{number} pertence à sequência de Fibonacci.")
else:
    print(f"{number} não pertence à sequência de Fibonacci.")

# Aguarda o pressionamento de uma tecla antes de fechar
input("Pressione Enter para fechar...")
