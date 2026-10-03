import pandas as pd
from pathlib import Path


EX01 = Path(__file__).resolve().parent
SUBJECT = EX01.parent / "subject"
train = pd.read_csv(SUBJECT / "Train_knight.csv")


# Convertimos el target "knight" a valores numéricos
train["knight"] = train["knight"].map({
    "Sith": 0,
    "Jedi": 1
})

correlation = train.corr()["knight"]
correlation = correlation.sort_values(ascending=False)
print(correlation)