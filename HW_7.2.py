# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import shuffle

def sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        sort(left)
        sort(right)

        i = j = k = 0
        left_s = len(left)
        right_s = len(right)

        while i < left_s and j < right_s:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < left_s:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < right_s:
            arr[k] = right[j]
            j += 1
            k += 1


array = [float(i) for i in range(0, 50)]
shuffle(array)
print(array)
sort(array)
print(array)
