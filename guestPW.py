from bs4 import BeautifulSoup
import config
import requests
import schedule
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json
import requests


#Function Grab the guest password
def getGuestPWD():
    #Configure the selenium webdriver using google chrome
    options = Options()  
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome("./chromedriver", options=options)

    #Log into VPN using the website url
    driver.get("https://myaccess.oraclevpn.com")
    usernameElement = driver.find_element_by_id("username")
    usernameElement.send_keys(config.VPNusername)

    passwordElement = driver.find_element_by_id("password_input")
    passwordElement.send_keys(config.VPNpassword)

    passwordElement.submit()

    https = Select(driver.find_element_by_id('protocol_selector'))
    https.select_by_value('https://')

    #Access the guest password direct link, requires SSO login
    url = driver.find_element_by_id('unicorn_form_url')
    url.send_keys("https://gmp.oracle.com/captcha/fi1es/amer.txt?_dc=1575486564313")
    url.submit()

    #Wait for the webpage to fully load
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "sso_username")))
    usernameElement = driver.find_element_by_id("sso_username")
    usernameElement.send_keys(config.SSOusername)

    passwordElement = driver.find_element_by_id("ssopassword")
    passwordElement.send_keys(config.SSOpassword)
    passwordElement.submit()

    #Parse out the html and print
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.pre.string)
    driver.quit()
    return soup.pre.string


def printGuestPWD():
    guestPWD = getGuestPWD()

    # parse out the password only
    splitterPWD = guestPWD.split(' ')[5].split('\n')
    print(splitterPWD[0])

    guestpass = "```{}``` {}".format(guestPWD, splitterPWD[0])
    # Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
    webhook_url = config.webhook
    slack_data = {'text': guestpass}

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

# printGuestPWD()

#Have the guest password retrieved and posted every morning at 6AM PST
schedule.every().day.at("16:10").do(printGuestPWD)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
