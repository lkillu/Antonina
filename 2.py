import random
import time

start_time = time.time()

array = [random.randint(1, 100) for _ in range(1000000)]

def selection_sort_descending(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

sorted_array = selection_sort_descending(array)

end_time = time.time()

print(f"Время сортировки выбором: {end_time - start_time:.5f} секунд")
print(sorted_array)
