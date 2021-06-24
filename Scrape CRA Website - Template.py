# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 13:29:46 2021

@author: CWilson
"""

from selenium.webdriver import Edge, Chrome
from selenium.webdriver.common.keys import Keys 
import time
import pandas as pd

# Initialize Selenium (for Edge)
edgedriver_path = r"C:\Users\cwilson\Documents\Chromedriver\edgedriver\msedgedriver.exe"
d = Edge(edgedriver_path)

#Initialize Selenium (for Chome)
#chromedriver_path = r"C:\Users\cwilson\Documents\Chromedriver\chromedriver.exe"
#d = Chrome(chromedriver_path)

def scrape_cra_people(letter):
    url = r"https://www.crai.com/our-people/?page=1&sort=role&letter={}".format(letter)
    d.get(url)
    
    print("Getting data for letter {}...".format(letter))
    
    time.sleep(1)
    
    try:
        cookies_button = d.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
        cookies_button.send_keys(Keys.ENTER)
    except:
        pass

    time.sleep(0.5)
    
    while True:
        try:
            load_more_button = d.find_element_by_xpath('//*[@id="LandingPageSearch__scroll-to-results"]/div[2]/button')
            load_more_button.send_keys(Keys.ENTER)
            time.sleep(0.5)
        except:
            break
    
    cards = d.find_elements_by_class_name("PersonCard__content")
    people = []
    for card in cards:
        split = card.text.split("\n")
        name = card.find_element_by_class_name("PersonCard__name").text
        title = card.find_element_by_class_name("PersonCard__role").text
        try:
            office = card.find_element_by_class_name("PersonCard__location").text
        except:
            office = ""
        contacts = card.find_elements_by_class_name("PersonCard__contact")
        email = ""
        phone = ""
        for contact in contacts:
            if "@" in contact.text:
                email = contact.text
            else:
                phone = contact.text

        temp_dict = {"Name" : name,
                     "Title" : title,
                     "Office" : office,
                     "Phone" : phone,
                     "E-mail" : email}

        people.append(temp_dict)

    return people


#Create list of letters called "list of letters"


#Create empty list of people called "all_people"


#Loop through the list of letters and run "scrape_cra_people" for each letter. Store results into a variable called "results"


    #Run the "scrape_cra_people" function. Store results in variable "results"


    #Within the loop add the results to "all_people"


#Create dataset from "all_people"
df = pd.DataFrame(all_people)