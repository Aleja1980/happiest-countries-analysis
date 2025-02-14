import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['country'], inplace=True)
    df.fillna(method='ffill', inplace=True)
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    return df
# Ruta del archivo CSV relativa a la carpeta raíz del proyecto
file_path = 'happiest-countries-in-the-world-2024.csv'
df = load_data(file_path)
print(df.head())  