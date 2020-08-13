import os
import pandas as pd
import numpy as np

os.chdir(r"C:\Users\saivivekc\Downloads\SF and Intercom reports\Daily reports")

sf_workbook = "13_aug_sf_all.csv"
intercom_workbook = "13th_aug_intercom.csv"
output_workbook = "output.xlsx"

df_sf = pd.read_csv(sf_workbook, encoding='latin1')
df_intercom = pd.read_csv(intercom_workbook)

df_3 = pd.merge(df_sf, df_intercom, on = 'Email', how = 'left')

df_3 = df_3.replace(np.nan, ' ', regex = True)

df_3 = df_3.dropna(how='all', axis=1)

print(df_3)

df_3.to_excel(output_workbook, index=False)
