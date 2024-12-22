# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:01:32 2024

@author: mcmah
"""
import requests
import sqlite3
from bs4 import BeautifulSoup

def GetOutsideTemperature():
    # Enter city name
    city = "harvard, ma"

    # Creating URL and making requests instance
    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content

    # Getting raw data using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extracting the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    return temp

def CreateWebPage():
    try:
        conn = sqlite3.connect("GymTest.db")
        cursor = conn.cursor()
        cmd = "SELECT * FROM reports DESC LIMIT 100;"
        cursor.execute(cmd)
        output = cursor.fetchall() 
        
        for sublist in output:
            print(sublist)
    except sqlite3.Error as e:
        # Handle the exception
        print(f"An sqlite error occurred: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    CreateWebPage()