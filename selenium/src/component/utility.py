import time
import os
import component.log as log

logger = log.getLogger("common")

def check_alert(driver):
    from selenium.common.exceptions import NoAlertPresentException
    try:
        alertObject = driver.switch_to.alert
        return (True, alertObject.text)
    except NoAlertPresentException:
        return (False, '')
    
def now():
    now = time.localtime()
    returnTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    return '('+returnTime+')'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('경로 생성에 실패했습니다.')
        
def getUserHome():
    return os.path.expanduser('~')

def errorMessageHandler(exception):
    
    status = 'fail'
    logger.info(exception)
    if 'user data directory is already in use' in exception:
        return status, '동작 중인 Chrome 브라우저가 존재합니다. \n모든 Chrome 브라우저를 종료 후 재실행해주세요. \n지속해서 해당 문제가 발생할 경우 Chrome 백그라운드 동작 여부를 확인해주세요.'
    
    elif 'no such element' in exception:
        return status, '식별할 수 없는 화면 요소가 있습니다. \n지속해서 오류가 발생할 경우 문의하기를 이용해주세요.'
    
    elif 'chrome not reachable' in exception:
        return status, '동작 중 Chrome 브라우저가 외부 요인에 의해 종료되었습니다. \n작업을 재수행해주세요.'
    
    elif 'excel.product.not.exist' in exception:
        return status, '엑셀 파일에 작업 대상이 없습니다. 상품을 등록해주세요.'
    
    else:
        return status, '오류가 발생했습니다. \n문의하기를 이용해주세요.'
    
    