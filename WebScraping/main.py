import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import os
from bs4 import BeautifulSoup
import pandas as pd
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# functions library
import functions as fn



# Name of the url for the stat
name_url = ['keepersadv', 'shooting', 'passing', 'passing_types', 'gca', 'defense', 'possession']

# Name of the css_selector for the stat
name_css = ['keeper_adv', 'shooting', 'passing', 'passing_types' , 'gca', 'defense', 'possession' ] #table for each stat has different surfix

# League data to acceses the correct url, i.e.: https://fbref.com/en/comps/20/stats/Bundesliga-Stats
league_meta_data = {
    'Bundesliga': 20 ,
    'Premier-League': 9,
    'Ligue-1': 13,
    'Serie-A': 11,
    'La-Liga': 12
}

# Running the webscraper
fn.get_league_data(league_meta_data, name_url, name_css)
