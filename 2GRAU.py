print("### Olá ###")
print("Versão 1.0")
while True:
    print("### Menu ###")
    print("")
    print("1-Resolver")
    print("2-Criar")
    V1 = input("Selecione Qual:")
    if V1=="1":
        print("")
        print("A formula utilizada para a equação de segundo grau é ax²+bx+c=0")
        print("Portando 'A' não pode ser 0")
        while True:
         A=int(input("Insira o valor de A: "))
         if A==0:
           print("")
           print("### 'A' não pode ser 0 ###")
           print("")
           continue
         else:
            break
        B=int(input("Insira o valor de B: "))
        C=int(input("Insira o Valor de c: "))
        D1 = B**2 - 4*A*C
        X1 = (-B+D1**0.5)/(2*A)
        X2 = (-B-D1**0.5)/(2*A)
        print("")
        print("")
        print(f"Seu delta é igual a {D1}")
        print(f"A fórmula do seu delta é {B}²-4.{A}.{C}")
        print("")
        print("A sua Fórmula de bhaskara é")
        print(f"\033[4m-{B} +/- {D1**0.5}\033[0m")
        print(f"    {A*2}")
        print("")
        print(f"Seu X1 é {-B+D1**0.5}/{A*2} logo {X1}")
        print(f"Seu X2 é {-B-D1**0.5}/{A*2} Logo {X2}")
        print("")
        while True:
         V2=input("Digite Y para voltar ao menu")
         if V2=="y" or V2=="Y":
            break
         else:
            continue        
    elif V1 == "2":
       print("")
       V3 = input("Deseja completa? y/n: ")
       if V3 == "y" or V3 == "Y":
            while True:
             import random
             A2 = random.randint(1, 99)
             B2 = random.randint(1, 99)
             C2 = random.randint(1, 99)
             D2 = B2**2-4*A2*C2
             N1 = D2**0.5
             if D2 >= 0 and N1 == int(N1):
                X1=(-B2+N1)/(2*A2)
                X2=(-B2-N1)/(2*A2)
                if X1 == int(X1) and X2 == int(X2):
                   break
                else:
                   None
            print("")
            print("Sua equação é:")
            print(f"{A2}x²+{B2}x+{C2}=0")
            print(f"Seu delta é {D2}")
            print(f"Suas raízes são {X1} e {X2}")
            print("")
            V5=input("Deseja ir para o menu? Y:")
            if V5 == "Y" or V5 == "y":
              continue
       elif V3 == "n" or V3 == "N":
          print("Sabendo que na equação Ax²+Bx+C=0")
          print("A não pode ser igual a 0")
          V6 = input("Deseja zerar C ou B? ")
          if V6 == "c" or V6 == "C":
             while True:
                import random
                A3 = random.randint(1, 99)
                B3 = random.randint(1, 99)
                C3 = 0
                D3 = B3**2-4*A3*C3
                N2 = D3**0.5
                if D3 >= 0 and N2 == int(N2):
                   X1=(-B3+N2)/(2*A3)
                   X2=(-B3-N2)/(2*A3)
                   if X1 == int(X1) and X2 == int(X2):
                      break
                   else:
                      None
             print("")
             print("Sua equação é:")
             print(f"{A3}x²+{B3}x+{C3}=0")
             print(f"Seu delta é {D3}")
             print(f"Suas raízes são {X1} e {X2}")
             print("")
             V5=input("Deseja ir para o menu? Y:")
             if V5 == "Y" or V5 == "y":
              continue
          elif V6 == "b" or V6 == "B":
             while True:
                import random
                A4 = random.randint(1, 99)
                B4 = 0
                C4 = random.randint(-99, -1)
                D4 = B4**2-4*A4*C4
                N3 = D4**0.5
                if D4 >= 0 and N3 == int(N3):
                   X1 = (-B4+N3)/(2*A4)
                   X2 = (-B4-N3)/(2*A4)
                   if X1 == int(X1) and X2 == int(X2):
                      break
                   else:
                      None
             print("")
             print("Sua equação é:")
             print(f"{A4}x²+{B4}x{C4}=0")
             print(f"Seu delta é {D4}")
             print(f"Suas raízes são {X1} e {X2}")
             print("")
             V6=input("Deseja ir para o menu? Y:")
             if V6 == "y" or V6 == "Y":
                continue