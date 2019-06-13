from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

url = 'http120.105.184.250cswangthitLinuxCommand-1.htm'
executable_path = 'homecodingworkspacechromedriver'#自行設定路徑
driver = webdriver.Chrome(executable_path=executable_path , chrome_options=chrome_options)
driver.get(url)

html = driver.page_source
print(html)
print(done)
driver.quit()#關閉瀏覽器 
