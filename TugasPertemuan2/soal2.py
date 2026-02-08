def bilangan_prima(n):
    prima = []
    for i in range(2, n + 1):
        is_prima = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prima = False
                break
        if is_prima:
            prima.append(i)
    return prima

hasil_prima = bilangan_prima(50)
print("Bilangan prima 1 sampai 50:")
print(hasil_prima)