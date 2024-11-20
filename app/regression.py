import numpy as np

def regress(y):
    # Инициализация весов w:
    # w[0] — свободный член,
    # w[1] — коэффициент наклона,
    # w[2] — счётчик итераций (используется как индикатор завершения работы).
    w = [0.0, 0.0, 0.0]

    # Переменная для хранения результатов регрессии (копия весов w)
    result = [0.0, 0.0, 0.0]

    # Шаг обучения (скорость изменения весов)
    eta = 0.001

    # Суммы ошибок для анализа прогресса
    sum_do = 0         # Ошибка на предыдущей итерации
    sum_posle = 0      # Ошибка на текущей итерации
    sum_do_do = 100000 # Минимальная ошибка, зафиксированная за всё время

    # Цикл оптимизации (до 100,000 итераций)
    for j in range(100000):
        # Перебираем все точки данных
        for i in range(len(y)):
            # Вычисляем разницу между фактическим значением y[i] и предсказанным
            delta = y[i] - (w[1] * i + w[0])
            # Определяем направление изменения весов (положительное или отрицательное)
            d = 1 if delta > 0 else -1
            # Обновляем веса:
            # w[0] — сдвиг прямой
            # w[1] — наклон прямой
            w[0] += eta * d
            w[1] += eta * d * i
            # Накапливаем квадрат ошибки для текущей итерации
            sum_posle += int(delta ** 2)

        # Увеличиваем счётчик итераций
        w[2] += 1

        # Проверяем, удалось ли уменьшить ошибку
        if sum_do == sum_posle and sum_do_do > sum_posle:
            # Если ошибка уменьшилась, сохраняем минимальное значение
            sum_do_do = sum_do
            # Копируем текущие веса в результат
            result = w.copy()

        # Подготовка к следующей итерации:
        # Сохраняем текущую сумму ошибок для анализа на следующем шаге
        sum_do = sum_posle
        # Сбрасываем сумму ошибок для новой итерации
        sum_posle = 0

    print("Sum Do Do:", sum_do_do)
    print("Result:", result)
    return result
