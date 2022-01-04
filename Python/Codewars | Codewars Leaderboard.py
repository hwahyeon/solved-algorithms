import re
import requests
from bs4 import BeautifulSoup

def get_leaderboard_honor():
    url = 'https://www.codewars.com/users/leaderboard'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    lst_ = soup.find_all(text=re.compile("[0-9]"))[3:1598]

    A = []
    for i in lst_:
        if ',' in i:
            A.append(int(i.replace(',','')))

    return A
