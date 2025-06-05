#2- Escreva um programa que calcule a velocidade média de um veículo com base na distância percorrida e no tempo em que uma viagem foi realizada.

#3 – Com base nos dados obtidos no programa anterior e sabendo que o veículo usado consome 12 Km/l, construa um programa que determine a quantidade de combustível gasto nessa viagem.

dist = float(input('Informe a distância percorrida em km: '))
tempo = float(input('Informe o tempo de viagem em horas: '))
velmedia = dist/tempo
consumo = dist/12

print(f'A velocidade média foi de {velmedia:.0f} km/h e o consumo de combustível foi de {consumo} litros')






