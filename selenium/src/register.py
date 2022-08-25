from genericpath import isfile
import sys
import io
import sys
import os.path       
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math
import numpy as np
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import component.excelFile as excelFile
import component.utility as utility
import component.kakao as kakao
import component.mail as mail
import component.chromeDriver as chromeDriver
import pandas as pd
import openpyxl

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

####################################################################################################################


def init():
    excelFile.checkFileExist()
    rowData = excelFile.getRegisterExcel()
    newData = excelFile.getRegisterFrameData(rowData)
    print('[데이터 등록 시작 - ', len(newData.index),'건]')
    print("==============================================================================")
    print(newData)
    print("==============================================================================")
    doRegist(newData)
    
def doRegist(rowData):

    mail.sendMail('','============================================','내용없음')
    mail.sendMail('','[데이터 등록 시작 - ' +str(len(rowData.index))+'건]','내용없음')
    
    # 초기 시작 계정
    workingUser = rowData.loc[0,'account']
   
    # 전체 수집 건수
    totalCnt = len(rowData.index)
    
    driver = chromeDriver.getChromeDriver(workingUser)
    chromeDriver.doLogin(driver, workingUser)
    time.sleep(3)
    
    for productList in range(len(rowData.index)):
        
        driver.get('https://mr-seo.co.kr/mr_product/list')
        time.sleep(4)
        targetKeyword = rowData.loc[productList, 'searchKeyword']
        count_logLabel = '['+ str(productList+1)+'/'+str(totalCnt) +'] ' 
        targetKeyword_logLabel = '['+ targetKeyword +']' 
        
        print('=============================================================================')
        print(count_logLabel,targetKeyword_logLabel,'에 대한 등록을 시작합니다.',utility.now())

        if rowData.loc[productList, 'account'] != workingUser:
            workingUser = rowData.loc[productList, 'account']
            print(count_logLabel, workingUser,'계정으로 재로그인을 시도합니다.')
            chromeDriver.doLogin(driver, workingUser)
            time.sleep(3)
                   
        # 실제 등록 리스트
        pageList = {}
        siteIndex = 0

        # 폴더입력
        folderList = Select(driver.find_element('id', 'product_folder'))
        folderList.select_by_value(rowData.loc[productList, 'searchKeyword'])
        
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
        weightList = Select(driver.find_element('id', 're_wgt'))
        weightList.select_by_value(str(rowData.loc[productList, 'weight']))
        driver.find_element('xpath','//*[@id="listContainer"]/ul/li[5]/button').click() #[선택무게변경] 버튼 클릭

        # 무게 설정 변경에 대한 alert처리
        wait = WebDriverWait(driver, 120)
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
        time.sleep(3)
        driver.find_element('xpath','//*[@id="commerce_coupang"]/td/div[1]/button').click() # 쿠팡 카테고리 매핑 버튼 클릭
        time.sleep(1)
        driver.find_element('name', 'categoryMappingTitle').send_keys(rowData.loc[productList, 'coupangCategory']) # 카테고리 문자 복사
        driver.find_element('xpath','//*[@id="categoryMappingModal"]/div/div[2]/div[1]/button').click() # 검색 버튼 클릭
        time.sleep(1)
        driver.find_element('xpath','//*[@id="setRecommendCoupangCategoryButton"]').click() # 카테고리 변경 클릭
        time.sleep(1)
        driver.find_element('xpath','//*[@id="categoryMappingModal"]/div/div[3]/button').click() # 적용 버튼 클릭
        time.sleep(1)
        driver.find_element('xpath','//*[@id="setCategoryButton"]').click() # 부모 페이지의 적용 버튼 클릭

        # 일괄 카테고리 변경에 대한 alert처리
        wait = WebDriverWait(driver, 120)
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
        time.sleep(3)
        driver.find_element('xpath','//*[@id="titleModal"]/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[1]/input[1]').clear()
        time.sleep(1)
        driver.find_element('xpath','//*[@id="titleModal"]/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[1]/input[1]').send_keys(100) # 글자수를 100으로 변경
        #driver.find_element('name', 'maxKeyword').send_keys(100) # 글자수를 100으로 변경
        driver.find_element('name', 'brandName').send_keys('구미호 협력사') # 브랜드명 입력
        originalTitle = rowData.loc[productList, 'title']
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
        time.sleep(3)

        # 일괄 제목 설정에 대한 alert처리
        wait = WebDriverWait(driver, 160)
        element = wait.until(EC.alert_is_present())
        alert_result = driver.switch_to.alert
        print(alert_result.text)
        alert_result.accept()
        print('[일괄 제목 설정이 완료되었습니다.........................................]')
        # 일괄 키워드 설정   
        print('[일괄 키워드 설정을 시작합니다..........................................]')
        # 수집 결과의 iframe 페이지로 이동
        time.sleep(2)
        driver.switch_to.frame('listFrame')
        driver.find_element('xpath','//*[@id="listContainer"]/ul/li[8]/button').click() # 일괄 키워드 편집 클릭
        time.sleep(5)
        driver.switch_to.parent_frame() # 상위 프레임으로 재이동
        time.sleep(10)
        driver.find_element('name', 'addText').send_keys(rowData.loc[productList, 'searchWord']) # 적용된 검색어 입력
        time.sleep(3)
        driver.find_element('name', 'addText').send_keys(Keys.ENTER) # 엔터키 입력
        time.sleep(1)
        driver.find_element('xpath','//*[@id="keywordMain"]/div/div[1]/button[3]').click() # 적용 버튼 클릭

        # 일괄 키워드 설정에 대한 alert처리
        wait = WebDriverWait(driver, 120)
        element = wait.until(EC.alert_is_present())
        alert_result = driver.switch_to.alert
        print(alert_result.text)
        alert_result.accept()
        print('[일괄 키워드 설정이 완료되었습니다.........................................]')

        # 최종 업로드 처리
        # 등록 결과의 iframe 페이지로 이동
        driver.switch_to.frame('listFrame')
        driver.find_element('xpath','//*[@id="listContainer"]/ul/li[11]/button').click() # 업로드 버튼 클릭
        time.sleep(1)
        driver.find_element('xpath','//*[@id="listContainer"]/ul/li[11]/div/div[2]/ul/div/button').click() # 업로드 버튼 클릭(쇼핑몰 선택-쿠팡)

        # 일괄 연동 시스템에 대한 메시지 confirm창 처리
        wait = WebDriverWait(driver, 120)
        element = wait.until(EC.alert_is_present())
        alert_result = driver.switch_to.alert
        print(alert_result.text)
        alert_result.accept()


        print('[업로드를 시작합니다..........................................]')

        # 업로드에 대한 alert 처리
        wait = WebDriverWait(driver, 1800)
        element = wait.until(EC.alert_is_present())
        alert_result = driver.switch_to.alert
        print(alert_result.text)    

        if "A00683854" in alert_result.text:   
            print('[구매 옵션 5000개를 초과하여 업로드가 중지되었습니다.] 등록 중이던 폴더명 : ', rowData.loc[productList, 'searchKeyword'])
            sys.exit(1)
        else:
            returnMail = count_logLabel + targetKeyword_logLabel+ '에 대한 등록이 종료되었습니다.'+ utility.now()
            #kakao.f_send_talk(returnMail)
            mail.sendMail('성공', returnMail, alert_result.text)

        alert_result.accept()

        time.sleep(3)
    
    mail.sendMail('','[데이터 등록 종료 - ' +str(len(rowData.index))+'건]','내용없음')
    mail.sendMail('','============================================','내용없음')
    #kakao.f_send_talk('[데이터 수집 종료 - ' +str(len(rowData.index))+'건]')