
# import selenium, beautiful soup, schedule
# Assumes 5 resorts; Alta, Snowbird, Solitude, Brighton, and Powder Mountain

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import messageConfig as mc
import schedule
import time


def main_task(send_from_address, send_from_password):
    resorts = {
        "Alta": "snow-report-summary-alta",
        "Snowbird": "snow-report-summary-snowbird",
        "Solitude": "snow-report-summary-solitude",
        "Brighton": "snow-report-summary-brighton",
        "Powder Mountain": "snow-report-summary-powder-mountain"
    }
    # list of phone numbers to contact with the information
    phone_numbers = {
        'phone_number{}':'carrier'
    }
    # initial setup via selenium and beautiful soup to get things rolling

    s = Service(r"C:\Users\mnuge\Desktop\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.skiutah.com/snowreport")
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    final_updates = []

    # create a dictionary of all the mountains, pass these in for ID. Assumes a static list of mountains

    def scrapeUtah(dict_key, resort_html):
        cur_mountain = soup.findAll("div", id=resort_html)
        for x in cur_mountain:
            snow_Last_24 = x.find("div", class_="Conditions-condition SnowReportSummary-newSnow24").get_text() #pulls snow in the last 24 hours
            base_depth = x.find("div", class_="Conditions-condition SnowReportSummary-baseSnowDepth").get_text() #pulls current base depth
            snow_Last_24.strip()
            base_depth.strip()
            updated_info = {}
            updated_info["Resort: "] = dict_key
            updated_info["Base Depth: "] = base_depth[1:3]
            updated_info["Snow Last 24hrs: "] = snow_Last_24[1:2]
            updated_info[""] = "----------"
            final_updates.append(updated_info)

    for key in resorts:
        scrapeUtah(key, resorts[key])
    msg_str = ""
    for i in final_updates:
        for key in i:
            msg_str += key + i[key] + "\n"
    msg_str = f"\n{(str(msg_str))}"
    for phone in phone_numbers:
        mc.send(msg_str, phone, phone_numbers[phone],send_from_address,send_from_password)

#This email address is the one that you will send the message from

user_email = input("Please enter your Gmail address, ending in @gmail.com: \n")
user_password = input("Please enter your Gmail password: \n")

#Scheduling function to run every day at 06:30
schedule.every().day.at("06:30").do(main_task, user_email, user_password)
while True:
    schedule.run_pending()
    time.sleep(1)
