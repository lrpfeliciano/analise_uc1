"""
1) Faça um programa que executará a conversão 
de temperaturas Celsius para Fahrenheit 
começando em 10 graus celsius até 60 graus 
celsius, saltando de 5 em 5 graus.
A fórmula da conversão é F = 9C / 5 + 32 
"""
for c in range(10,61,5):
    f = 9 * c / 5 + 32
    print(f'{c}°C equivale a {f}F')