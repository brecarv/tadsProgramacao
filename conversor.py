print("1- Decimal -> IEEE754 2- IEEE754 -> Decimal")
opcao = int(input())

if opcao == 1:
    num = float(input())

    if num > 0:
        sinal = '0'
    else:
        sinal = '1'

    num = abs(num)

    if num >= 2:
        cont = 0

        while num > 2:
            num /= 2
            cont += 1

        expoente = bin(cont + 127).split("0b")[1]
    #    expoente2 = "{0:b}".format(cont + 127)
    else:
        cont = 0

        while num < 1:
            num *= 2
            cont -= 1

        expoente = '0' + bin(cont + 127).split("0b")[1]
    #    expoente2 = '0' + "{0:b}".format(cont + 127)

    cont = 0
    mantissa = ''
    fracionaria = num % 1
    decimal = num / 1

    while cont < 23:
        num = round(fracionaria * 2, 8) + 0.0000001
        fracionaria = num % 1
        decimal = num // 1
        mantissa += str(decimal)[0]
        cont += 1

    final = sinal + expoente + mantissa
    print("Final:", final)

else:
    binario = input()

    sinal = int(binario[0])
    expoente = binario[1:9]
    mantissa = binario[9:32]

    fracao = 0.00
    final = 0

    expoenteReal = int(expoente, 2) - 127

    for cont in range(1, 24):
        aux = int(mantissa[cont - 1])
        if aux > 0:
            fracao += 1 / (2 ** cont)

    fracao += 1

    if sinal == 1:
        final = -1 * fracao * float(2 ** expoenteReal)
    else:
        final = fracao * float(2 ** expoenteReal)

    print("%.6f" % final)
