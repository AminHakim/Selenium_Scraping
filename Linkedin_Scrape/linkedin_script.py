import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

# open target website with webdriver
website = 'https://www.linkedin.com/search/results/companies/?heroEntityKey=urn%3Ali%3Aautocomplete%3A-1781024605&keywords=video%20production&origin=CLUSTER_EXPANSION&position=0&searchId=8b8b2aaa-172b-4aae-86ba-842fcb3ce178&sid=gac'
path = '\Python310\Chromedriver'
driver = webdriver.Chrome(executable_path=r'C:\Python310\Chromedriver\chromedriver.exe')
driver.get(website)

# wait before click sign in
time.sleep(2)

# click sign in button
click_sign_in = driver.find_element("xpath", '//*[@class="main__sign-in-link"]').click()

# fill linkedin username and password
username = ""
password = ""

# wait before click log in
time.sleep(5)

# automated fill in username and password
driver.find_element("xpath", '//*[@name="session_key"]').send_keys(username)
driver.find_element("xpath", '//*[@name="session_password"]').send_keys(password)

# click to log in
click_submit = driver.find_element("xpath", '//*[@aria-label="Sign in"]').click()

# click to go deeper into spesific portfolio link
# click_porfolio = driver.find_element("xpath", '//a[@class="app-aware-link"]').click()

# scrape portfolio page
company_name = []
follower = []
industry = []
description = []
linkedin_link = []

X = 1

while X <= 100:
    X += 1

    scrape = driver.find_elements("xpath", '//div[@class="entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light"]')

    for a in scrape:
        array1 = a.text.split('\n')
        #print(array1)
        company_name.append(array1[0])
        follower.append(array1[1])
        industry.append(array1[2])
        description.append(array1[3])
        #print(a.text)

# scrape linkedin link
    y = 0
    while y < 10:
        y += 1

        link = driver.find_elements(by=By.XPATH,
                                    value="/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[" + str(
                                        y) + "]/div/div/div[2]/div[1]/div[1]/div/span/span/a")
        for a in link:
            get_link = a.get_attribute("href")
            linkedin_link.append(get_link)
            # print(get_link)

# print(company_name)
# print(follower)
# print(industry)
# print(description)
    print('COMPANY NAME')
    for a in company_name:
        print(a)
    print()
    print('FOLLOWER')
    for a in follower:
        print(a)
    print()
    print('INDUSTRY')
    for a in industry:
        print(a)
    print()
    print('DESCRIPTION')
    for a in description:
        print(a)
    print('LINKEDIN LINK')
    for a in linkedin_link:
        print(a)

# wait before scroll bottom page
    time.sleep(3)

# scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# wait before click next
    time.sleep(5)

# click next button
    next_button = driver.find_element("xpath", '//button[@aria-label="Next"]').click()

# sleep to wait loading page after next page
    time.sleep(5)

# final export
df = pd.DataFrame({'company_name': company_name, 'follower': follower, 'industry': industry, 'description': description,
                   'linkedin_link': linkedin_link})
df.to_excel('Linkedin test 1.xlsx')
print(df)


