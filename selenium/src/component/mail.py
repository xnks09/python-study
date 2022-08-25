import smtplib
from email.mime.text import MIMEText
 
def sendMail(type, subject, text): 
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()      # say Hello
    smtp.starttls()  # TLS 사용시 필요
    smtp.login('9.miho.noreply@gmail.com', 'uqdtgvtccddqjrpy')
    
    subjectType = '[수집]['+type+']'
    msg = MIMEText(text)
    
    msg['Subject'] = subjectType+subject
    msg['To'] = '1113ruddl@daum.net'
    smtp.sendmail('9.miho.noreply@gmail.com', '1113ruddl@daum.net', msg.as_string())
        
    smtp.quit()
    
    
    
    