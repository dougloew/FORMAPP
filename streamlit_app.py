#https://www.scrapethissite.com/pages/forms
# 
# 

import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml


#streamlit run streamlit_app.py

st.title("Web Scraper")


webpage = requests.get(f'https://www.scrapethissite.com/pages/forms/').text

##'lxml': 


soup = BeautifulSoup(webpage, 'lxml')
players = soup.find_all('tr')[1:]

print(players)

team_name = []
year = []
win = []
losses = []

otlosses = []
winpercent = []
goalsfor = []
goalsagainst = []
plusminus = []



for i in players:
    name = i.find_all('td')[0].text.strip()
    yr = i.find_all('td')[1].text.strip()
    wn = i.find_all('td')[2].text.strip()
    ls = i.find_all('td')[3].text.strip()
    ol = i.find_all('td')[4].text.strip()
    wp = i.find_all('td')[5].text.strip()
    gf = i.find_all('td')[6].text.strip()
    ga = i.find_all('td')[7].text.strip()
    pm = i.find_all('td')[8].text.strip()
    

    team_name.append(name)
    year.append(yr)
    win.append(wn)
    losses.append(ls)

    otlosses.append(ol)
    winpercent.append(wp)
    goalsfor.append(gf)
    goalsagainst.append(ga)
    plusminus.append(pm)

data = pd.DataFrame({'Team Name': team_name,
                     "Year": year,
                     "win": win,
                     "Losses": losses,
                     "Overtime Losses": otlosses,
                     "Win Percentage": winpercent,
                     "Goals For": goalsfor,
                     "Goals Against": goalsagainst,
                     "Plus Minus": plusminus
                     })

print(data)

st.dataframe(data)

