import time

from selenium import webdriver
import pandas as pd

# open target website with webdriver
website = 'https://www.linkedin.com/search/results/companies/?heroEntityKey=urn%3Ali%3Aautocomplete%3A-1781024605&keywords=video%20production&origin=CLUSTER_EXPANSION&position=0&searchId=8b8b2aaa-172b-4aae-86ba-842fcb3ce178&sid=gac'
path = '\Python310\Chromedriver'
driver = webdriver.Chrome(executable_path=r'C:\Python310\Chromedriver\chromedriver.exe')
driver.get(website)

time.sleep(2)

# click sign in button
click_sign_in = driver.find_element("xpath", '//*[@class="main__sign-in-link"]').click()

# fill linkedin username and password
username = "pringiolos@gmail.com"
password = "Akk1Q@gtBHPV"

time.sleep(5)

# automated fill in username and password
driver.find_element("xpath", '//*[@name="session_key"]').send_keys(username)
driver.find_element("xpath", '//*[@name="session_password"]').send_keys(password)

# click to log in
click_submit = driver.find_element("xpath", '//*[@aria-label="Sign in"]').click()

# click to go deeper into spesific portfolio link
# click_porfolio = driver.find_element("xpath", '//a[@class="app-aware-link"]').click()

# scrape portfolio page
scrape = driver.find_elements("xpath", '//div[@class="entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light"]')

company_name = []
follower = []
industry = []
description = []

for a in scrape:
    array1 = a.text.split('\n')
    #print(array1)
    company_name.append(array1[0])
    follower.append(array1[1])
    industry.append(array1[2])
    description.append(array1[3])
    #print(a.text)

#print(company_name)
#print(follower)
#print(industry)
#print(description)
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

# scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# wait before click next
time.sleep(5)

# click next button
next_button = driver.find_element("xpath", '//button[@aria-label="Next"]').click()

time.sleep(2)

scrape = driver.find_elements("xpath", '//div[@class="entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light"]')

company_name = []
follower = []
industry = []
description = []

for a in scrape:
    array1 = a.text.split('\n')
    #print(array1)
    company_name.append(array1[0])
    follower.append(array1[1])
    industry.append(array1[2])
    description.append(array1[3])
    #print(a.text)

#print(company_name)
#print(follower)
#print(industry)
#print(description)
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

df = pd.DataFrame({'company_name': company_name, 'follower': follower, 'industry': industry, 'description': description,})
df.to_excel('test3.xlsx')
print(df)


