import numpy as np
import matplotlib
matplotlib.use("Agg")          # lai varētu saglabāt failā bez loga; lokāli var izdzēst
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 13})

r = 1.3                        # L/D


# ---------------- Funkcija un atvasinājums ----------------
def f(x):
    return np.sinh(x) / x - r


def df(x):
    return (x * np.cosh(x) - np.sinh(x)) / x**2


# ---------------- BISEKCIJA ----------------
a, b = 1.0, 3.0
bis = []
for _ in range(60):
    c = (a + b) / 2
    bis.append(c)
    if f(a) * f(c) <= 0:
        b = c
    else:
        a = c


# ---------------- SEKANTE ----------------
x0, x1 = 1.0, 2.0
sec = []
for _ in range(12):
    if f(x1) == f(x0):         # jau sakonverģējis, izvairāmies no dalīšanas ar 0
        sec.append(x1)
        continue
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    sec.append(x2)
    x0, x1 = x1, x2


# ---------------- ŅŪTONS ----------------
x = 2.0
new = []
for _ in range(8):
    x = x - f(x) / df(x)
    new.append(x)


# ---------------- Precīzā vērtība (labākais rezultāts) ----------------
# 20 Ņūtona iterācijas no citas sākuma vērtības nekā galvenajā skrējienā
x_prec = 1.5
for _ in range(20):
    x_prec = x_prec - f(x_prec) / df(x_prec)


# ---------------- Rezultāti ----------------
print("Precīzais xi*  =", x_prec)
print("Bisekcija      =", bis[-1])
print("Sekante        =", sec[-1])
print("Ņūtons         =", new[-1])
print("a/L            =", 1 / (2 * r * x_prec))
print("h/L            =", (np.cosh(x_prec) - 1) / (2 * r * x_prec))


# ---------------- Kļūdas ----------------
EPS = 1e-17                    # apakšējā robeža log skalai
def err(xs):
    return np.maximum(np.abs(np.array(xs) - x_prec), EPS)

bis_error, sec_error, new_error = err(bis), err(sec), err(new)


# ---------------- Grafiks ----------------
plt.figure(figsize=(7, 4.5))
plt.semilogy(range(1, len(bis) + 1), bis_error, "o-", ms=4, label="Bisekcija")
plt.semilogy(range(1, len(sec) + 1), sec_error, "s-", ms=4, label="Sekante")
plt.semilogy(range(1, len(new) + 1), new_error, "^-", ms=4, label="Ņūtons")
plt.xlabel("Iterāciju skaits $k$")
plt.ylabel(r"$|\xi_k-\xi^*|$")
plt.title("1. att. Metožu konverģence")
plt.ylim(1e-17, 10)
plt.grid(True, which="both", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("konvergence.png", dpi=200)
plt.show()