import re

someArray = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def function(text, someArray):
    number = re.findall(r'\d+', text)
    if len(number) == 1:
        n = int(number[0])
    elif len(number) == 3:
        n = int(number[0])
        b = int(number[1])
        v = int(number[2])
    else:
        result = "Числа в тексте отсутствуют."

    target_word1 = "индексу"
    target_word2 = "шагом"
    target_word3 = "конца"

    l = len(someArray)
    
    if target_word1 in text:
        if 1 <= n <= len(someArray):
            nth_element = someArray[n - 1]
            result = f"{n}-й элемент массива: {nth_element}"
        else:
            result = f"Ошибка: значение вне диапазона. Длина массива {l}"

    elif target_word2 in text:
        if 1 <= n <= len(someArray):
            elements_arr = someArray[n - 1:b:v]
            elements = ', '.join(map(str, elements_arr))
            result = f"Элементы массива с {n} по {b} с шагом {v}: {elements}"
        else:
            result = f"Ошибка: значения вне диапазона. Длина массива {l}"

    elif target_word3 in text:
        if 1 <= n <= len(someArray):
            nth_eft_end = someArray[len(someArray) - n]
            result = f"{n}-й элемент массива с конца: {nth_eft_end}"
        else:
            result = f"Ошибка: значение вне диапазона. Длина массива {l}"

    else:
            result = "Ошибка: команда не распознана"
    return result

print(function(input("Введите команду: "), someArray))
