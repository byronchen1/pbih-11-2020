import time
import pandas as pd
from selenium import webdriver


def glass_door(ticker, address, usr, pwd):                       
    driver = webdriver.Chrome() 
    login = 'https://www.glassdoor.ca/profile/login_input.htm'
    driver.get(login)
    email_field = driver.find_element_by_name('username').send_keys(usr)
    password_field = driver.find_element_by_name('password').send_keys(pwd)
    submit_btn = driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(3)
    
    driver.get(address)
    desc=[]
    try:
        for i in range(10):
            elems = driver.find_elements_by_xpath('.//li[@class = "empReview cf  "]')
            for e in elems:
                cdate = e.find_element_by_xpath('.//time[@class = "date subtle small"]').text
                crate = e.find_element_by_xpath('.//div[@class = "v2__EIReviewsRatingsStylesV2__ratingNum v2__EIReviewsRatingsStylesV2__small"]').text
                desc.append([cdate,crate])
            next_ = driver.find_element_by_class_name('pagination__PaginationStyle__next').find_element_by_tag_name('a')
            driver.get(next_.get_attribute('href'))
    except:
        pass
    df=pd.DataFrame(desc)
    df.to_csv(f'df_{ticker}.csv', columns=['Date', 'Rating'], index=False)
    driver.close()
    
companies = {'wcn':'https://www.glassdoor.ca/Reviews/Waste-Connections-Reviews-E7903.htm',
            'zts':'https://www.glassdoor.ca/Reviews/Zoetis-Reviews-E680848.htm',
            'txn':'https://www.glassdoor.ca/Reviews/Texas-Instruments-Reviews-E651.htm',    
            'tjx':'https://www.glassdoor.ca/Reviews/The-TJX-Companies-Inc-Reviews-E639.htm',
            'tmo':'https://www.glassdoor.ca/Reviews/Thermo-Fisher-Scientific-Reviews-E658.htm',
            'vrsk':'https://www.glassdoor.ca/Reviews/Verisk-Analytics-Reviews-E140233.htm',
            'idex':'https://www.glassdoor.ca/Reviews/IDEX-Reviews-E344.htm',
            'bdx':'https://www.glassdoor.ca/Reviews/BD-Reviews-E88.htm',
             'dhr':'https://www.glassdoor.ca/Reviews/Danaher-Reviews-E193.htm',
             'hei':'https://www.glassdoor.ca/Reviews/HEICO-Reviews-E886.htm',
             'lin':'https://www.glassdoor.ca/Reviews/Linde-Reviews-E10436.htm',
             'mtd':'https://www.glassdoor.ca/Reviews/Mettler-Toledo-Reviews-E7144.htm',
             'cb':'https://www.glassdoor.ca/Reviews/Chubb-Reviews-E150.htm',
             'brk':'https://www.glassdoor.ca/Reviews/Berkshire-Hathaway-Reviews-E805672.htm',
             'sq':'https://www.glassdoor.ca/Reviews/Square-Reviews-E422050.htm',
             'v':'https://www.glassdoor.ca/Reviews/Visa-Inc-Reviews-E3035.htm',
             'mmm':'https://www.glassdoor.ca/Reviews/3M-Reviews-E446.htm',
             'ko':'https://www.glassdoor.ca/Reviews/The-Coca-Cola-Company-Reviews-E161.htm',
             'hd':'https://www.glassdoor.ca/Reviews/The-Home-Depot-Reviews-E655.htm',
             'nke':'https://www.glassdoor.ca/Reviews/NIKE-Reviews-E1699.htm',
             'twdc':'https://www.glassdoor.ca/Reviews/Walt-Disney-Company-Reviews-E717.htm',
             'cost':'https://www.glassdoor.ca/Reviews/Costco-Wholesale-Reviews-E2590.htm',
             'jnj':'https://www.glassdoor.ca/Reviews/Johnson-and-Johnson-Reviews-E364.htm',
             'cmcsa':'https://www.glassdoor.ca/Reviews/Comcast-Reviews-E1280.htm',
             'msft':'https://www.glassdoor.ca/Reviews/Microsoft-Reviews-E1651.htm',
             'mcd':'https://www.glassdoor.ca/Reviews/McDonald-s-Reviews-E432.htm',
            }
            
            
 if __name__ == '__main__':
    username = ''
    password = ''
    for co, link in zip(companies.keys(),companies.values()):
        try:
            glass_door(co, link, username, password)
        except:
            continue
