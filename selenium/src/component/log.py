import logging
import logging.handlers
import component.utility as utility
import sys
import io

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(u'%(asctime)s [%(levelname)8s] %(message)s')

utility.createFolder('C:/자동화폴더/logs')

def getLogger(name=None):
    
    #1 logger instance를 만듭니다. 
    logger = logging.getLogger(name)

    #2 logger의 level을 가장 낮은 수준인 DEBUG로 설정합니다.
    logger.setLevel(logging.DEBUG)
    
    #3 formatter 지정하여 log head를 구성해줍니다. 
    ## asctime - 시간정보
    ## levelname - logging level
    ## funcName - log가 기록된 함수
    ## lineno - log가 기록된 line
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - [%(funcName)s:%(lineno)d] - %(message)s")

    #4 handler instance 생성하여 console 및 파일로 저장할 수 있도록 합니다. 파일명은 txt도 됩니다.
    #console = logging.StreamHandler()
    #console = logging.FileHandler('C:/자동화폴더/logs')
    #
    #file_handler_debug = logging.FileHandler(filename="log_debug.log")
    #file_handler_info = logging.FileHandler(filename="log_info.log")
#
    ##5 handler 별로 다른 level 설정합니다. 설정한 level 이하 모두 출력,저장됩니다.
    #console.setLevel(logging.INFO)
    #file_handler_debug.setLevel(logging.DEBUG)
    #file_handler_info.setLevel(logging.INFO)
#
    ##6 handler 출력을 format 지정방식으로 합니다.
    #console.setFormatter(formatter)
    #file_handler_debug.setFormatter(formatter)
    #file_handler_info.setFormatter(formatter)
#
    ##7 logger에 handler 추가합니다.
    #logger.addHandler(console)
    #logger.addHandler(file_handler_debug)
    #logger.addHandler(file_handler_info)
	
    #8 설정된 log setting을 반환합니다.
    # FileHandler
    file_handler = logging.FileHandler('C:/자동화폴더/logs/out.log')
    file_handler.setFormatter(formatter)
    
    # RotatingFileHandler
    log_max_size = 10 * 1024 * 1024  ## 10MB
    log_file_count = 20
    rotatingFileHandler = logging.handlers.RotatingFileHandler(
    filename='C:/자동화폴더/logs/out.log',
    maxBytes=log_max_size,
    backupCount=log_file_count
    )
    
    rotatingFileHandler.setFormatter(formatter)

    # RotatingFileHandler
    timeFileHandler = logging.handlers.TimedRotatingFileHandler(
        filename='C:/자동화폴더/logs/out.log',
        when='midnight',
        interval=1,
        encoding='utf-8'
    )
    timeFileHandler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    return logger