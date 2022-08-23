import smtplib
from email.mime.text import MIMEText
 
def sendMail(type, text): 
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()      # say Hello
    smtp.starttls()  # TLS 사용시 필요
    smtp.login('9.miho.noreply@gmail.com', 'uqdtgvtccddqjrpy')
    
    subjectType = '['+type+']'
    msg = MIMEText(text)
    
    msg['Subject'] = subjectType+' 자동화 프로그램'
    msg['To'] = '1113ruddl@daum.net'
    smtp.sendmail('9.miho.noreply@gmail.com', '1113ruddl@daum.net', msg.as_string())
    
    smtp.quit()
    
    
    
    