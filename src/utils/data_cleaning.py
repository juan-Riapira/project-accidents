import pandas as pd

url="https://www.datos.gov.co/api/views/jj5k-4x95/rows.csv?accessType=DOWNLOAD"

df =pd.read_csv(url)

print(df.head())

# obtenemos el numero de filas del dataframe sin limpieza
number_row = len(df)
print("number of row ", number_row)

