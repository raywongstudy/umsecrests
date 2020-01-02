from selenium import webdriver
from selenium.webdriver.common.by import By#for the selector use by
from time import sleep

import io #for the file
import json

from locators.umsecrets_locators import indexPageLocators

class indexPageFunctions(object):

    def clickShowAllComments(driver):
        try:
            driver.execute_script("check = document.querySelectorAll('a[data-testid=\"UFI2ViewOptionsSelector/link\"]');\
                                    for(let i = 0; i < check.length; i++){\
                                        console.log(check[i]);\
                                        check[i].click();\
                                        document.querySelectorAll('div[data-testid=\"UFI2ViewOptionsSelector/menuOption\"]')[2].click()\
                                    }")
        except:
            print('clickShowAllComments error')

    def click_more_btn(driver):
        try:
            #for the more comments button 
            more_btn_all = driver.find_elements(By.CSS_SELECTOR,"a[data-testid=\"UFI2CommentsPagerRenderer/pager_depth_0\"]")
            while len(more_btn_all) > 0:
                driver.execute_script("more_comments = document.querySelectorAll('a[data-testid=\"UFI2CommentsPagerRenderer/pager_depth_0\"]');\
                                        for (let j = 0; j < more_comments.length; j++) {\
                                            more_comments[j].click();\
                                        }")
                sleep(1)
                more_btn_all = driver.find_elements(By.CSS_SELECTOR,"a[data-testid=\"UFI2CommentsPagerRenderer/pager_depth_0\"]")

            #for the comments more comments button
            comment_btn_more = driver.find_elements(By.CSS_SELECTOR,"a[data-testid=\"UFI2CommentsPagerRenderer/pager_depth_1\"]")    

            while len(comment_btn_more) > 0:
                driver.execute_script("comment_mroe = document.querySelectorAll('a[data-testid=\"UFI2CommentsPagerRenderer/pager_depth_1\"]');\
                                        for (let k = 0; k < comment_mroe.length; k++) {\
                                            comment_mroe[k].click();\
                                        }")
                sleep(1)
                comment_btn_more = driver.find_elements(By.CSS_SELECTOR,"a[data-testid=\"UFI2CommentsPagerRenderer/pager_depth_1\"]")    
                
        except:
            print('click_more_btn error')

    def clickPostsDetail(driver):

        try:
            driver.execute_script("check = document.querySelectorAll('"+indexPageLocators.posts_detail_btn+"');\
                                    for(let i =0; i < check.length;i++){\
                                        check[i].click();\
                                    }")
            sleep(1)
            driver.execute_script("check = document.querySelectorAll('"+indexPageLocators.comments_detail_btn+"');\
                                    for(let i =0; i < check.length;i++){\
                                        check[i].click();\
                                    }")
        except:
            print('clickPostsDetail error')


    def find_comments(post):
        try:

            # comment_box => the big comments box 
            comment_box = post.find_element_by_css_selector("._7a9a")

            #data_comments => all comments box
            data_comments = comment_box.find_elements_by_css_selector("._6c7i")

            all_comments = []

            print('    data_comments length:',len(data_comments))
            for data_comment in data_comments:

                comment_name = data_comment.find_element_by_css_selector("._6qw4").text
                comment_text = data_comment.find_element_by_css_selector("._3l3x").text
                comment = {
                    'name' : comment_name,
                    'text' : comment_text
                }
                # print("comment : ",comment)
                all_comments.append(comment)
            return all_comments

        except:
            print("    no comments~")

    def loadMorePosts(driver,times=5):
        for i in range(times):
            sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def delLoginBanner(driver):
        driver.find_element_by_css_selector("._62up").click()
        driver.execute_script("document.getElementById('"+indexPageLocators.banner+"').style.display='none'")
        sleep(1)

    def saveJsonData(data,python_version):
        if python_version == 'python3':
            # for python 3
            with open('data.json', 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)
        elif python_version == 'python2':
            #for python 2
            with io.open('data.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=4))

# ---------------------------here not use--------------------------------
class oldFunctions():
    def clickShowAllComments(driver):
        #find all the most relevant button
        try:
            option_buttons = driver.find_elements_by_link_text("Most Relevant")
                # print('all option buttons len:',len(option_buttons))

            # driver find element from top to down 
            driver.execute_script("window.scrollTo(0,0)")
            #click the button to make the option_menus show 
            for option_button in option_buttons:
                option_button.click()

            #find all the all_comments button
            option_menus = driver.find_elements(By.CSS_SELECTOR,"div[data-testid='UFI2ViewOptionsSelector/menuRoot'] li:last-child a")
                # print('all option menus len:',len(option_menus))

            # driver find element from top to down 
            driver.execute_script("window.scrollTo(0,0)")

            #for loop to click all option_buttons and click the option_menus button
            for i in range(len(option_buttons)):
                option_buttons[i].click()
                option_menus[i].click()
        except:
            print("fail click show all comments function")

    # click comments more button
    def click_more_btn(driver):
        # driver.execute_script("all_more_btn = document.querySelectorAll('._4sxc._42ft');for(i=0;i<all_more_btn.length;i++){all_more_btn[i].click()}")
        try:
            # driver find element from top to down 
            driver.execute_script("window.scrollTo(0,0)")

            more_btn_all = driver.find_elements(By.CSS_SELECTOR,"._4sxc._42ft")

            while len(more_btn_all) > 0:
                print('run one time')
                for more_btn in more_btn_all:
                    more_btn.click()
                    print('click')

                driver.execute_script("window.scrollTo(0,0)")
                sleep(1.5)
                more_btn_all = driver.find_elements(By.CSS_SELECTOR,"._4sxc._42ft")
                print('more btn all :',more_btn_all)
                print('more btn all len:',len(more_btn_all))
                print('run one time end')

        except:
            print("fail click more buttons function")
