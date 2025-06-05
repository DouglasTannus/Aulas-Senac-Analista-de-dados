#2- Faça um programa que receba do usuário o nome e a idade de 10 pessoas. Ao final mostre a soma e a média das idades.
#3- Utilizando a estrutura do programa anterior, identifique o nome da pessoa mais velha.

soma=0
maior_idade=0
menor_idade=200

for i in range(3):
    nome=input("Informe o nome do usuário: ")
    idade=int(input('Informe a idade do usuário: '))
    soma=soma+idade
    if idade>maior_idade:
        maior_idade=idade
        maior_nome=nome
    if idade<menor_idade:
        menor_idade=idade
        menor_nome=nome

print(f"A soma das idades foi {soma}")
print(f"A média das idades foi {soma/(i+1):.2f}")
print(f'A maior idade é {maior_idade}')
print(f'O nome do mais velho é {maior_nome}')
print(f'A menor idade é {menor_idade}')
print(f'O nome do mais velho é {menor_nome}')









