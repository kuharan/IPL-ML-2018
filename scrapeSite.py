import requests
import pandas as pd

url = 'http://www.cricmetric.com/ipl/ranks/'
# pd.read_html(requests.get(url).content)[-1].to_csv("./Dataset/_player_rank.csv",index=False)
html = requests.get(url).content

df_list = pd.read_html(html)
df = df_list[-1]
df.to_csv('./Dataset/_player_rank.csv', index=False)
df_new = pd.read_csv('./Dataset/_player_rank.csv')
df_new.to_csv('./Dataset/_player_rank.csv', index=False, header=None)

