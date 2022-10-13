# Задача 4: Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

N = int(input('Введите число N: '))
numbers_list = list(range(1,N+1))
summa = 0
for i in range(N):
    if numbers_list[i]%2==0:
        summa = numbers_list[i]+summa
print(f"Рассматриваемый список: {numbers_list} ")
print(f'Сумма четных чисел: {summa}')
