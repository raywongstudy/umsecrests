from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json
    
driver = webdriver.Firefox()
driver.get("https://www.facebook.com/New-UM-Secrets-359374200910281/")
driver.implicitly_wait(1)

for i in range(10):
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(5)

data_lists = []


posts = driver.find_elements_by_css_selector("#u_0_1b > ._1xnd > ._1xnd ._4-u2._4-u8._5jmm._5pat")

print("<p>posts len : ", len(posts),"</p>")
for post in posts:
    try:
        post_content = post.find_element_by_css_selector("._5pbx.userContent._3576")
        # post_content = post_content.get_attribute('innerHTML')
        post_content = post_content.text
        post_content = post_content.replace('"','\'')

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
        'post_like' : post_like 
    }

    data_lists.append(data_list)

print("<p>lists len : ", len(data_lists),"</p>")

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data_lists, outfile, ensure_ascii=False, indent=4)



