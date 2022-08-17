import sys
import io

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ActionChains

#from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


def getChromeOptions():
    return 'a'

chrome_options = Options()

#지정한 user-agent로 설정합니다.
#user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Safari/537.36"
user_agent = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36 '
chrome_options.add_argument('user-agent=' + user_agent)

#chrome_options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.
chrome_options.add_argument('--window-size= x, y') #실행되는 브라우저 크기를 지정할 수 있습니다.
chrome_options.add_argument('--start-maximized') #브라우저가 최대화된 상태로 실행됩니다.
#chrome_options.add_argument('--start-fullscreen') #브라우저가 풀스크린 모드(F11)로 실행됩니다.
#chrome_options.add_argument('--blink-settings=imagesEnabled=false') #브라우저에서 이미지 로딩을 하지 않습니다.
chrome_options.add_argument('--mute-audio') #브라우저에 음소거 옵션을 적용합니다.
chrome_options.add_argument('--user-data-dir=C:/Users/mypc/AppData/Local/Google/Chrome/User Data') #사용자 환경설정 경로
#chrome_options.add_argument('--profile-directory=profile 2') #사용자 환경설정 경로
chrome_options.add_argument('--profile-directory=Default') #사용자 환경설정 경로
#chrome_options.add_argument('incognito') #시크릿 모드의 브라우저가 실행됩니다.

driver = webdriver.Chrome(r'C:\Dev\git\python-study\selenium\files\chromedriver.exe', options=chrome_options)
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

# 사이트 선택
siteList = Select(driver.find_element('id', 'site_code'))
siteList.select_by_index(1)

# 폴더 입력
driver.find_element('id', 'folder').send_keys('1')
time.sleep(1)

# 스크래핑 URL 입력
shoppingUrl = 'https://www.aliexpress.com/af/category/200000369.html?categoryBrowse=y&origin=n&CatId=200000369&spm=a2g0o.productlist.0.0.462a629bVkiHRd&catName=car-electronics'
driver.find_element('id', 'url').send_keys(shoppingUrl)
time.sleep(1)

#불러오기 버튼 클릭
driver.find_element('xpath','//*[@id="getItemButton"]').click()

time.sleep(15)

# 수집 결과의 iframe 페이지로 이동
driver.switch_to.frame('listFrame')

# 페이지 수 입력
pageCnt = 1
pageList = Select(driver.find_element('id', 'e_page'))
pageList.select_by_index(pageCnt-1)

# 페이지 수집 버튼 클릭
#driver.find_element('xpath','/html/body/div[1]/ul[1]/div/form/ul/div[2]/button').click()


#driver.close()

###################################################################################################################
# test = driver.find_element_by_id('username')
#test.send_keys('awefawefawef')


