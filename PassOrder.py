from selenium import webdriver
import time

def passOrder(infos):
    driver = webdriver.Chrome('./chromedriver')

    #Open page
    driver.get(infos['url'])

    #Select Size, Add to cart, Pay
    driver.implicitly_wait(15)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/main/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div/div/select/option[4]').click()
    driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[3]/div/div[1]/div/div/button').click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[3]/div/div[1]/div/div/a/span').click()
    driver.implicitly_wait(10)

    #Email
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/main/div/div/div[2]/div/div/div/div/div/div/div/form/div/div[3]/input[1]').send_keys(infos['mail'])
    driver.find_element_by_xpath('//*[@id="submitLogin"]').click()

    #Personal infos
    driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(infos['first_name'])
    driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(infos['last_name'])
    driver.find_element_by_xpath('//*[@id="address1"]').send_keys(infos['street'])
    driver.find_element_by_xpath('//*[@id="city"]').send_keys(infos['city'])
    driver.find_element_by_xpath('//*[@id="postCode"]').send_keys(infos['zip'])
    driver.find_element_by_xpath('//*[@id="stateCode"]/option[12]').click()
    driver.find_element_by_xpath('//*[@id="phone"]').send_keys(infos['phone'])



    #Payment
        #Go inside iFrame
    driver.switch_to.frame(driver.find_element_by_id("ccframe"))

    driver.find_element_by_xpath('//*[@id="ccNum"]').send_keys(infos['card_number'])
    driver.find_element_by_xpath('//*[@id="holderName"]').send_keys(infos['cc_name'])
    driver.find_element_by_xpath('//*[@id="expiryMonth"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="expiryYear"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="ccCVV"]').send_keys(infos['cvv'])
        #BackToNormal
    driver.switch_to.default_content()

    #driver.find_element_by_xpath('//*[@id="checkoutSubmitButton"]').click()


    while(True):
        pass