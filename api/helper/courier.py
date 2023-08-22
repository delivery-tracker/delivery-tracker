import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup

def fedex(tracking):
    driver = uc.Chrome(headless=True)
    driver.get(f"https://www.fedex.com/fedextrack/?trknbr={tracking}")
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for delivery_date in soup.find_all("span", {"class": "deliveryDateText"}, True):
        return (delivery_date.text)

def canada_post(tracking):
    driver = uc.Chrome(headless=True)
    driver.get(f"https://www.canadapost-postescanada.ca/track-reperage/en#/details/{tracking}")
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for delivery_date in soup.find_all("span", {"class": "text-typography-redesigned-medium edd-text-size ng-star-inserted"}, True):
        return (delivery_date.text)