import numpy as np

def regress(y):
    w = [0.0, 0.0, 0.0]
    result = [0.0, 0.0, 0.0]
    eta = 0.001
    sum_do = 0
    sum_posle = 0
    sum_do_do = 100000

    for j in range(100000):
        for i in range(len(y)):
            delta = y[i] - (w[1] * i + w[0])
            d = 1 if delta > 0 else -1
            w[0] += eta * d
            w[1] += eta * d * i
            sum_posle += int(delta ** 2)

        w[2] += 1

        # Проверяем условие минимизации ошибки
        if sum_do == sum_posle and sum_do_do > sum_posle:
            sum_do_do = sum_do
            result = w.copy()  # Копируем текущее значение w в result

        sum_do = sum_posle
        sum_posle = 0

    print("Sum Do Do:", sum_do_do)
    print("Result:", result)
    return result
