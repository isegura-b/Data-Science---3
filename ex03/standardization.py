import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


EX03 = Path(__file__).resolve().parent
SUBJECT = EX03.parent / "subject"

train = pd.read_csv(SUBJECT / "Train_knight.csv")
test = pd.read_csv(SUBJECT / "Test_knight.csv")


# STANDARDIZATION
knight = train["knight"]
train_features = train.drop(columns=["knight"])


# Estandarizamos Train
train_standardized = ( train_features - train_features.mean()) / train_features.std()
# Estandarizamos Test
test_standardized = ( test - test.mean()) / test.std()


train_standardized["knight"] = knight

print("TRAIN STANDARDIZED:")
print(train_standardized)

print("\nTEST STANDARDIZED:")
print(test_standardized)


# GRAPH

# Separamos Jedi y Sith
jedi = train_standardized[
    train_standardized["knight"] == "Jedi"
]
sith = train_standardized[
    train_standardized["knight"] == "Sith"
]


plt.scatter(
    jedi["Empowered"],
    jedi["Stims"],
    label="Jedi",
    alpha=0.6
)
plt.scatter(
    sith["Empowered"],
    sith["Stims"],
    label="Sith",
    alpha=0.6
)

plt.xlabel("Empowered")
plt.ylabel("Stims")
plt.title("Standardized data")
plt.legend()

plt.tight_layout()

plt.savefig(EX03 / "standardized.png")
plt.show()
plt.close()