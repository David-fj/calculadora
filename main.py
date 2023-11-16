def stringforint(e, j, a):
    numberList = ""
    while (j >= 0 and j < len(e)) and (e[j] not in ['*', '/', '+', '-']):
        numberList += e[j]
        j += a
    if a < 0:
        numberList = numberList[::-1]
    return numberList, j

print("CALCULADORA")

print("Adição: +\nSubtração: -\nMultiplicação: *\nDivisão: /\n")

selection = input("Deseja realizar uma operação Matemática? [s] ou [n]: ")

while(selection == 's'):
    expression = input("Informe a expressão Matemática: ")
    preference = 1
    for j in range(2):
        i = 0 
        while i < len(expression):
            if preference:
                if expression[i] == '*' or expression[i] == '/':
                    esq = stringforint(expression, i-1, -1)
                    dir = stringforint(expression, i+1, 1)
                    if expression[i] == '*':
                        r = str(float(esq[0]) * float(dir[0]))
                    else:
                        r = str(float(esq[0]) / float(dir[0]))
                    expression = expression[:esq[1]+1] + r + expression[dir[1]:]
            else:
                if expression[i] == '+' or expression[i] == '-':
                    esq = stringforint(expression, i-1, -1)
                    dir = stringforint(expression, i+1, 1)
                    if expression[i] == '+':
                        r = str(float(esq[0]) + float(dir[0]))
                    else:
                        r = str(float(esq[0]) - float(dir[0]))
                    expression = expression[:esq[1]+1] + r + expression[dir[1]:]
            i += 1
        preference = 0
    print(expression)
    selection = input("Deseja realizar uma operação Matemática? [s] ou [n]: ")
