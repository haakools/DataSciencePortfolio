import requests
from selenium import webdriver
from selenium.webdriver import DesiredCabalities
from bs4 import BeautifulSoup


URL = 'https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/8618/Stages/19793/PlayerStatistics/England-Premier-League-2021-2022'

def driver():
    # Do not know what this does (?)
    desired_capabilites = DesiredCapabilites.PHANTOMJS.copy()
	desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
																  'AppleWebKit/537.36 (KHTML, like Gecko) ' \
																  'Chrome/39.0.2171.95 Safari/537.36'
	driver = webdriver.PhantomJS(desired_capabilities=desired_capabilities)

	return driver

def fetcher(driver, URL):
    driver.get(URL)
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML").encode('utf-8')

    with open('WhoScored.html', 'w') as sf:
        sf.write(str(source_code))
        sf.flush()

    driver.quit()


soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="qc-cmp2-container")

print(results)
