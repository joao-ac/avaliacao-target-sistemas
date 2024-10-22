def contar_letra_a(texto):
    # Contar a ocorrência da letra 'a' e 'A'
    contador = texto.lower().count('a')

    # Verifica se a letra 'a' foi encontrada
    if contador > 0:
        print(f"A letra 'a' (ou 'A') aparece {contador} vez(es) na string.")
    else:
        print("A letra 'a' (ou 'A') não foi encontrada na string.")

# Solicita ao usuário uma string
string_usuario = input("Digite uma string: ")

# Chama a função para contar as letras 'a'
contar_letra_a(string_usuario)

# Aguarda o pressionamento de uma tecla antes de fechar
input("Pressione Enter para fechar...")
