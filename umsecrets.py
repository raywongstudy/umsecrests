# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json
import time
from selenium.webdriver.chrome.options import Options
import io #for the file
import functions

start_time = time.time()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')


url = 'https://www.facebook.com/New-UM-Secrets-Backup-367101790658487'
executable_path = '/home/ubuntu/environment/umsecrets/chromedriver'#自行設定路徑
driver = webdriver.Chrome(executable_path=executable_path , chrome_options=chrome_options)
driver.get(url)

driver.implicitly_wait(1)

for i in range(4):
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

driver.find_element_by_css_selector("._62up").click()
driver.execute_script("document.getElementById('u_0_1g').style.display='none'")
sleep(2)

functions.click_more_btn(driver)#function for click all more button
sleep(1)

data_lists = []

#posts is the main posts id#u_0_18 > posts i want ._1xnd > .... 
# .    "._4-u2._4-u8._5jmm._5pat" the one by one post
posts = driver.find_elements_by_css_selector("#u_0_18 > ._1xnd > ._1xnd ._4-u2._4-u8._5jmm._5pat")
print(posts)

print("<p>posts len : ", len(posts),"</p>")
for post in posts:
    try:
        post_content = post.find_element_by_css_selector("._5pbx.userContent._3576")
        # post_content = post_content.get_attribute('innerHTML')
        post_content = post_content.text
        post_content = post_content.replace('"','\'')
        try:
            post_comments = functions.find_comments(post)
        except:
            post_comments = 'error / no'
            print("no post_comments")

        post_time = post.find_element_by_css_selector(".timestampContent").text
    except:
        post_content = 'error'   
        post_time = 'error' 
    try:
        post_like = post.find_element_by_css_selector("._81hb").text
    except:
        post_like = "0"
    data_list = {
        'post_time' : post_time,
        'post_content' : post_content,
        'post_comments' : post_comments,
        'post_like' : post_like 
    }

    data_lists.append(data_list)

print("<p>lists len : ", len(data_lists),"</p>")

# for python 3
with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data_lists, outfile, ensure_ascii=False, indent=4)

# #for python 2
# with io.open('data.json', 'w', encoding='utf-8') as f:
#   f.write(json.dumps(data_lists, ensure_ascii=False, indent=4))


print('done')
driver.quit()#關閉瀏覽器

print("--- %s seconds ---" % (time.time() - start_time))