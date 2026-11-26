from pathlib import Path
import duckdb

DATA_DIR = Path("data")
DB_PATH = "fleetsense.duckdb"


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    csv_files = list(DATA_DIR.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in data/.")
        return

    connection = duckdb.connect(DB_PATH)

    for file in csv_files:
        print(f"Found file: {file.name}")

    connection.close()


if __name__ == "__main__":
    main()
