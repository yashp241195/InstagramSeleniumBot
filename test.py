# # from selenium import webdriver
# # from os import path 
# # import time, requests
# # from selenium.webdriver.common.keys import Keys

# # def sleep(t=3):
# #     time.sleep(t)

# # def getBrowser():
# #     chromePath = path.abspath('')+'/chromedriver'
# #     browser = webdriver.Chrome(chromePath)
# #     return browser

# # def run():
# #     browser = getBrowser()
# #     sleep(1)    
# #     browser.get("https://en.wikipedia.org/wiki/Albert_Einstein")
# #     sleep(2)
# #     gotofollowDiv = browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table[1]') 
    
# #     with open('test2.txt','w') as f:
# #         f.write(gotofollowDiv.get_attribute('innerHTML'))
    
# #     sleep(2)


# # run()

# from bs4 import BeautifulSoup

# content = ''
# with open('follower_list.html','r') as f:
#     for line in f:
#         content += line

# soup = BeautifulSoup(content, 'html.parser')
# # print(soup.prettify())

# li = list()

# for anchor in soup.find_all('a'):
#     name = anchor.get_text()
#     li.append(name)

# fl = lambda fl : fl != '' 

# li = filter(fl,li)

# follower_list = list(li)

# content = ''
# with open('following_list.html','r') as f:
#     for line in f:
#         content += line

# soup = BeautifulSoup(content, 'html.parser')
# # print(soup.prettify())

# li = list()

# for anchor in soup.find_all('a'):
#     name = anchor.get_text()
#     li.append(name)

# fl = lambda fl : fl != '' 

# li = filter(fl,li)
# following_list = list(li)

# print('\nfollower list',' count= ',len(follower_list),' \n')
# # print(follower_list)
# print('\nfollowing list',' count= ',len(following_list),' \n')
# # print(following_list)



# set_follower = set(follower_list)
# set_following = set(following_list)

# set_dontfollowme = set_following - set_follower
# dontfollowme_list = list(set_dontfollowme)
# print('\nPeople who donot follow artistt.app, count = ',len(dontfollowme_list),'\n')
# print(dontfollowme_list,'\n\n')

# set_Idontfollow = set_follower - set_following
# Idontfollow_list = list(set_Idontfollow)
# print('\nPeople artistt.app dont follow, count = ', len(Idontfollow_list),'\n')
# print(Idontfollow_list,'\n\n')

# with open('idontfollow.txt','w') as f:
#     for item in Idontfollow_list:
#         f.write(item)
#         f.write("\n")

li = list()
with open('notfollowme.txt','r') as f:
    for line in f:
        name = line.split('\n')
        li.append(name[0])


print(len(li))
print(li)
