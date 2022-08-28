from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import os
from pathlib import Path
import component.utility as utility
import component.log as log

logger = log.getLogger("common")

userList = {
    '1번': {'userId': 'shooting113', 'password': 'wpdl0907!', 'profile': 'Default'},
    '2번': {'userId': 'rnsoskfk2', 'password': 'wpdl0907!', 'profile': 'Default'},
    '3번': {'userId': 'rnsoskfk3', 'password': 'dlwpdl0907!', 'profile': 'Default'}
}

def getChromeOptions(profile):
      
    chrome_options = Options()
    
    userPath = utility.getUserHome()
    
    user_agent = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Safari/537.36 '
    chrome_options.add_argument('user-agent=' + user_agent)
    #chrome_options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.
    chrome_options.add_argument('--window-size= x, y') #실행되는 브라우저 크기를 지정할 수 있습니다.
    chrome_options.add_argument('--start-maximized') #브라우저가 최대화된 상태로 실행됩니다.
    #chrome_options.add_argument('--start-fullscreen') #브라우저가 풀스크린 모드(F11)로 실행됩니다.
    #chrome_options.add_argument('--blink-settings=imagesEnabled=false') #브라우저에서 이미지 로딩을 하지 않습니다.
    chrome_options.add_argument('--mute-audio') #브라우저에 음소거 옵션을 적용합니다.
    
    userPath
    profilePath = userPath + '/AppData/Local/Google/Chrome/User Data'
    #if Path('C:/Users/nks/AppData/Local/Google/Chrome/User Data').exists():
    #        profilePath = "C:/Users/nks/AppData/Local/Google/Chrome/User Data"
    #else:
    #        profilePath = "C:/Users/mypc/AppData/Local/Google/Chrome/User Data"
    #        
    chrome_options.add_argument('--user-data-dir='+profilePath) #사용자 환경설정 경로
    #chrome_options.add_argument('--profile-directory=profile 2') #사용자 환경설정 경로
    #chrome_options.add_argument('--profile-directory=Default') #사용자 환경설정 경로
    chrome_options.add_argument('--profile-directory='+profile)
    #chrome_options.add_argument('incognito') #시크릿 모드의 브라우저가 실행됩니다.
    
    return chrome_options

def getChromeDriver(workingUser):
    
    driver =''
    
    if getattr(sys, 'frozen', False):
        chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
        driver = webdriver.Chrome(chromedriver_path, options=getChromeOptions(userList.get(workingUser).get('profile')))
    else:
        driver = webdriver.Chrome(r'C:\Dev\git\python-study\selenium\files\chromedriver.exe', options=getChromeOptions(userList.get(workingUser).get('profile'))) 
    #driver = webdriver.Chrome(r'C:\Dev\git\python-study\selenium\files\chromedriver.exe', options=getChromeOptions(profile))
    #driver = webdriver.Remote('http://localhost:4444/wd/hub', chrome_options.to_capabilities())
    return driver
    
#url = 'https://mr-seo.co.kr/auth/login'
#driver.get(url)

# 로그인 처리
def doLogin(driver, workingUser):
    url = 'https://mr-seo.co.kr/auth/login'
    driver.get(url)
    time.sleep(3)
    
    isLogin = LoginCheck(driver)
    
    # 로그인되어 있을 경우 로그아웃 처리
    if(isLogin):
        driver.find_element('xpath','/html/body/div[1]/div[1]/ul/li/div/ul/li[3]/a/img').click()
        
    time.sleep(3)
    
    userId = driver.find_element('id', 'am_id')
    userId.send_keys(userList.get(workingUser).get('userId'))

    userPwd = driver.find_element('id', 'am_pwd')
    userPwd.send_keys(userList.get(workingUser).get('password'))

    loginButton = driver.find_element('xpath','//*[@id="loginBox"]/form/div/ul/li[3]/input')
    loginButton.click()
    time.sleep(3)
    
# 로그인되어 있는 상태인지 체크
def LoginCheck(driver):
    
    checkLotoutButton = False
    
    try:
        checkLotoutButton = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/ul/li/div/ul/li[3]/a/img')))
        
        if(checkLotoutButton):
            checkLotoutButton = True
                
        return checkLotoutButton
    finally:
        return checkLotoutButton
        