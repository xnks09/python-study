def check_alert(driver):
    from selenium.common.exceptions import NoAlertPresentException
    try:
        alertObject = driver.switch_to.alert
        return (True, alertObject.text)
    except NoAlertPresentException:
        return (False, '')