import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


EX00 = Path(__file__).resolve().parent
# Carpeta donde están los CSV
SUBJECT = EX00.parent / "subject"

test = pd.read_csv(SUBJECT / "Test_knight.csv")
train = pd.read_csv(SUBJECT / "Train_knight.csv")

# TEST_KNIGHT

# Creamos un histograma para cada feature de Test_knight.csv
test.hist(bins=30, figsize=(15, 12))
plt.tight_layout()

plt.savefig(EX00 / "test_histograms.png")
plt.show()
plt.close()


# TRAIN_KNIGHT

# Todas las columnas excepto "knight" son las features
features = train.columns[:-1]

# Separamos los datos según el target "knight"
jedi = train[train["knight"] == "Jedi"]
sith = train[train["knight"] == "Sith"]

fig, axes = plt.subplots(6, 5, figsize=(15, 12))
axes = axes.flatten()

# Creamos un histograma para cada feature
for i, feature in enumerate(features):

    axes[i].hist(
        jedi[feature],
        bins=30,
        alpha=0.5,
        label="Jedi"
    )

    axes[i].hist(
        sith[feature],
        bins=30,
        alpha=0.5,
        label="Sith"
    )

    axes[i].set_title(feature)
    axes[i].legend()


plt.tight_layout()

plt.savefig(EX00 / "train_histograms.png")
plt.show()
plt.close()