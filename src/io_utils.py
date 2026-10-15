import pandas as pd 

def load_data(filepath):
    data = pd.read_csv(filepath, encoding='utf-8')
    return data


df = load_data("data/ecommerce_sales.csv")
print(df.head())


# https://www.strato.se/guide/webbplatser/webbutveckling/python-pandas-read-csv/