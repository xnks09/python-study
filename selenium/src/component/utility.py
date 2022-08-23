import time

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
