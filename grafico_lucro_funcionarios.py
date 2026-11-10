import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\patrick.araujo\OneDrive - SENAC-ARRJ\Documentos\Analista de dados\funcionarios.csv")

# 2. Inspeção rápida dos dados
print(df.head())
print(df.info())

# 3. Selecionar as colunas de interesse e ordenar pelo lucro
df_lucro = df[["nome", "lucro"]].sort_values("lucro", ascending=True)

# Funcionários sem lucro (0) ficam separados para não poluir o gráfico
sem_lucro = df_lucro[df_lucro["lucro"] == 0]
com_lucro = df_lucro[df_lucro["lucro"] > 0]

# 5. Criar o gráfico de barras horizontais


fig, ax = plt.subplots(figsize=(10, 7))

barras = ax.barh(com_lucro["nome"], com_lucro["lucro"],
                 color="#2a78d6", height=0.65)

# Rótulo de valor no fim de cada barra
for barra in barras:
    largura = barra.get_width()
    ax.text(largura + 300, barra.get_y() + barra.get_height() / 2,
            largura, va="center", fontsize=9, color="#52514e")

# 6. Títulos e eixos
ax.set_title("Lucro gerado por funcionário", fontsize=14,
             fontweight="bold", loc="left", pad=15)
ax.set_xlabel("Lucro (R$)", color="#52514e")
ax.set_xlim(0, com_lucro["lucro"].max() * 1.15)

# Grade discreta e remoção de bordas desnecessárias
ax.grid(axis="x", color="#e0e0e0", linewidth=0.8)
ax.set_axisbelow(True)
for lado in ["top", "right", "left"]:
    ax.spines[lado].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.tick_params(colors="#52514e")

plt.tight_layout(rect=(0, 0.04, 1, 1))

# 7. Salvar e exibir
plt.savefig("grafico_lucro_funcionarios.png", dpi=150)
plt.show()
