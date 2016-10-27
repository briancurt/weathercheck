#!/bin/python3

# Set up chrome driver https://sites.google.com/a/chromium.org/chromedriver/getting-started
# Install xorg-x11-server-Xvfb

import requests
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from pyvirtualdisplay import Display

def get_smn():
        
        smn = requests.get('http://www.smn.gov.ar/?mod=pron&id=1')
        soup = BeautifulSoup(smn.content, 'html.parser')
        return soup.find(id="divPronostico").b.string
        
def get_accu():

        accu = requests.get('http://www.accuweather.com/es/ar/buenos-aires/7894/weather-forecast/7894')
        soup = BeautifulSoup(accu.content, 'html.parser')
        return soup.find(class_="day current first cl").find(class_="large-temp").string
        
def get_wc():

        display = Display(visible=0, size=(800, 600))
        display.start()
        browser = webdriver.Chrome('/usr/bin/chromedriver')
        browser.get('https://weather.com/es-AR/tiempo/hoy/l/ARBA0009:1:AR')
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        browser.quit()
        display.stop()
        return soup.find(class_="today_nowcard-temp").find(class_="dir-ltr").string
#       s/term soup.find(class_="today_nowcard-feels").find(class_="dir-ltr").string

def main():

        print("SMN:     ", get_smn(), "ST: n/a")
        print("ACCU:    ", get_accu(), "ST: n/a")
        print("WC:      ", get_wc(), "°C ST: n/a")
        
if __name__ == "__main__":
    main()
