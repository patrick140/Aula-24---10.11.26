import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.loureiro\Documents\Aulas\funcionarios.csv")

df_lucro = df[df["lucro"] > 0]

xpoints = df_lucro["nome"]
ypoints = df_lucro["lucro"]

plt.barh(xpoints, ypoints)

plt.title("Grafico")
plt.xlabel("Plano X")
plt.ylabel("Plano Y")

plt.show()