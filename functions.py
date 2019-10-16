def test():
    print("hello world")

def click_more_btn(driver):
    driver.execute_script("all_more_btn = document.querySelectorAll('._4sxc._42ft');for(i=0;i<all_more_btn.length;i++){all_more_btn[i].click()}")
    driver.execute_script("all_more_btn = document.querySelectorAll('._4sxc._42ft');for(i=0;i<all_more_btn.length;i++){all_more_btn[i].click()}")
    driver.execute_script("all_more_btn = document.querySelectorAll('._4sxc._42ft');for(i=0;i<all_more_btn.length;i++){all_more_btn[i].click()}")
    print("run click more btn funtion ")
    # more_btn_all = driver.find_elements_by_css_selector("._4sxc._42ft")
    # print("more_btn_all : ", more_btn_all)
    # for more_btn in more_btn_all:
    #     print("more_btn : ",more_btn)
    #     more_btn.click()

def find_comments(post):
    try:
        print("run find_comments function")
        #the UFI2CommentsList/root_depth_0 next element , just for comments is ul > li ! we selector ul
        comment_box = post.find_element_by_css_selector("._7a9a")
        print("comment_box : ",comment_box)
        # try:
        #     comment_more_btn = comment_box.find_element_by_css_selector("._4sxc._42ft")
        #     print("run comment_more_btn : ",comment_more_btn)
        #     comment_more_btn.click()
        # except:
        #     sleep(.5)

        data_comments = comment_box.find_elements_by_css_selector("._6c7i")
        print("data_comments : ", data_comments)
        all_comments = []
        for data_comment in data_comments:
            comment_name = data_comment.find_element_by_css_selector("._6qw4").text
            print("comment_name :",comment_name)
            comment_text = data_comment.find_element_by_css_selector("._3l3x").text
            print("comment_text :",comment_text)
            comment = {
                'name' : comment_name,
                'text' : comment_text
            }
            print("comment : ",comment)
            all_comments.append(comment)
        return all_comments
    except:
        print("error the find_comments function")

