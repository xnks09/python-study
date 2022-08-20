from genericpath import isfile
import sys
import io
import sys
import os.path       
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math
import numpy as np
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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


beforeDf = pd.read_excel('C:/자동화폴더/상품목록.xlsx', engine = "openpyxl", usecols='B,C,D,E,F', header=0, sheet_name='list')

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

beforeDf.rename(columns = {'검색 키워드' : 'keyword', '제목' : 'title','검색어' : 'search','쿠팡 카테고리' : 'category','무게' : 'weight',}, inplace = True)

df = pd.DataFrame(columns=['keyword', 'title','search','category','weight'])

print()
print()
print('[엑셀 데이터 및 유효성 체크 중..........................................]')
for product in range(len(beforeDf.index)):

    keyword = ''
    title = ''
    search = ''
    category = ''
    weight = ''
    
    keyword = str(beforeDf.iloc[product, 0])
    title = str(beforeDf.iloc[product, 1])
    search = str(beforeDf.iloc[product, 2])
    category = str(beforeDf.iloc[product, 3])
    weight = str(int(beforeDf.iloc[product, 4]))
    
    df.loc[product] =[keyword, title, search, category, weight]    

print('[엑셀 데이터 및 유효성 체크 종료..........................................]')

print('[데이터 수집 시작 - ', len(df.index),'건]')
for product1 in range(len(df.index)):
    # print(df.iloc[product1, 0])
    # print(df.iloc[product1, 1])
    # print(df.iloc[product1, 2])
    # print(df.iloc[product1, 3])
    # print(df.iloc[product1, 4])
    print("==============================================================================")

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

driver.get('https://mr-seo.co.kr/mr_product/list')

time.sleep(10)

############################################# 등록 처리 ###########################################################

for productList in range(len(df.index)):
    
    # 폴더입력
    folderList = Select(driver.find_element('id', 'product_folder'))
    folderList.select_by_value(df.iloc[productList, 0])
    
    # 조회버튼 클릭
    driver.find_element('xpath','//*[@id="submit"]').click()
    time.sleep(5)

    # 수집 결과의 iframe 페이지로 이동
    driver.switch_to.frame('listFrame')

    # 리스팅 숫자를 500으로 변경
    listingList = Select(driver.find_element('id', 'rScaleList'))
    listingList.select_by_value('500')
    
    time.sleep(10)
    
    # 전체선택
    driver.find_element('xpath','//*[@id="all_chk"]').click()
    
    # 무게 변경 설정 및 무게변경 버튼 클릭
    print('[무게 설정을 시작합니다..........................................]')
    weightList = Select(driver.find_element('id', 're_wgt'))
    weightList.select_by_value(df.iloc[productList, 4])
    driver.find_element('xpath','//*[@id="listContainer"]/ul/li[5]/button').click()

    # 무게 설정 변경에 대한 alert처리
    wait = WebDriverWait(driver, 9999999999999999999999)
    element = wait.until(EC.alert_is_present())
    alert_result = driver.switch_to.alert
    print(alert_result.text)
    alert_result.accept()
    print('[무게 설정이 완료되었습니다...........................................]')
    
    # 일괄 카테고리 편집
    print('[일괄 카테고리 편집을 시작합니다..........................................]')
    driver.find_element('xpath','//*[@id="listContainer"]/ul/li[6]/button').click()
    time.sleep(2)
    driver.switch_to.parent_frame() # 상위 프레임으로 재이동
    driver.find_element('xpath','//*[@id="commerce_coupang"]/td/div[1]/button').click() # 쿠팡 카테고리 매핑 버튼 클릭
    time.sleep(1)
    driver.find_element('name', 'categoryMappingTitle').send_keys(df.iloc[productList, 3]) # 카테고리 문자 복사
    driver.find_element('xpath','//*[@id="categoryMappingModal"]/div/div[2]/div[1]/button').click() # 검색 버튼 클릭
    time.sleep(1)
    driver.find_element('xpath','//*[@id="setRecommendCoupangCategoryButton"]').click() # 카테고리 변경 클릭
    time.sleep(1)
    driver.find_element('xpath','//*[@id="categoryMappingModal"]/div/div[3]/button').click() # 적용 버튼 클릭
    time.sleep(1)
    driver.find_element('xpath','//*[@id="setCategoryButton"]').click() # 부모 페이지의 적용 버튼 클릭

    # 일괄 카테고리 변경에 대한 alert처리
    wait = WebDriverWait(driver, 9999999999999999999999)
    element = wait.until(EC.alert_is_present())
    alert_result = driver.switch_to.alert
    print(alert_result.text)
    alert_result.accept()
    print('[일괄 카테고리 편집이 완료되었습니다.........................................]')
    
    # 일괄 제목 설정   
    print('[일괄 제목 설정을 시작합니다..........................................]')
    # 수집 결과의 iframe 페이지로 이동
    driver.switch_to.frame('listFrame')
    driver.find_element('xpath','//*[@id="listContainer"]/ul/li[7]/button').click() # 일괄 제목 변경 클릭
    time.sleep(2)
    driver.switch_to.parent_frame() # 상위 프레임으로 재이동
    time.sleep(1)
    driver.find_element('xpath','//*[@id="titleModal"]/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[1]/input[1]').clear()
    time.sleep(1)
    driver.find_element('xpath','//*[@id="titleModal"]/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[1]/input[1]').send_keys(100) # 글자수를 100으로 변경
    #driver.find_element('name', 'maxKeyword').send_keys(100) # 글자수를 100으로 변경
    driver.find_element('name', 'brandName').send_keys('구미호 협력사') # 브랜드명 입력
    originalTitle = df.iloc[productList, 1]
    originalTitleLength = len(originalTitle)
    enrollTitle = originalTitle.ljust(originalTitleLength+1, ' ')   
    driver.find_element('name', 'title_front_text').send_keys(enrollTitle) # 제목 입력
    
    keywordDelete = originalTitle.replace(' ', ',')
    driver.find_element('name', 'titleOverlap').send_keys(keywordDelete) # 키워드 제거 입력
    time.sleep(1)
    driver.find_element('xpath','//*[@id="titleModal"]/div/div/div[2]/div[1]/div/table/tbody/tr[3]/td[3]/button').click() # 제거버튼 클릭 클릭
    time.sleep(3)
    driver.find_element('xpath','//*[@id="titleModal"]/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[4]/button').click() # 글자수 적용버튼 클릭 클릭
    time.sleep(2)
    driver.find_element('xpath','//*[@id="setTitleButton"]').click() # 최종 적용버튼 클릭 클릭

    # 일괄 제목 설정에 대한 alert처리
    wait = WebDriverWait(driver, 9999999999999999999999)
    element = wait.until(EC.alert_is_present())
    alert_result = driver.switch_to.alert
    print(alert_result.text)
    alert_result.accept()
    print('[일괄 제목 설정이 완료되었습니다.........................................]')
    # 일괄 키워드 설정   
    print('[일괄 키워드 설정을 시작합니다..........................................]')
    # 수집 결과의 iframe 페이지로 이동
    driver.switch_to.frame('listFrame')
    driver.find_element('xpath','//*[@id="listContainer"]/ul/li[8]/button').click() # 일괄 키워드 편집 클릭
    time.sleep(2)
    driver.switch_to.parent_frame() # 상위 프레임으로 재이동
    time.sleep(1)
    driver.find_element('name', 'addText').send_keys(df.iloc[productList, 2]) # 적용된 검색어 입력
    driver.find_element('name', 'addText').send_keys(Keys.ENTER) # 엔터키 입력
    time.sleep(1)
    driver.find_element('xpath','//*[@id="keywordMain"]/div/div[1]/button[3]').click() # 적용 버튼 클릭
    
    # 일괄 키워드 설정에 대한 alert처리
    wait = WebDriverWait(driver, 9999999999999999999999)
    element = wait.until(EC.alert_is_present())
    alert_result = driver.switch_to.alert
    print(alert_result.text)
    alert_result.accept()
    print('[일괄 키워드 설정이 완료되었습니다.........................................]')
    
    
    
    # 최종 업로드 처리
    # 수집 결과의 iframe 페이지로 이동
    driver.switch_to.frame('listFrame')
    driver.find_element('xpath','//*[@id="listContainer"]/ul/li[11]/button').click() # 업로드 버튼 클릭
    time.sleep(1)
    driver.find_element('xpath','//*[@id="listContainer"]/ul/li[11]/div/div[2]/ul/div/button').click() # 쿠팡 선택 버튼 클릭

    # 일괄 연동 시스템에 대한 메시지 confirm창 처리
    wait = WebDriverWait(driver, 9999999999999999999999)
    element = wait.until(EC.alert_is_present())
    alert_result = driver.switch_to.alert
    print(alert_result.text)
    alert_result.accept()
    
    
    print('[업로드를 시작합니다..........................................]')
    
    # 업로드에 대한 alert 처리
    wait = WebDriverWait(driver, 9999999999999999999999)
    element = wait.until(EC.alert_is_present())
    alert_result = driver.switch_to.alert
    print(alert_result.text)
    alert_result.accept()   
    print('[업로드가 완료되었습니다.........................................]')
    
    driver.get('https://mr-seo.co.kr/mr_product/list')

    time.sleep(10)
    
    
#    if df.iloc[productList, 0] != '':   
#        # 사이트 선택
#        siteList = Select(driver.find_element('id', 'site_code'))
#        siteList.select_by_index(1)
#
#        print(df.iloc[productList, 4])
#        # 폴더 입력
#        driver.find_element('id', 'folder').send_keys(df.iloc[productList, 4])
#        time.sleep(1)
#
#        # 스크래핑 URL 입력
#        driver.find_element('id', 'url').send_keys(str(df.iloc[productList, 0]))
#        time.sleep(1)
#
#        #불러오기 버튼 클릭
#        driver.find_element('xpath','//*[@id="getItemButton"]').click()
#
#        time.sleep(15)
#
#        # 수집 결과의 iframe 페이지로 이동
#        driver.switch_to.frame('listFrame')
#
#        # 페이지 수 입력
#        
#        pageCnt = int(df.iloc[productList, 1])
#        pageList = Select(driver.find_element('id', 'e_page'))
#        pageList.select_by_index(pageCnt-1)
#        
#        time.sleep(5)
#
#        driver.find_element('xpath','//*[@id="checkItemUpdate"]').click()
#        
#        wait = WebDriverWait(driver, 9999999999999999999999)
#        element = wait.until(EC.alert_is_present())
#        alert_result = driver.switch_to.alert
#        print(alert_result.text)
#        alert_result.accept()
#        
#        driver.get('https://mr-seo.co.kr/mr_product/regist')
#
#        time.sleep(3)
#
#        # 대량수집 버튼 클릭
#        driver.find_element('xpath','//*[@id="searchFrm"]/table/tbody/tr[1]/td[1]/label[1]/input').click()
#        
#    
#    if df.iloc[productList, 2] != '':   
#
#        # 사이트 선택
#        siteList = Select(driver.find_element('id', 'site_code'))
#        siteList.select_by_index(10)
#
#        # 폴더 입력
#        driver.find_element('id', 'folder').send_keys(df.iloc[productList, 4])
#        time.sleep(1)
#
#        # 스크래핑 URL 입력
#        driver.find_element('id', 'url').send_keys(str(df.iloc[productList, 2]))
#        time.sleep(1)
#
#        #불러오기 버튼 클릭
#        driver.find_element('xpath','//*[@id="getItemButton"]').click()
#
#        time.sleep(15)
#
#        # 수집 결과의 iframe 페이지로 이동
#        driver.switch_to.frame('listFrame')
#
#        # 페이지 수 입력
#        
#        pageCnt = int(df.iloc[productList, 3])
#        pageList = Select(driver.find_element('id', 'e_page'))
#        pageList.select_by_index(pageCnt-1)
#        
#        time.sleep(10)
#
#        driver.find_element('xpath','//*[@id="checkItemUpdate"]').click()
#        
#        wait = WebDriverWait(driver, 9999999999999999999999)
#        element = wait.until(EC.alert_is_present())
#        alert_result = driver.switch_to.alert
#        print(alert_result.text)
#        alert_result.accept()
#
#        driver.get('https://mr-seo.co.kr/mr_product/regist')
#
#        time.sleep(3)
#
#        # 대량수집 버튼 클릭
#        driver.find_element('xpath','//*[@id="searchFrm"]/table/tbody/tr[1]/td[1]/label[1]/input').click()
#        
#        #페이지 수집 버튼 클릭
#        #driver.find_element('xpath','/html/body/div[1]/ul[1]/div/form/ul/div[2]/button').click()
#        #driver.close()
#
#
####################################################################################################################
## test = driver.find_element_by_id('username')
##test.send_keys('awefawefawef')
#
#
#