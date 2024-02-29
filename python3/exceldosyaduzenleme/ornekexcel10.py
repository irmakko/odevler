import pandas as pd
df1 = pd.read_excel('youtrack_excel - Kopya.xlsx')
df2 = pd.read_excel('Software_Development_Team Dosyasının Kopyası.xlsx')
sadece_sutun = df2['Tanımlama']
df1['Description'] = sadece_sutun
df1['Description']=df1['Description'].str.upper()
df1.to_excel('enyeniexcel.xlsx', index=False)
print("veriler başariyla eklendi.")
