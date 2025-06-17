def f(x):
    return x**3 - x - 2

def regula_falsi(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Metode gagal: f(a) dan f(b) harus berbeda tanda")
        return None

    for i in range(max_iter):
        c = b - (f(b)*(a - b))/(f(a) - f(b))
        print(f"Iterasi {i+1}: c = {c}, f(c) = {f(c)}")
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

akar = regula_falsi(1, 2)
print("Akar pendekatan:", akar)