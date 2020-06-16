from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


def new_chat(user_name,message):
    

    search= chrome_browser.find_element_by_xpath('//div[@class="_2EoyP"]')
    search.click()

    search_user= chrome_browser.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    search_user.send_keys(user_name)

    time.sleep(5)

    try:
        user= chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('"{}" does not appear in your contact list '. format(user_name))
    
    message_bot= chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
    message_bot.send_keys(message)
    send= chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
    send.click()
    

def create_group(users,group_subject):
    menu=chrome_browser.find_element_by_xpath('//div[@title="Menu"]')
    menu.click()

    group=chrome_browser.find_element_by_xpath('//div[@class="Ut_N0 n-CQr"]')
    group.click()
    for user in users:
        add_person=chrome_browser.find_element_by_xpath('//input[@class="_17ePo copyable-text selectable-text"]')
        add_person.send_keys(user)
        add_user= chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user))
        add_user.click()
        time.sleep(2)

    time.sleep(2)    
    next1=chrome_browser.find_element_by_xpath('//div[@class="_3y5oW"]')
    next1.click()

    time.sleep(2)
    group_name=chrome_browser.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    group_name.send_keys(group_subject)

    time.sleep(2)
    next2=chrome_browser.find_element_by_xpath('//div[@class="_3y5oW"]')
    next2.click()




def broadcast(users,message):
    for user in users:
        new_chat(user,message)




  
print("HELLO WELCOME TO AUTOMATED WHATSAPP")
print("CHOOSE FROM THE FOLLOWING OPTIONS:")
print("1. Start a new chat")
print("2. Create a group")
print("3. Broadcast message to multiple people")
print("\n")
choice=int(input("Enter you choice:"))
#skipping qr code
skip_QR_code=webdriver.ChromeOptions()
skip_QR_code.add_argument('--user-data-dir=C:\\Users\\Sanjay Gupta\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
skip_QR_code.add_argument('--profile-directory=Default')
#registering the driver
chrome_browser=webdriver.Chrome(executable_path='H:/chromedriver', options=skip_QR_code)
chrome_browser.get('https://web.whatsapp.com/')
#time given to load whatsapp completely
time.sleep(10)

if choice==1:
    user_name=input("Enter name:")
    message=input("Enter the message to be sent:")
    new_chat(user_name,message)
    
elif choice==2:
    users=[]
    n = int(input("Enter number of users : "))
    for i in range(0, n): 
        user = input("Enter user") 
        users.append(user)
    group_subject=input("Enter group name")
    create_group(users,group_subject)
elif choice==3:
    message=input("Enter the message to be sent:")
    users=[]
    n = int(input("Enter number of users : "))
    for i in range(0, n): 
        user = input("Enter user") 
        users.append(user)
    broadcast(users,message)