from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

# open target website with webdriver
website = 'https://www.linkedin.com/search/results/companies/?heroEntityKey=urn%3Ali%3Aautocomplete%3A-1781024605&keywords=video%20production&origin=CLUSTER_EXPANSION&position=0&searchId=8b8b2aaa-172b-4aae-86ba-842fcb3ce178&sid=gac'
path = '\Python310\Chromedriver'
driver = webdriver.Chrome(executable_path=r'C:\Python310\Chromedriver\chromedriver.exe')
driver.get(website)

# click sign in button
click_sign_in = driver.find_element("xpath", '//*[@class="main__sign-in-link"]').click()

# fill linkedin username and password
username = "tsubaki.azura@gmail.com"
password = "F@w6UZ*F4kfY"

# automated fill in username and password
driver.find_element("xpath", '//*[@name="session_key"]').send_keys(username)
driver.find_element("xpath", '//*[@name="session_password"]').send_keys(password)

# click to log in
click_submit = driver.find_element("xpath", '//*[@aria-label="Sign in"]').click()

# click to go deeper into spesific portfolio link
# click_porfolio = driver.find_element("xpath", '//a[@class="app-aware-link"]').click()

# scrape portfolio page
scrape = driver.find_elements("xpath", '//a[@class="app-aware-link"]')

company_name = []

x = 0
company = 1
for a in scrape
  x+=1
  if x == 5
    x = 1
  end
  result = a.text
  if x == 1
    result = company + " " + a.text
    company +=1
  end
  print (result)





