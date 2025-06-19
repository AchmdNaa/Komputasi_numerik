import numpy as np
import matplotlib.pyplot as plt

# Fungsi yang akan diintegrasikan
def f_romberg(x):
    return np.sin(x)

# Aturan Trapezoida
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    sum_val = 0.5 * (f_romberg(a) + f_romberg(b))
    for i in range(1, n):
        sum_val += f_romberg(a + i * h)
    return h * sum_val

# Fungsi Romberg
def romberg_integration(a, b, max_order):
    R = np.zeros((max_order, max_order))
    for i in range(max_order):
        n = 2**i
        R[i, 0] = trapezoidal_rule(a, b, n)
        for k in range(1, i + 1):
            R[i, k] = (4**k * R[i, k - 1] - R[i - 1, k - 1]) / (4**k - 1)
    return R

# Parameter
a = 0
b = np.pi
max_order = 4
nilai_eksak = 2.0

# Hitung tabel Romberg
R = romberg_integration(a, b, max_order)

# Perbandingan Trapezoida vs Romberg
print(f"\n{'Orde':<6} {'Interval':<10} {'Trapezoida':<15} {'Romberg':<15} {'Error Trap':<15} {'Error Romberg':<15}")
print("-" * 80)

errors_romberg = []
errors_trap = []

for i in range(max_order):
    n = 2**i
    trap = trapezoidal_rule(a, b, n)
    romb = R[i, i]
    err_trap = abs(trap - nilai_eksak)
    err_romb = abs(romb - nilai_eksak)

    errors_trap.append(err_trap)
    errors_romberg.append(err_romb)

    print(f"{i+1:<6} {n:<10} {trap:<15.10f} {romb:<15.10f} {err_trap:<15.10f} {err_romb:<15.10f}")

# Plot grafik error Romberg dan Trapezoida
orders = np.arange(1, max_order + 1)

plt.figure(figsize=(8, 5))
plt.plot(orders, errors_trap, marker='o', linestyle='--', color='red', label="Error Trapezoida")
plt.plot(orders, errors_romberg, marker='o', color='green', label="Error Romberg")
plt.title("Perbandingan Error Trapezoida vs Romberg")
plt.xlabel("Orde (n = 2^i)")
plt.ylabel("Error terhadap Nilai Eksak")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()