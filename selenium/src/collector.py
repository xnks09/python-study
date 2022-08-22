from genericpath import isfile
import sys
import io
import sys
import os.path       
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import numpy as np
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# from selenium.webdriver import ActionChains

#from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

import pandas as pd
import openpyxl

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# Chrome 브라우저 옵션을 설정
def getChromeOptions(profile):
    
    chrome_options = Options()

    user_agent = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Safari/537.36 '
    chrome_options.add_argument('user-agent=' + user_agent)
    #chrome_options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.
    chrome_options.add_argument('--window-size= x, y') #실행되는 브라우저 크기를 지정할 수 있습니다.
    chrome_options.add_argument('--start-maximized') #브라우저가 최대화된 상태로 실행됩니다.
    #chrome_options.add_argument('--start-fullscreen') #브라우저가 풀스크린 모드(F11)로 실행됩니다.
    #chrome_options.add_argument('--blink-settings=imagesEnabled=false') #브라우저에서 이미지 로딩을 하지 않습니다.
    chrome_options.add_argument('--mute-audio') #브라우저에 음소거 옵션을 적용합니다.
    chrome_options.add_argument('--user-data-dir=C:/Users/mypc/AppData/Local/Google/Chrome/User Data') #사용자 환경설정 경로
    #chrome_options.add_argument('--profile-directory=profile 2') #사용자 환경설정 경로
    #chrome_options.add_argument('--profile-directory=Default') #사용자 환경설정 경로
    chrome_options.add_argument('--profile-directory='+profile)
    #chrome_options.add_argument('incognito') #시크릿 모드의 브라우저가 실행됩니다.
    
    return chrome_options

####################################################################################################################

excelFile = 'C:/자동화폴더/상품목록.xlsx'

try:
    if os.path.isfile(excelFile):
        print('상풍목록 엑셀 파일이 잘 있네~~')
        print('이제 수집을 시작해볼게용~~♡')
    else:
        raise
except:
    print('==================================================================================')
    print('Oops!!!')
    print('쟈기~상품목록 파일이 없네~~?')
    print('자자..아래를 참고해서 경로에 파일을 넣어줘~')
    print('C:/자동화폴더/상품목록.xlsx')
    print('==================================================================================')
    sys.exit(1)


beforeDf = pd.read_excel('C:/자동화폴더/상품목록.xlsx', engine = "openpyxl", usecols='I,J,K,L,N', header=0, sheet_name='list')

productCnt = len(beforeDf.index)

try:
    if productCnt < 1:
        raise
    else:
        print('==================================================================================')
        print('엑셀을 잘 읽은 것 같앙~')
        print('이제 시작할꺼야~')
        print('==================================================================================')
except:
    print('==================================================================================')
    print('Oops!!!')
    print('쟈갸 엑셀에 파일에 수집할 목록이 없쩌!!!')
    print('수집 상품을 등록해주세용~~♡')
    print('==================================================================================')
    sys.exit(1)

beforeDf.rename(columns = {'알리익스프레스' : 'ali', '알리_페이지' : 'ali_page','타오바오' : 'tao','타오_페이지' : 'tao_page','미서폴더' : 'folder',}, inplace = True)

df = pd.DataFrame(columns=['ali', 'ali_page','tao','tao_page','folder'])

print()
print()
print('[엑셀 데이터 및 유효성 체크 중..........................................]')
for product in range(len(beforeDf.index)):

    # 알리익스플레스 또는 타오바오 둘 다 없는 경우 예외 발생!!!
    try:
        if str(type(beforeDf.iloc[product, 0])) == "<class 'float'>" and str(type(beforeDf.iloc[product, 2])) == "<class 'float'>":
            raise
    except:
        print('==================================================================================')
        print('Oops!!!')
        print('알리하고 타오바오 주소 둘 다 없는게 있어서 종료할게~~~')
        print('다시 확인하고 프로그램 돌려줭~')
        print('==================================================================================')
        sys.exit(1)

    # 알리익스플레스가 값이 있는데 알리 페이지가 없는 경우
    if(str(type(beforeDf.iloc[product, 0])) != "<class 'float'>"):
        try:
            if(np.isnan(beforeDf.iloc[product, 1])):
                raise
        except:
            print('==================================================================================')
            print('Oops!!!')
            print('알리 페이지가 숫자가 아니거나 내용이 없는게 있어서 종료할게~~~')
            print('다시 확인하고 프로그램 돌려줭~')
            print('==================================================================================')
            sys.exit(1)
    print('check')

    # 타오바오가 값이 있는데 타오 페이지가 없는 경우
    if(str(type(beforeDf.iloc[product, 2])) != "<class 'float'>" and str(type(beforeDf.iloc[product, 2])) != "<class 'numpy.float64'>"):
        try:
            if(np.isnan(beforeDf.iloc[product, 3])):
                raise
        except:
            print('==================================================================================')
            print('Oops!!!')
            print('타오 페이지가 숫자가 아니거나 내용이 없는게 있어서 종료할게~~~')
            print('다시 확인하고 프로그램 돌려줭~')
            print('==================================================================================')
            sys.exit(1)               

    # 미서폴더에 내용이 없는 경우
    if str(type(beforeDf.iloc[product, 4])) == "<class 'float'>":
        try: 
            if(np.isnan(beforeDf.iloc[product, 4])):
                raise
        except:
            print('==================================================================================')
            print('Oops!!!')
            print('미서 폴더에 값이 없는게 있네~~~~')
            print('다시 확인하고 프로그램 돌려줭~')
            print('==================================================================================')
            sys.exit(1)
  

    ali = ''
    tao = ''
    ali_page = ''
    tao_page = ''
    
    if(str(type(beforeDf.iloc[product, 0])) != "<class 'float'>"):
        ali = str(beforeDf.iloc[product, 0])
        ali_page = str(int(beforeDf.iloc[product, 1]))
    else:
        ali = ''

       
    if(str(type(beforeDf.iloc[product, 2])) != "<class 'float'>" and str(type(beforeDf.iloc[product, 2])) != "<class 'numpy.float64'>"):
        tao = str(beforeDf.iloc[product, 2])
        tao_page = str(int(beforeDf.iloc[product, 3]))
    else:
        tao = ''
    
    folder = ''
    
    if str(type(beforeDf.iloc[product, 4])) == "<class 'float'>":
        folder = str(int(beforeDf.iloc[product, 4]))
    else:
        folder = beforeDf.iloc[product, 4]
        
    df.loc[product] =[ali, ali_page, tao, tao_page, folder]    

print('[엑셀 데이터 및 유효성 체크 종료..........................................]')

print('[데이터 수집 시작 - ', len(df.index),'건]')
for product1 in range(len(df.index)):
    # print(df.iloc[product1, 0])
    # print(df.iloc[product1, 1])
    # print(df.iloc[product1, 2])
    # print(df.iloc[product1, 3])
    # print(df.iloc[product1, 4])
    print("==============================================================================")

#print(df.iloc[0])
#print(df.iloc[1])


driver = webdriver.Chrome(r'C:\Dev\git\python-study\selenium\files\chromedriver.exe', options=getChromeOptions('Default'))
#driver = webdriver.Remote('http://localhost:4444/wd/hub', chrome_options.to_capabilities())
url = 'https://mr-seo.co.kr/auth/login'
driver.get(url)


############################################# 로그인 처리 ###########################################################
userId = driver.find_element('id', 'am_id')
userId.send_keys('shooting113')

userPwd = driver.find_element('id', 'am_pwd')
userPwd.send_keys('wpdl0907!')

loginButton = driver.find_element('xpath','//*[@id="loginBox"]/form/div/ul/li[3]/input')
loginButton.click()

time.sleep(5)

driver.get('https://mr-seo.co.kr/mr_product/regist')

time.sleep(3)

# 대량수집 버튼 클릭
driver.find_element('xpath','//*[@id="searchFrm"]/table/tbody/tr[1]/td[1]/label[1]/input').click()


for productList in range(len(df.index)):
    
    if df.iloc[productList, 0] != '':   
        # 사이트 선택
        siteList = Select(driver.find_element('id', 'site_code'))
        siteList.select_by_index(1)

        print(df.iloc[productList, 4])
        # 폴더 입력
        driver.find_element('id', 'folder').send_keys(df.iloc[productList, 4])
        time.sleep(1)

        # 스크래핑 URL 입력
        driver.find_element('id', 'url').send_keys(str(df.iloc[productList, 0]))
        time.sleep(1)

        #불러오기 버튼 클릭
        driver.find_element('xpath','//*[@id="getItemButton"]').click()

        time.sleep(15)

        # 수집 결과의 iframe 페이지로 이동
        driver.switch_to.frame('listFrame')

        # 페이지 수 입력
        
        pageCnt = int(df.iloc[productList, 1])
        pageList = Select(driver.find_element('id', 'e_page'))
        pageList.select_by_index(pageCnt-1)
        
        time.sleep(5)

        driver.find_element('xpath','//*[@id="checkItemUpdate"]').click()
        
        wait = WebDriverWait(driver, 9999999999999999999999)
        element = wait.until(EC.alert_is_present())
        alert_result = driver.switch_to.alert
        print(alert_result.text)
        alert_result.accept()
        
        driver.get('https://mr-seo.co.kr/mr_product/regist')

        time.sleep(3)

        # 대량수집 버튼 클릭
        driver.find_element('xpath','//*[@id="searchFrm"]/table/tbody/tr[1]/td[1]/label[1]/input').click()
        
    
    if df.iloc[productList, 2] != '':   

        # 사이트 선택
        siteList = Select(driver.find_element('id', 'site_code'))
        siteList.select_by_index(10)

        # 폴더 입력
        driver.find_element('id', 'folder').send_keys(df.iloc[productList, 4])
        time.sleep(1)

        # 스크래핑 URL 입력
        driver.find_element('id', 'url').send_keys(str(df.iloc[productList, 2]))
        time.sleep(1)

        #불러오기 버튼 클릭
        driver.find_element('xpath','//*[@id="getItemButton"]').click()

        time.sleep(15)

        # 수집 결과의 iframe 페이지로 이동
        driver.switch_to.frame('listFrame')

        # 페이지 수 입력
        
        pageCnt = int(df.iloc[productList, 3])
        pageList = Select(driver.find_element('id', 'e_page'))
        pageList.select_by_index(pageCnt-1)
        
        time.sleep(10)

        driver.find_element('xpath','//*[@id="checkItemUpdate"]').click()
        
        wait = WebDriverWait(driver, 9999999999999999999999)
        element = wait.until(EC.alert_is_present())
        alert_result = driver.switch_to.alert
        print(alert_result.text)
        alert_result.accept()

        driver.get('https://mr-seo.co.kr/mr_product/regist')

        time.sleep(3)

        # 대량수집 버튼 클릭
        driver.find_element('xpath','//*[@id="searchFrm"]/table/tbody/tr[1]/td[1]/label[1]/input').click()
        
        #페이지 수집 버튼 클릭
        #driver.find_element('xpath','/html/body/div[1]/ul[1]/div/form/ul/div[2]/button').click()
        #driver.close()


###################################################################################################################
# test = driver.find_element_by_id('username')
#test.send_keys('awefawefawef')


