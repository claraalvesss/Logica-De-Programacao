salario = float(input("Digite o salário do colaborador: "))

if salario<=280:
  percentualaumento = 20

elif salario <= 700:
  percentualaumento = 15

elif salario <= 1500:
 percentualaumento =10

else:
  percentualaumento = 5

aumento= salario * (percentualaumento/100)
novosalario = salario + aumento

print(f"O salário antes do reajuste era de: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentualaumento}%")
print(f"O valor do aumento foi de: R$ {aumento:.2f}")
print(f" O novo salário após o aumento será de: R$ {novosalario:.2f}")