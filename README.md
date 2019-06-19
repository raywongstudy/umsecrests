# Setup a Cloud IDE Linux for Selenium use Chromedriver Headless

### 1 . install python: 

  your can check how to install python : url( https://realpython.com/installing-python/ ) or 
```
    sudo apt update
    sudo apt install python3.7
```
### 2 . install selenium:   
```
  pip install selenium
  pip3 install selenium
```

  your can check how to install python selenium : url( https://selenium-python.readthedocs.io/installation.html )

### 3 . set chrome headless config and import selenium in python file:

```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

url = 'http://mlcfood.tk/'# write your url
executable_path = '/home/ubuntu/environment/chromedriver'# write your chromedriver path
driver = webdriver.Chrome(executable_path=executable_path , chrome_options=chrome_options)
```

# error message and solution

### 1 . SyntaxError : Non-ASCII character '\xe8' in file testing.py on line 11, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

> solution : add this in the python file head : -*- coding:UTF-8 -*-

### 2 . selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable may have wrong permissions. Please see https://sites.google.com/a/chromium.org/chromedriver/home

> solution : use linux command (" chmod 774 <your file path> ")    e.g(" chmod 774 /home/ubuntu/environment/chromedriver ")
  
> remind : you can use linux command (" ls -lh ") to check the permissions

### 3 . selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Chrome binary

> solution : use linux command (" sudo apt-get install chromium-browser ") to install teh chrome browser file







