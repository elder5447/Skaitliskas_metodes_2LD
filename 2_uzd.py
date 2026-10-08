import numpy as np
import matplotlib.pyplot as plt

# Bezdimensiju koordināta u = x/a, funkcija f(u) = y/a = cosh(u) - 1
u = np.linspace(-2, 2, 100)
h = u[1] - u[0]

def f(u):
    return np.cosh(u) - 1

def deriv3(f, h):
    return lambda u: (f(u + h) - f(u - h)) / (2*h)

def deriv5(f, h):
    return lambda u: (-f(u + 2*h) + 8*f(u + h) - 8*f(u - h) + f(u - 2*h)) / (12*h)

d2f_exact = np.cosh(u)

d2f_3 = deriv3(deriv3(f, h), h)
d2f_5 = deriv5(deriv5(f, h), h)

floor = 1e-17
err_3 = np.maximum(np.abs(d2f_3(u) - d2f_exact), floor)
err_5 = np.maximum(np.abs(d2f_5(u) - d2f_exact), floor)

fig, ax = plt.subplots(figsize=(8, 5))
ax.semilogy(u, err_3, label="3 punktu formula")
ax.semilogy(u, err_5, label="5 punktu formula")

ax.set_xlabel(r"$u = x/a$", fontsize=14)
ax.set_ylabel(r"$a\,|y''_{\mathrm{skait.}} - y''_{\mathrm{prec.}}|$", fontsize=14)
ax.grid(True, which="both", alpha=0.3)
ax.legend(fontsize=14)

fig.tight_layout()
plt.savefig("2.uzd.png")
plt.show()