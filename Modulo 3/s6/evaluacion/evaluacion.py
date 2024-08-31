

entrada = input("Introduce tres números separados por un espacio")

numeros = list(map(int, entrada.split()))

numeros.sort(reverse=True)

print(f"Números ordenados de mayor a menor: {numeros}")