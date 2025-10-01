n = float(input("Digite o valor da sua primeira nota:"))
o = float(input("Digite o valor da sua segunda nota:"))
t = float(input("Digite o valor da sua terceira nota:"))
a = float(input("Digite o valor da sua quarta nota:"))
nota = (n + o + t + a)/4

print("Sua média é", nota)

if(nota >=80):
    print("Aluno aprovado!")
elif (nota >= 60):
    print("Aluno de recuperação")
else:
    print("Está reprovado")