def q_exemplo():
    n = int(input(""))
    for i in range(0, n+1) :
        if i>1 and i % 2 == 0:
            print(i)

def q1():
    n1 = int(input(""))
    n2 = int(input(""))
    n3 = int(input(""))
    numeros_ordenados = sorted([n1, n2, n3])
    for n in numeros_ordenados:
        print(n)
    

def q2():
    dias = int(input(""))
    quilometragem_total = float(input(""))
    # Valor da diária
    valor_diaria = 90
    # Cota de quilometragem por diária
    quilometragem_cota = 100
    # Taxa extra por quilômetro adicional
    taxa_extra_por_km = 12
    # Cálculo do valor da diária
    valor_diarias = dias * valor_diaria
    # Chamada da função para calcular o valor total
    quilometragem_excedente = max(0, quilometragem_total - (dias * quilometragem_cota))

    # Cálculo do valor adicional por quilometragem
    valor_adicional_km = quilometragem_excedente * taxa_extra_por_km

    # Cálculo do valor total a ser pago
    valor_total = valor_diarias + valor_adicional_km

    # Impressão do valor total com duas casas decimais
    print(f"{valor_total:.2f}")

def q3():
    n = int(input(""))
    for i in range(1, n + 1):
        for j in range(1, i + 1 ):
            print(j, end=' ')
        print()

def q4():
    pass

def main():
    q_exemplo()

if __name__ == "__main__":
    main()