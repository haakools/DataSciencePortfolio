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




def update_url(driver, stat_name):

    # Update url to next tablename
    current_url = driver.current_url.split('/') # Dividing to change stat-page
    current_url[-2] = stat_name
    new_url = "/".join(current_url)
    return new_url
def get_table_from_css(driver, css_name):

    # Getting the html content
    content = driver.find_element(By.CSS_SELECTOR, css_name)
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

    # Getting the column values which are unique
    header = []
    for tr_body in tbody.find_all('tr'):
        tr_body_temp = tr_body.find_all('td')
        for i in range(len(tr_body_temp)):
            header.append(tr_body_temp[i]["data-stat"])

        break
    #header = table.find('thead').find_all('tr')[1].get_text().split('\n')[2:-1]
    df.columns=header

    # Dropping NaN rows which occur
    df = df.dropna()

    return df

def save_data(df, league_name):
    data_path = os.path.join(os.getcwd(), 'adv_data')

    # Creating folder if not exists
    if os.path.exists(data_path) == False:
        os.mkdir(data_path)

    # Saving the dataframe as csv
    file_name = league_name + ".csv"
    file_path = os.path.join(data_path, file_name)
    print("\n Saving data to: " + file_path)

    df.to_csv(file_path)

def open_webdriver(start_url):
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Starting webdriver
    driver.get(start_url)

    # Click "disagree cookies" - button
    disagree = driver.find_element(By.CSS_SELECTOR, "#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button:nth-child(1)")
    disagree.click()
    print("Disagree with cookies.")

    # Emulate human behaviour
    time.sleep(random.randint(0, 3))
    return driver



def get_league_data(league_meta_data, name_url, name_css):

    # league_meta_data : dictionary containing leaguename and "comp" number to access the url for current season.
    # Then the webscraping gets all the stats listed in both "name_url" and "name_css"
    # Then the webscraper click to the previous season and gets all the stats as in the previous point.
    # When the season contains 17, i.e. 17/18 season, the webscraper stops at this league as there is not data below this point
    # The process above then starts again for the next league.

    # Starting webpage
    start_url = 'https://fbref.com/en/'

    # Opening webdriver
    driver = open_webdriver(start_url)


    for league in league_meta_data:

        # Changing url to the newest season of the league in loop
        driver.get('https://fbref.com/en/comps/{}/stats/{}-Stats'.format(league_meta_data[league], league))


        # Initializing emtpy array for storing
        league_df = pd.DataFrame()

        while True:
            # Get season
            info = driver.find_element(By.CSS_SELECTOR, '#info')
            info_soup = BeautifulSoup(info.get_attribute('innerHTML')) # should this be different?
            season = info_soup.find('h1').text.split()[0]
            print("Fetching data for season " + season)

            for url_tag, css_tag in zip(name_url, name_css):
                # Emulate human behaviour
                time.sleep(random.randint(0,3))

                # Updating url
                new_url = update_url(driver, url_tag)

                # Opening the new url
                driver.get(new_url)

                # Scarping the table
                temp_df = get_table_from_css(driver=driver,
                                             css_name='#div_stats_{}'.format(css_tag)) # Changing the css selector tag for new

                # Adding season to the data
                temp_df["season"] = season

                # Combining the table for each season
                league_df = pd.concat([league_df, temp_df])


            if "17" in season: #& league == list(league_meta_data.keys())[-1]:
                print("Last season and league found")
                break # breakign the while true loop

            # Going to previous season
            try:
                # For the first "previous button"
                prev_button = driver.find_element_by_css_selector("#meta > div:nth-child(2) > div > a")
                prev_button.click()
                print("Going to next season")
            except:
                print("Did not find click button")
                break
            # Wait some time to make sure site is getting loaded
            time.sleep(random.randint(0, 5))

        # Saving the data
        save_data(league_df, league)
