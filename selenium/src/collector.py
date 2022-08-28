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
import component.excelFile as excelFile
import component.chromeDriver as chromeDriver
import component.utility as utility
import component.kakao as kakao
import component.mail as mail
import pandas as pd
import openpyxl
import component.log as log


logger = log.getLogger("common")
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#logger = log.getLogger("common")

#driver = webdriver.Chrome(r'C:\Dev\git\python-study\selenium\files\chromedriver.exe', options=getChromeOptions('Default'))
##driver = webdriver.Remote('http://localhost:4444/wd/hub', chrome_options.to_capabilities())
#url = 'https://mr-seo.co.kr/auth/login'
#driver.get(url)

siteSelectList = {
    'ali': {'selectIndex': 1},
    'tao': {'selectIndex': 10}
}


def init():
    try:
        excelFile.checkFileExist()
        rowData = excelFile.getCollectorExcel()
        newData = excelFile.getCollectorFrameData(rowData)
        logger.info('[데이터 수집 시작 - ', len(newData.index),'건]')
        logger.info('==============================================================================')
        logger.info(newData)
        logger.info('==============================================================================')
        result = doCollector(newData)
    except Exception as e:
        logger.info(e)
        return utility.errorMessageHandler(str(e))
    return result
        
def doCollector(rowData):
    mail.sendMail('수집','============================================','내용없음')
    mail.sendMail('수집','[데이터 수집 시작 - ' +str(len(rowData.index))+'건]','내용없음')

    # 초기 시작 계정
    workingUser = rowData.loc[0,'account']
    
    # 전체 수집 건수
    totalCnt = len(rowData.index)

    driver = chromeDriver.getChromeDriver(workingUser)
    chromeDriver.doLogin(driver, workingUser)
    time.sleep(3)

    for productList in range(len(rowData.index)):

        targetKeyword = rowData.loc[productList, 'searchKeyword']
        count_logLabel = '['+ str(productList+1)+'/'+str(totalCnt) +'] ' 
        targetKeyword_logLabel = '['+ targetKeyword +']' 
        logger.info('==============================================================================')
        logger.info(count_logLabel + targetKeyword_logLabel, '에 대한 수집을 시작합니다.')
        
        if rowData.loc[productList, 'account'] != workingUser:
            workingUser = rowData.loc[productList, 'account']
            logger.info(count_logLabel + targetKeyword_logLabel, '계정으로 재로그인을 시도합니다.')
            chromeDriver.doLogin(driver, workingUser)
            time.sleep(3)
            driver.get('https://mr-seo.co.kr/mr_product/regist')
            logger.info(count_logLabel + targetKeyword_logLabel, '계정으로 로그인되었습니다.')

        # 실제 수집 리스트
        pageList = {}
        siteIndex = 0

        if(rowData.loc[productList, 'ali']) != '':
            pageList[siteIndex] = {'type': 'ali','url': rowData.loc[productList, 'ali'], 'page': rowData.loc[productList, 'ali_page']}
            siteIndex += 1

        if(rowData.loc[productList, 'tao']) != '':
            pageList[siteIndex] = {'type': 'tao','url': rowData.loc[productList, 'tao'], 'page': rowData.loc[productList, 'tao_page']}

        for page in range(len(pageList.keys())):       
            time.sleep(2)
            driver.get('https://mr-seo.co.kr/mr_product/regist') 

            time.sleep(2)

        # 대량수집 버튼 클릭
        driver.find_element('xpath','//*[@id="searchFrm"]/table/tbody/tr[1]/td[1]/label[1]/input').click()
        time.sleep(2)

        # 폴더 입력
        driver.find_element('id', 'folder').send_keys(rowData.loc[productList, 'searchKeyword'])

        time.sleep(2)

        target = pageList[page].get('type')

        if(target == 'ali'):
            logger.info(count_logLabel + '알리익스플레스에 대한 수집을 수행합니다.')

        if(target == 'tao'):
            logger.info(count_logLabel + '타오바오에 대한 수집을 수행합니다.')

        siteList = Select(driver.find_element('id', 'site_code'))
        siteList.select_by_index(int(siteSelectList.get(pageList[page].get('type')).get('selectIndex')))

        # 스크래핑 URL 입력
        driver.find_element('id', 'url').send_keys(str(pageList[page].get('url')))
        time.sleep(1)

        #불러오기 버튼 클릭
        driver.find_element('xpath','//*[@id="getItemButton"]').click()

        time.sleep(20)

        isAlert, alertText = utility.check_alert(driver)

        if(isAlert):
            alert_result = driver.switch_to.alert
            logger.info('-------------------------------------------------------------')
            logger.info(count_logLabel + ' - 오류 : ' + targetKeyword+'에 대한 수집 중 오류가 발생했습니다.')
            logger.info(count_logLabel + ' - 오류내용 : ' + alertText)
            logger.info('-------------------------------------------------------------')
            mail.sendMail('수집', count_logLabel + targetKeyword_logLabel+' 수집 중 오류 발생', alertText)
            alert_result.accept()
            continue

        # 수집 결과의 iframe 페이지로 이동
        driver.switch_to.frame('listFrame')
        print(count_logLabel, '페이지 수를 입력합니다.')
        # 페이지 수 입력
        pageCnt = int(pageList[page].get('page'))

        pageSelect = Select(driver.find_element('id', 'e_page'))
        sitePageCnt = len(pageSelect.options)
        # 엑셀의 페이지수가 실제 페이수보다 클 경우 실제 페이지수를 기준으로 변경

        if sitePageCnt < pageCnt:
            pageSelect.select_by_index(sitePageCnt-1)
        else:
            pageSelect.select_by_index(pageCnt-1)
        print(count_logLabel, '페이지 입력을 완료했습니다.')
        time.sleep(5)

        driver.find_element('xpath','/html/body/div[1]/ul[1]/div/form/ul/div[2]/button').click()
        wait = WebDriverWait(driver, 10000)
                
        logger.info(count_logLabel + '수집 중입니다.')
                
        element = wait.until(EC.alert_is_present())
        logger.info(count_logLabel + '수집 완료 페이지를 찾고 있습니다.')
        alert_result = driver.switch_to.alert
        logger.info(count_logLabel + targetKeyword_logLabel + '에 대한 수집이 종료되었습니다.')
        returnMail = count_logLabel + targetKeyword_logLabel+ '에 대한 수집이 종료되었습니다.'+ utility.now()
        #kakao.f_send_talk(returnMail)
        mail.sendMail('성공', returnMail, alert_result.text)

        print(alert_result.text)
        alert_result.accept()
    logger.info('[데이터 수집 종료 - ' + str(len(rowData.index)) + '건]')
    logger.info('==============================================================================')
    mail.sendMail('수집','[데이터 수집 종료 - ' +str(len(rowData.index))+'건]','내용없음')
    mail.sendMail('수집','============================================','내용없음')
    return 'success', '데이터 수집이 종료되었습니다.'
    #kakao.f_send_talk('[데이터 수집 종료 - ' +str(len(rowData.index))+'건]')

