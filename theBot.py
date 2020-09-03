#for crusoeandsons.com
#login first
# find product id
#add to cart
#input payment details
#submit order

from selenium import webdriver
import time
from info import myinfo
from info import credit_card
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  TimeoutException

gmail= 'michaelameteku@gmail.com'
#finding product id
def urlGen( size,url,raw_size=32768):
    smallest_size = 8
    smallest_size_raw = 34810311737505
    raw_size_diff = raw_size
    url_end = (size - smallest_size)*raw_size_diff + smallest_size_raw
    actual_url = url +str(url_end)
    return actual_url

the_site= urlGen(10,'https://crusoeandsons.com/collections/footwear/products/'
         'nike-mens-air-max-90-premium-shoes-cj0611-100?variant=')
browser = webdriver.Chrome('C:\\Users\\micha\\Downloads\\chromedriver_win32\\chromedriver.exe')
browser.get(the_site)
time.sleep(3)
browser.find_element_by_xpath('//*[@id="product_form_5295911731361"]/div[2]/div/div/div/button[1]').click()
time.sleep(5)

browser.find_element_by_xpath('//*[@id="checkout_email"]').clear()
browser.find_element_by_xpath('//*[@id="checkout_email"]').send_keys(gmail)
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys(myinfo.Fname)
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys(myinfo.Lname)
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys(myinfo.Eaddress)
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys(myinfo.city)
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys(myinfo.Zip)
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys(myinfo.Pnum)
browser.find_element_by_xpath('//*[@id="continue_button"]').click()
try:
    current_element = EC.presence_of_element_located((By.XPATH, '//*[@id="continue_button"]'))
    WebDriverWait(browser,timeout=7).until(current_element)
except TimeoutException:
    print('timed out waiting for continue button')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="continue_button"]').click()
time.sleep(2)
browser.switch_to.frame('google-analytics-sandbox')
try:
    current_element = EC.presence_of_element_located((By.XPATH, '//*[@id="number"]'))
    WebDriverWait(browser,timeout=7).until(current_element)
except TimeoutException:
    print('timed out waiting for card number')
browser.find_element_by_xpath('//*[@id="number"]').send_keys(credit_card.Cnum)
browser.find_element_by_xpath('//*[@id="name"]').send_keys(credit_card.name)
browser.find_elements_by_xpath('//*[@id="expiry"]').clear()
browser.find_elements_by_xpath('//*[@id="expiry"]').send_keys(str(credit_card.month) + '/' + str(credit_card.year))


"""size = int(input('shoe size'))
raw_size= int(input('raw size difference'))
url = input('base url')

addrss = urlGen(size, raw_size,url)
print(str(addrss))"""