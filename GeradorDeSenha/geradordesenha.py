import string
import random


def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Nenhum tipo de caractere selecionado para gerar a senha.")

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Gerador de Senhas")

    length = int(input("Digite o comprimento da senha: "))

    use_uppercase = input("Incluir letras maiúsculas? (sim/não): ").lower() == "sim"
    use_lowercase = input("Incluir letras minúsculas? (sim/não): ").lower() == "sim"
    use_digits = input("Incluir números? (sim/não): ").lower() == "sim"
    use_special = input("Incluir carcteres especial? (sim/não): ").lower() == "sim"

    try:
        password = generate_password(
            length, use_uppercase, use_lowercase, use_digits, use_special
        )
        print(f"Sua senha gerada é: {password}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
