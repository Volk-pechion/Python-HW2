#Задача 1: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) 


N = int(input('Введите число N: '))
summa_list = list(range(1, N+1))
factor = 1
for i in range(N):
        factor = factor * summa_list[i]
        summa_list[i]=factor
print(summa_list)
