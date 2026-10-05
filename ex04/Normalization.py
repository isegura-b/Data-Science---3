import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


EX04 = Path(__file__).resolve().parent
SUBJECT = EX04.parent / "subject"

train = pd.read_csv(SUBJECT / "Train_knight.csv")
test = pd.read_csv(SUBJECT / "Test_knight.csv")


# NORMALIZATION
knight = train["knight"]
train_features = train.drop(columns=["knight"])


# Normalizamos Train entre 0 y 1
train_normalized = (
    train_features - train_features.min()
) / (
    train_features.max() - train_features.min()
)


# Normalizamos Test entre 0 y 1
test_normalized = (
    test - test.min()
) / (
    test.max() - test.min()
)


# Volvemos a añadir el target
train_normalized["knight"] = knight


print("TRAIN NORMALIZED:")
print(train_normalized)

print("\nTEST NORMALIZED:")
print(test_normalized)


# GRAPH

# Separamos Jedi y Sith
jedi = train_normalized[
    train_normalized["knight"] == "Jedi"
]

sith = train_normalized[
    train_normalized["knight"] == "Sith"
]


# Usamos EL OTRO gráfico del ex02
plt.scatter(
    jedi["Midi-chlorien"],
    jedi["Deflection"],
    label="Jedi",
    alpha=0.6
)

plt.scatter(
    sith["Midi-chlorien"],
    sith["Deflection"],
    label="Sith",
    alpha=0.6
)

plt.xlabel("Midi-chlorien")
plt.ylabel("Deflection")
plt.title("Normalized data")
plt.legend()

plt.tight_layout()

plt.savefig(EX04 / "normalized.png")
plt.show()
plt.close()