from selenium import webdriver
import webbrowser
import time
from webdriver_manager.chrome import ChromeDriverManager

b = "https://deere.cloud.databricks.com/login.html"
webbrowser.register('chrome',
                   None,
                    webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome').open(b)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://deere.cloud.databricks.com/login.html")
time.sleep(20)
button = driver.find_element_by_xpath(r"/html/body/uses-legacy-bootstrap/div/div/div[1]/div/div/div/div/div/button")
button.click()


##EXTRA##
#driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")