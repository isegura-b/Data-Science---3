import pandas as pd
import sys
from pathlib import Path


EX05 = Path(__file__).resolve().parent


def main():
    # Comprobamos que nos pasen el CSV
    if len(sys.argv) != 2:
        print("Usage: python3 split.py Train_knight.csv")
        return

    # Leemos el archivo pasado por argumento
    file_path = Path(sys.argv[1])
    data = pd.read_csv(file_path)

    # Mezclamos las filas aleatoriamente
    data = data.sample(frac=1).reset_index(drop=True)

    # 80% para entrenamiento
    split_index = int(len(data) * 0.8)

    training = data[:split_index]
    validation = data[split_index:]

    # Guardamos los dos CSV
    training.to_csv(EX05 / "Training_knight.csv", index=False)
    validation.to_csv(EX05 / "Validation_knight.csv", index=False)

    print("Training:", len(training))
    print("Validation:", len(validation))


if __name__ == "__main__":
    main()