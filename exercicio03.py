n1 = float(input("Digite a 1º nota"))
n2 = float(input("Digite a 2º nota"))
n3 = float(input("Digite a 3º nota"))

media = (n1+n2+n3)/3

if media >= 7:
    print("Parabéns, Aluno Aprovado!")
    
else:
    if media >= 4:
        print("Recuperação!")
    else:
        print("Reprovado!")