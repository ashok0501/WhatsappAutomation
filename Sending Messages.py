"""
Whatsapp automation using Python

Source code to send a message to a person.


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


#Now the contact opens and a new textbox is created, so we need to execute this line once again to read the new textbox
search=driver.find_elements_by_class_name(r"_2S1VP")

"""
search[0] -> contact search textbox
search[1] -> message textbox
""" 

#type some messages in message textbox (search[1]) and press enter to send the chat
search[1].send_keys("Hi"+Keys.ENTER)
