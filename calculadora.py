while True: 
    num1 = float(input("digite o primeiro numero "))
    op = input("didite o operador ")
    num2 = float(input("digite o segundo numero "))
    opera={
'*': num1 * num2,
'+': num1 + num2,
'-': num1 - num2,
'/': num1 / num2
}
    resultado = opera.get(op)
    print("--------------------------------------------------")
    print("||\t\t\t",resultado,"\t\t\t||")
    print("--------------------------------------------------")

    reinicio = input("deseja reiniciar o programa ? (s/n): ")
    if reinicio.lower() != 's': 
        break 