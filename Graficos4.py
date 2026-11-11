import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.loureiro\Documents\Aulas\funcionarios.csv")

df_lucro = df[df["lucro"] > 0]

xpoints = df_lucro["nome"]
ypoints = df_lucro["lucro"]

bars = plt.barh(xpoints, ypoints)

plt.bar_label(bars, fmt="%.2f", padding=3)

plt.title("Grafico")
plt.xlabel("Plano X")
plt.ylabel("Plano Y")

plt.show()