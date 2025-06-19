import numpy as np
import matplotlib.pyplot as plt

# Fungsi Regula Falsi
def f_regula(x):
    return x**3 - x - 2

def regula_falsi(a, b, tol=1e-6, max_iter=100):
    if f_regula(a) * f_regula(b) >= 0:
        print("Metode gagal: f(a) dan f(b) harus berbeda tanda.")
        return None, []

    steps = []
    print(f"{'Iterasi':<8} {'a':<10} {'b':<10} {'c':<15} {'f(c)':<15}")
    print("-" * 60)
    
    for i in range(1, max_iter + 1):
        c = b - (f_regula(b)*(a - b))/(f_regula(a) - f_regula(b))
        fc = f_regula(c)
        steps.append((c, fc))
        print(f"{i:<8} {a:<10.6f} {b:<10.6f} {c:<15.10f} {fc:<15.10f}")
        
        if abs(fc) < tol:
            break
        if f_regula(a) * fc < 0:
            b = c
        else:
            a = c
    return c, steps

akar, iterasi = regula_falsi(1, 2)

# Plot hasil Regula Falsi
x = np.linspace(0, 3, 400)
y = f_regula(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="f(x) = x³ - x - 2")
plt.axhline(0, color='black', linewidth=0.5)
for step in iterasi:
    plt.plot(step[0], step[1], 'ro')
plt.title("Grafik Fungsi dan Titik Iterasi Regula Falsi")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()