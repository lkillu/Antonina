def f(b,c):
    a=int(input("Введите число a: "))
    if a<0:
        return -1
    else:
        return max(a,b,c)
print("Результат функции: ", f(10,5))
