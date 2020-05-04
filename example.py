from bs4 import BeautifulSoup
import requests
import csv

def getData(url):
    r = requests.get(url)
    return r.text

def speak(str):
    from win32com.client import Dispatch 
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":
    
    myHtmlData= getData('https://www.brainyquote.com/topics/science-quotes')

    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(myHtmlData)
    # print(soup.prettify())
    #print(soup.get_text())
    for div in soup.find("div" ,{'class': 'reflow_container'}).find_all('div'):
        print(div.get_text())
        speak(div.get_text())


    


    
    