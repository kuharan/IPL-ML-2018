import pandas as pd
from bs4 import BeautifulSoup
import requests

# For player ranks
url = 'http://www.cricmetric.com/ipl/ranks/'
pd.read_html(requests.get(url).content)[-1].to_csv("./Dataset/_player_rank.csv", index=False, header=None)

# Store the sum of EF score by team.
data = pd.read_csv('./Dataset/_player_rank.csv')
team_rank = pd.DataFrame(
    data.groupby('Team')['EFscore'].agg(['sum']).reset_index().sort_values('sum', ascending=False)).to_csv(
    './Dataset/_team_rank.csv', index=False)

# For news Headlines
url = 'https://sports.ndtv.com/indian-premier-league-2018/news'
page_response = requests.get(url)
page_content = BeautifulSoup(page_response.content, "html.parser")
pd.DataFrame(page_content.find_all(class_='menutitle')).to_csv("./Dataset/_news.txt", index=False, header=None)
clean_df = pd.read_csv('./Dataset/_news.txt', header=None).replace('<[^>]+>', '', regex=True)
pd.DataFrame(clean_df).to_csv("./Dataset/_news.txt", index=False, header=None)

