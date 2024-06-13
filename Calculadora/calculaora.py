def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida"
    return x / y

def calculator():
    print("Selecione a operação:")
    print("1. Adição:")
    print("1. Subtração:")
    print("1. Multiplicação:")
    print("1. Divisão:")

    while True:
        choice = input("Digite sua escolha (1/2/3/4)")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("Deseja realizar outra operação? (sim/não): ")    
            if next_calculation.lower() != 'sim':
                break
    else:
        print("Opção inválida, por favor selecione uma operação válida (1/2/3/4).")  

if __name__ == "__main__":
    calculator()              
    
