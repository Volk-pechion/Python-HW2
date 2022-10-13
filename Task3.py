#Задача 3: Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
#   Пример списка ИНДЕКСОВ [2, 4, 3, 1, 8]
    #Ввод: 10
    #[-10, -9, ...-4, -3, -2, -1, 0, 1, 2, 3,4....10]

N = int(input('Введите число N: '))
numbers_list =(list(range(-N,N+1)))
index_list = [3, 5, 2, 1, 4]
new_list = index_list
print(numbers_list)
print(index_list)
print(f'Старый список: {new_list}')
s=0
for i in range(-N,N+1):
            s = index_list[i] * numbers_list[i]
            new_list[i] = s
print(f'Новый список: {new_list}')