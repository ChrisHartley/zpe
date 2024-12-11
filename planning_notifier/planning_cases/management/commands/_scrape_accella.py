from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

import time
import csv

from urllib3.util import Retry
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
from random import randint

# by supputuri: https://stackoverflow.com/a/56570364
def getDownLoadedFileName(driver, waitTime):
    driver.execute_script("window.open()")
    WebDriverWait(driver,10).until(EC.new_window_is_opened)
    driver.switch_to.window(driver.window_handles[-1])
    driver.get("about:downloads")

    endTime = time.time()+waitTime
    while True:
        try:
            fileName = driver.execute_script("return document.querySelector('#contentAreaDownloadsView .downloadMainArea .downloadContainer description:nth-of-type(1)').value")
            if fileName:
              #  driver.close()
                return fileName
        except:
            pass
        time.sleep(1)
        if time.time() > endTime:
            break
#    driver.close()
    return None

def get_driver():
    options = Options()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", "./")
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

  #  driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver = webdriver.Remote(command_executor='http://selenium:4444/wd/hub', options=options)

    driver.implicitly_wait(3) # seconds
    return driver



def geocode_parcel_number(parcel_number):
    BASE_URL = "http://xmaps.indy.gov/arcgis/rest/services/Locators/IndyParcelID/GeocodeServer/findAddressCandidates?"
    GEOCODE_URL = "{}SingleKey={}&maxLocations=1&outSR=4326&f=pjson".format(BASE_URL, parcel_number,)

    s = Session()
    retries = Retry(
        total=5,
        backoff_factor=0.1,
    )
    s.mount('http://', HTTPAdapter(max_retries=retries))
    results_dict = {}

    try:
        response = s.get(GEOCODE_URL, timeout=30)
    except RequestException as err:
        return results_dict

    if response.status_code == 200:
        try:
            response_json = response.json()
            wkid = response_json['spatialReference']['wkid']
            lon = response_json['candidates'][0]["location"]["x"]
            lat = response_json['candidates'][0]["location"]["y"]
            results_dict['PNT_WKT'] = 'SRID={wkid};POINT({lon} {lat})'.format(wkid=wkid, lon=lon, lat=lat)
            results_dict['Geocoding Accuracy']  = response_json['candidates'][0]['score']
        except:
            print('Unable to geocode {}'.format(parcel_number,))
            print(results_dict)
            results_dict['PNT_WKT'] = ''

    else:
        results_dict['PNT_WKT'] = ''
    return results_dict

def get_parcel_details(parcel_number):
    BASE_URL = 'http://xmaps.indy.gov/arcgis/rest/services/Common/CommonlyUsedLayers/MapServer/0/query?'
    QUERY = 'where=PARCEL_C%3D+%27{parcel_number}%27&outFields=*&returnGeometry=true&f=pjson'.format(parcel_number=parcel_number)

    s = Session()
    retries = Retry(
        total=5,
        backoff_factor=0.1,
    )
    s.mount('http://', HTTPAdapter(max_retries=retries))
    results_dict = {}

    try:
        response = s.get(BASE_URL+QUERY, timeout=30)
    except RequestException as err:
        return results_dict

    if response.status_code == 200:
        try:
            response_json = response.json()
            FIELDS_OF_INTEREST = [
                'STNUMBER', 'PRE_DIR', 'FULL_STNAME', 'SUF_DIR', 'CITY', 'ZIPCODE',
                'FULLOWNERNAME', 'ESTSQFT', 'PROPERTY_CLASS', 'OWNERADDRESS', 'OWNERADDRESS2',
                'OWNERCITY', 'OWNERSTATE', 'OWNERZIP', 'ASSESSORYEAR_LANDTOTAL', 'ASSESSORYEAR_IMPTOTAL',
                'ASSESSORYEAR_TOTALAV', 'LEGAL_DESCRIPTION_'
            ]
            for field in FIELDS_OF_INTEREST:
                results_dict[field] = response_json['features'][0]['attributes'][field]

        except:
            print('Unable to retrieve details on parcel {}'.format(parcel_number,))
            print(results_dict)

    else:
        results_dict
    return results_dict

def get_case_details(case, driver=None):
    if driver is None:
        driver = get_driver()
    driver.get("https://permitsandcases.indy.gov/")
    #assert "Accela Citizen Access" in driver.title
    try:
        elem = driver.find_element(By.ID, "more_tab_place_holder")
        actions = ActionChains(driver)
        actions.move_to_element(elem).perform()
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "//*[@title='Planning / Historic Preservation']")
        elem.click()
        #assert driver.find_element(By.XPATH, '//*[@id="ctl00_PlaceHolderMain_lblPermitListTitle"]').text == 'Search for Planning / IHPC Cases'
        elem = driver.find_element(By.ID, "ctl00_PlaceHolderMain_generalSearchForm_txtGSPermitNumber")
        elem.send_keys(case)
        elem = driver.find_element(By.ID, "ctl00_PlaceHolderMain_btnNewSearch").click()

        wait = WebDriverWait(driver, 30)
        elem = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_PlaceHolderMain_lnkPrintSummary")))

        case_details = {}
        case_details['Case Number'] = case
        case_details['Case Date'] = '01/01/1970' # No way to find case date from case detail page, fact of life.
        case_details['Location'] = driver.find_element(By.XPATH, '//*[@id="divWorkLocationInfo"]').text.strip()
        case_details['Parcel'] = driver.find_element(By.XPATH,'//*[@id="ctl00_PlaceHolderMain_PermitDetailList1_palParceList"]/div/h2/table/tbody/tr/td/div').get_attribute('innerHTML').strip()[-7:]
        case_details['Description'] = driver.find_element(By.XPATH, "//table[@id='ctl00_PlaceHolderMain_PermitDetailList1_TBPermitDetailTest']//div[contains(.,'Description:')]").text[13:]
        case_details['CaseType'] = driver.find_element(By.XPATH, '//span[@id="ctl00_PlaceHolderMain_lblPermitType"]').text
        case_details['Owner'] = driver.find_element(By.XPATH, "//table[@id='ctl00_PlaceHolderMain_PermitDetailList1_TBPermitDetailTest']//div[contains(.,'Owner:')]").text[7:]
        case_details['Case URL'] = driver.current_url
        geocoded_results = geocode_parcel_number(case_details['Parcel'])
        try:
            case_details['PNT_WKT'] = geocoded_results['PNT_WKT']
        except KeyError:
            case_details['PNT_WKT'] = ''
    except (NoSuchElementException, TimeoutException):
        return None
    return case_details

def get_case_list(start_date='09/10/2024', end_date='09/12/2024'):
    driver = get_driver()

    driver.get("https://permitsandcases.indy.gov/")
    assert "Accela Citizen Access" in driver.title
    elem = driver.find_element(By.ID, "more_tab_place_holder")
    actions = ActionChains(driver)
    actions.move_to_element(elem).perform()
    time.sleep(3)
    elem = driver.find_element(By.XPATH, "//*[@title='Planning / Historic Preservation']")
    elem.click()
    assert driver.find_element(By.XPATH, '//*[@id="ctl00_PlaceHolderMain_lblPermitListTitle"]').text == 'Search for Planning / IHPC Cases'
    elem = driver.find_element(By.ID, "ctl00_PlaceHolderMain_generalSearchForm_txtGSStartDate")
    for _ in range(11):
        elem.send_keys(Keys.ARROW_LEFT)
    elem.send_keys(start_date)

    elem = driver.find_element(By.ID, "ctl00_PlaceHolderMain_generalSearchForm_txtGSEndDate")
    for _ in range(11):
        elem.send_keys(Keys.ARROW_LEFT)
    elem.send_keys(end_date)
    elem = driver.find_element(By.ID, "ctl00_PlaceHolderMain_btnNewSearch").click()

    download_list_link = driver.find_element(By.ID, "ctl00_PlaceHolderMain_dgvPermitList_gdvPermitList_gdvPermitListtop4btnExport")
    wait = WebDriverWait(driver, 30)
    elem = wait.until(EC.element_to_be_clickable(download_list_link))
    elem = driver.find_element(By.ID, "ctl00_PlaceHolderMain_dgvPermitList_gdvPermitList_gdvPermitListtop4btnExport").click()
    fileName = getDownLoadedFileName(driver, 10)

    cases = []
    # HACK - need to get download folder dynamically, setting it doesn't seem to work so that's why this hack is here.
    with open('/tmp/downloads/{}'.format(fileName,)) as csvfilein:
        case_reader = csv.DictReader(csvfilein)
        for row in case_reader:
            case = get_case_details(row['Case Number'], driver)
            if case is None: # Try once more
                time.sleep(5)
                case = get_case_details(row['Case Number'], driver)
                if case is None: # Assign the values we got from the case listing and move on.
                    case = {}
                    case['Case Number'] = row['Case Number']
                    case['Description'] = row['Description']
                    case['CaseType'] = row['Case Type']
                    case['Date'] = row['Date']
                    case['Location'] = ''
                    case['PNT_WKT'] = ''
                    case['Owner'] = ''
                    case['Case URL'] = ''
                    case['Parcel'] = ''
            case['Case Date'] = row['Date']
            cases.append(case)
           # break
            time.sleep( randint(1,5) ) # be a good very slow scraper

    driver.quit()
    return cases
  #  driver.quit()



if __name__ == '__main__':
    cases = get_case_list(start_date='09/30/2024', end_date='10/02/2024')
    print(cases)
