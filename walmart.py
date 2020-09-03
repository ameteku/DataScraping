from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH= "C:\\Users\\micha\\Downloads\\chromedriver_win32\\chromedriver.exe"
website= "https://www.walmart.com/ip/Spalding-NBA-29-5-Super-Tack-Pro-Indoor-Outdoor-Basketball/864231503?athcpid=864231503&athpgid=cart&athcgid=null&athznid=bab&athieid=v0&athstid=CS020&athguid=7d893dac-007-1730dc20aa49da&athancid=null&athena=true"
browser = webdriver.Chrome(PATH)
browser.get(website)
time.sleep(3)
option = browser.find_element_by_xpath("//*[@id='variants-section']/div/div/div[2]/label[1]")
option.click()
time.sleep(2)

add_to_cart_button = browser.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button')
add_to_cart_button.click()
time.sleep(2)

go_to_cart = browser.find_element_by_id("header-cart-link")
go_to_cart.click()

time.sleep(2)
checkout = browser.find_element_by_xpath('//*[@id="cart-root-container-content-skip"]/div/div/div[1]/div[2]/div/div/div[2]/div/div/button[1]')
checkout.click()
time.sleep(2)
enterWO_acc = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button')
enterWO_acc.click()
time.sleep(2)
todelveryadd=browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[3]/button')
todelveryadd.click()

#browser.quit()

#shoe = browser.find_element_by_link_text('Air Jordan 3 Retro SE "Animal Instinct 2.0", Black/Black-White-Gorge Green')
#shoe.click()
#size_selector = browser.find_elements_by_xpath('//*[@id="product-select-4544026345506-option-0"]/option[1]')
#size_selector.click()



##browser.close()