# -*- coding:UTF-8 -*-
# Here for the import library
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By#for the selector use by

import time
from selenium.webdriver.chrome.options import Options
from functions import indexPageFunctions
from locators.umsecrets_locators import indexPageLocators

#default value
scroll_times = 5

#set functions = indexPageFunctions
functions = indexPageFunctions
# Here for cacl the runing time
start_time = time.time()

# Here for the headless options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')

#open url setting 
url = 'https://www.facebook.com/New-UM-Secrets-Backup-367101790658487'
executable_path = 'webdriver/chromedriver'#自行設定webdriver路徑

class mainClass(object):
    """here is the main class"""

    def setDriver(executable_path , options):
        if options == True:
            driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)#for chrome
        else:
            driver = webdriver.Chrome(executable_path=executable_path)
        return driver

# main function
if __name__ == "__main__":

    driver = mainClass.setDriver(executable_path,True)
    driver.implicitly_wait(10)

    driver.get(url)
    sleep(1)
    #some error handle
    try:
        driver.find_element_by_css_selector('.autofocus.layerCancel._4jy0._4jy3._4jy1._51sy.selected._42ft').click()
    except:
        print('can not find the error alert to handle')

    #1 load more posts
    print('1. load more posts~')
    # scroll_time = input("    How many scroll times:")
    functions.loadMorePosts(driver,int(scroll_times))

    #2 delete the login banner
    print('2. delete the login banner~')
    functions.delLoginBanner(driver)

    #3 click show all button
    print('3. click show all comments~')
    functions.clickShowAllComments(driver)

    # #4 click more button
    # print('4. click more comments button~')
    # functions.click_more_btn(driver)

    #5 click all detail button
    print('5. click posts and comments detail~')
    functions.clickPostsDetail(driver)

    data_lists = []

    posts = driver.find_elements_by_css_selector(indexPageLocators.all_posts_box)

    print('6. get posts and comments data~')
    print("    <p>posts len : ", len(posts),"</p>")
    for post in posts:
        try:
            post_author = post.find_element_by_css_selector(indexPageLocators.post_author)
            post_author = post_author.text
            print('    runing post_tag:',post_author)

            post_content = post.find_element_by_css_selector(indexPageLocators.post_content)
            post_content = post_content.text
            # print('post_content:',post_content)
            post_content = post_content.replace(post_author," ")
            post_content = post_content.replace('"','\'')

            try:
                post_comments = functions.find_comments(post)
            except:
                post_comments = 'error'

            post_time = post.find_element_by_css_selector(indexPageLocators.post_time).text
        except:
            post_content = 'error'   
            post_time = 'error' 
        try:
            post_like = post.find_element_by_css_selector(indexPageLocators.post_like).text
        except:
            post_like = "0"
        try:
            post_comments_number = len(post_comments)
        except:
            post_comments_number = 0
        data_list = {
            'post_author' : post_author,
            'post_time' : post_time,
            'post_content' : post_content,
            'post_comments' : post_comments,
            'post_like' : post_like,
            'post_comments_number' : post_comments_number,
        }

        data_lists.append(data_list)

    print("    <p>lists len : ", len(data_lists),"</p>")

    print('7. save data to json~')
    functions.saveJsonData(data_lists,'python3')
    
    sleep(1000)
    print('8. done!!!!!!')
    driver.quit()#關閉瀏覽器

    print("--- %s seconds ---" % (time.time() - start_time))

