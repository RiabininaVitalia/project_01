# Задача 3.1.
# Создайте класс матрицы (или таблицы)

#    существуют следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.
import random

class Matrix:
    
    def create_matrix():
        """Задаем параметры матрицы"""
        r = 0
        N = int(input('Ведите количество строк матрицы: '))
        M = int(input('Ведите количество столбцов матрицы: '))
        array = []
        for i in range(N):
            array.append([])
            for j in range(M):
                array[i].append(random.randint(0,100))
                r += 1
        print(array)  
        return array    
   
    def add_matrix():
        """Принять новое значение"""
        m = Matrix.create_matrix()
        for i in range(len(m)):
            n = 0
            for j in m[i]:
               if j == 0:
                  m[i][n] = random.randint(1,9)
                  print(' ')
                  print(f"В строке под индексом {i} значение под индексом {n} заменено")
                  n +=1
               else:
                  n+=1  
        print('') 
        print(m) 

    def change_matrix():
        """Заменить объект в матрице"""
        m = Matrix.create_matrix()
        x = int(input('Ведите индекс строки матрицы: '))
        y = int(input('Ведите индекс столбца матрицы: '))
        n = int(input('Ведите новое число: '))
        m[x][y] = n
        print('В ячейке', x, y, 'элемент заменен на ', n)
        print(m)

    def size_matrix():
        """Узнать размер матрицы""" 
        m = Matrix.create_matrix()
        x = len(m)
        y = len(m[0])
        print ('Количество строк равно:', x)
        print ('Количество столбцов равно:', y)



Matrix.create_matrix()