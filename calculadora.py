
def arithmetic_arranger(problems):

  num1 = 0
  num2 = 0
  signo = None

  for i in problems:
    data = i.split()
    num1 = int(data[0])
    num2 = int(data[2])
    signo = str(data[1]) 

    def verificarSigno(signo):
      if signo != "+":
        if signo != "-":
          raise TypeError("No es una suma o resta")
    verificarSigno(signo)

    def verificarNumero(num1, num2):
      if type(num1) != int:
        raise TypeError("num1 no es numero")
        if len(num1) > 4:
          raise TypeError("El numero es muy grande")
      if type(num2) != int:
        raise TypeError("num2 no es numero")
        if len(num1) > 4:
          raise TypeError("El numero es muy grande")
    verificarNumero(num1, num2)

    def operacion():
      print(" " , str(num1))
      print(signo, str(num2))
      print("----")
      if signo == "+":
        print(num1 + num2)
      else:
        print(num1 - num2)
    print("\n")
    operacion()

  arranged_problems = [num1, signo, num2]
  return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])