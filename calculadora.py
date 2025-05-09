#Variables
while True:
    numero1= float(input(""))
    operador= input("")
    if operador == "Exit":
        break
    numero2= float(input(""))

    #Operaciones
    if operador == "+":
        operacion= numero1+numero2
        print(operacion)
    elif operador == "-":
        operacion= numero1-numero2
        print(operacion)
    elif operador == "x":
        operacion= numero1*numero2
        print(operacion)
    elif operador == "/":
        operacion= numero1/numero2
        print(operacion)
    elif operador == "D":
        print()
    else:
        print("Error")
