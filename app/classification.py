def classification(x, y, metka):
    eta = 0.1
    w = [0, 0, 0]
    metka = [1 if m == 1 else -1 for m in metka]

    for j in range(10000):
        count = 0
        for i in range(len(x)):
            otvet = w[1] * x[i] + w[2] * y[i] + w[0]
            met_otvet = 1 if otvet > 0 else -1
            if met_otvet != metka[i]:
                delta = metka[i] - met_otvet
                w[0] += eta * delta
                w[1] += eta * delta * x[i]
                w[2] += eta * delta * y[i]
                count += 1
        if count == 0:
            return w
    w[2] = 0
    return w
