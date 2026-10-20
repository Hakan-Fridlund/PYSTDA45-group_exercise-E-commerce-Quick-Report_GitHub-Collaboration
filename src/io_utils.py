
# Användning i en annan Python-fil:
# from src.io_utils import load_data
# df = load_data("data/ecommerce_sales.csv")


import pandas as pd


def load_data(filepath):
    data = pd.read_csv(filepath, encoding="utf-8")

    # Kontrollera och korrigera datatyper (t.ex. se till att price och revenue är numeriska.
    data["price"] = pd.to_numeric(data["price"], errors="coerce")
    data["units"] = pd.to_numeric(data["units"], errors="coerce")
    data["revenue"] = pd.to_numeric(data["revenue"], errors="coerce")
    data["date"] = pd.to_datetime(data["date"], errors="coerce")

    # Hantera saknade/tomma värden (t.ex. droppa rader som saknar kritiska värden eller fyll i dem på ett rimligt sätt).
    data = data.dropna(
        subset=["order_id", "date", "city", "category", "price", "units"]
    )

    # Kontrollera att revenue stämmer överens med units * price så att det inte finns korrupta beräkningar i källfilen.
    data["revenue"] = (data["units"] * data["price"]).round(2)

    return data


# Testar om allting fungerar
if __name__ == "__main__":

     # Läs originalfilen utan att städa den
    original = pd.read_csv("data/ecommerce_sales.csv")

    # Läs filen genom vår funktion som städar datan
    df = load_data("data/ecommerce_sales.csv")

    # Kontrollera antal rader före och efter städning
    print("Antal rader före städning:", len(original))
    print("Antal rader efter städning:", len(df))
    print("Antal borttagna rader:", len(original) - len(df))

    # Kontrollera saknade värden
    print("\nSaknade värden:")
    print(df.isnull().sum())

    # Kontrollera datatyper
    print("\nDatatyper:")
    print(df.dtypes)

    # Visa de första fem raderna
    print("\nFörsta fem raderna:")
    print(df.head())