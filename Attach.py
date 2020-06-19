"""
Whatsapp automation using Python

Source code to send an attachmnt to a person.




Important: This source code should be executed one after another with atleast 2 secs waiting time 
between each code.

This waiting time is because, the browser should load the content (based on the speed of your
internet connection the waiting time may increase/decrease).

If you want to execute all the codes at once, then you should add waiting time.

Waiting time is added by the following code


import time
time.sleep(2)   #waiting time for 2 secs.

the waiting time code should be added between all the code operation.

"""

#import the webdriver from selenium package
from selenium import webdriver

#import the keys class from selenium package
from selenium.webdriver.common.keys import Keys


#initialize the web driver variable
driver = webdriver.Chrome(executable_path = r"") #give the path of the web driver in the string

#browse to a whatsapp web
driver.get(r"https://web.whatsapp.com") 

#control the contact search textbox
search=driver.find_elements_by_class_name(r"_2S1VP")

#type the required contact name and click enter to open up the chat
search[0].send_keys(r""+Keys.ENTER) #type the contact name in this string

#control the attach button
attach=driver.find_element_by_xpath(r'//*[@title="Attach"]')  

#click the attach button
attach.click()

#control the open dialog
dialog=driver.find_element_by_tag_name(r"input")

#send a file to open dialog
dialog.send_keys(r"") #this string contains the path of the file to be uploaded
#NOTE: if the file is large, then upload time will be high. If it takes some time to upload, then the preview window also takes some time to load
#so, its better to ask the program to wait
#this is done by the following code
"""
import time
time.sleep(2) #wait for 2 secs
#this step is not required when you execute the code step by step
"""

#after the upload is completed, a preview window is opened
#in the preview window, there is a send button
#the below code controls the send button
but=driver.find_element_by_class_name(r"_3hV1n")

#click the send button
but.click()