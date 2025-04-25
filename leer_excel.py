#leer
import pandas as pd
file_path = r"C:\Users\Rafael\Documents\emails.xlsx"  # Ajusta el nombre del archivo según corresponda
df = pd.read_excel(file_path)
print(df.head())

#escribir
df.to_excel("emails_copia.xlsx")