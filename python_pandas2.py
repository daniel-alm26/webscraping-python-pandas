import pandas as pd
import requests
import os as o

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

url = 'https://br.investing.com/equities/brazil'
request = requests.get(url, headers=headers)

df = pd.read_html(request.text)  
for i, tabela in enumerate(df): 
    print('-------------------------------------')
    print(i)
    print(tabela)

df = pd.DataFrame(df[0]) 
print(df)

df['Último'] = df['Último'] / 100
df['Máxima'] = df['Máxima'] / 100
df['Mínima'] = df['Mínima'] / 100

df.to_csv('acoes_investing.csv', index=False)

df = pd.read_csv(r"acoes_investing.csv") 
df = df.drop('Unnamed: 0', axis=1) 
df.to_excel(r"acoes_investing.xlsx", index=False) 

o.system('start excel "{}"'.format(r'C:\projetosWebScraping\acoes_investing.xlsx'))
