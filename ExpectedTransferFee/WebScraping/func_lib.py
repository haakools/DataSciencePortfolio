import time
from selenium import webdriver
from datetime import datetime
import os
from bs4 import BeautifulSoup
import pandas as pd
import random

"""
Functions library for fbref.com webscraper.

    This webscraper uses selenium webdriver and Beautiful Soup to extract the data from fbref.com football stats.

    The data extracted is every players stats each season from the top 5 leagues.

    These stats include
        - Minutes played
        - Goals scored
        - Assists
        - Yellow cards

    And for the newer seasons (better technology) these include
        - xG (expected goals)
        - xA (expected assists)
"""

def init_selenium(chrome_path):
    # Opening the driver
    driver = webdriver.Chrome(executable_path=chrome_path)
    return driver

def webscraper(url, chrome_path, league_name, year_stop):
    """
    Enter in the url and this will click around and scrape the data on fbref.com for the particular league chosen.

    Input:
        url             : Url for the current season webpage to start extracting from
        chrome_path     : path to the chromium webdriver
        league_name     : Name of the league the url is scraping from. This creates folder and filenames
        year_stop       : The last season the webscraper goes to (Premier league goes to 92, Ligue 1 goes to 95(?))
    """

    # Starting webdriver
    driver = init_selenium(chrome_path)
    driver.get(url)

    # Click "disagree cookies" - button
    disagree = driver.find_element_by_css_selector("#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button:nth-child(1)")
    disagree.click()
    print("Disagree with cookies.")


    # Emulate human behaviour
    time.sleep(random.randint(0, 3))


    # Looping through all the seasons for that league
    while True:

        # Get seasons
        info = driver.find_element_by_css_selector('#info')
        info_soup = BeautifulSoup(info.get_attribute('innerHTML'))
        season = info_soup.find('h1').text.split()[0]
        print("Fetching data for season " + season)


        # Getting the table under #div_stats_standard
        content = driver.find_element_by_css_selector('#div_stats_standard')
        soup = BeautifulSoup(content.get_attribute('innerHTML'))

        # Extract table and tbody (table body)
        table = soup.find('table')
        tbody = table.find('tbody')

        # Appending every cell of data to a list
        data = []
        for tr_body in tbody.find_all('tr'):
            row = []
            for td in tr_body.find_all('td'):
                row.append(td.get_text())
            data.append(row)

        # Saving the table to a dataframe
        df = pd.DataFrame(data)

        # Get header
        header = table.find('thead').find_all('tr')[1].get_text().split('\n')[2:-1]
        df.columns=header
        df = df.dropna() # Dropping Nan rows
        df["Season"] = season

        # Saving each season as a separate csv
        save_data(df, season, league_name)


        # Setting and end to the loop if a certain year is reached
        if year_stop in season:
            print("Last season found " + season)
            return


        # Go to next page
        try:
            # For the first "previous button"
            prev_button = driver.find_element_by_css_selector("#meta > div:nth-child(2) > div > a")
            prev_button.click()
            print("Going to next season")
        except:
            print("Did not find click button")


        # Emulate human behaviour
        time.sleep(random.randint(0, 3))

    return

def save_data(df,season, league_name):
    data_path = os.path.join(os.getcwd(), 'data')

    # Checking if data path exists or not
    if os.path.exists(data_path) == False:
        os.mkdir(data_path)

    league_folder = os.path.join(data_path, league_name)

    if os.path.exists(league_folder) == False:
        print("Creating league folder")
        os.mkdir(league_folder)
    else:
        print("Folder for "+  league_name + " found.")

    # Saving the dataframe as csv
    file_name = league_name + "_" + season + ".csv"
    file_path = os.path.join(league_folder, file_name)
    print("Saving data to: \n" + file_path)

    df.to_csv(file_path)
