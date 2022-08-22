import sys
import os.path  
import pandas as pd
import numpy as np

excelFile = 'C:/자동화폴더/상품목록.xlsx'
excelSheetName = 'list'

# 엑셀파일 존재여부 체크
def checkFileExist():
    try:
        if os.path.isfile(excelFile):
            print('상풍목록 엑셀 파일이 잘 있네~~')
            print('이제 수집을 시작해볼게용~~♡')
        else:
            raise
    except:
        print('==================================================================================')
        print('Oops!!!')
        print('쟈기~상품목록 파일이 없네~~?')
        print('자자..아래를 참고해서 경로에 파일을 넣어줘~')
        print('C:/자동화폴더/상품목록.xlsx')
        print('==================================================================================')
        sys.exit(1)


# 수행할 데이터의 전체 건수 체크, 0이면 종료
def checkDataRow(rowData):
    
    productCnt = len(rowData.index)
    
    try:
        if productCnt < 1:
            raise
        else:
            print('==================================================================================')
            print('엑셀을 잘 읽은 것 같앙~')
            print('이제 시작할꺼야~')
            print('==================================================================================')
    except:
        print('==================================================================================')
        print('Oops!!!')
        print('쟈갸 엑셀에 파일에 수집할 목록이 없쩌!!!')
        print('수집 상품을 등록해주세용~~♡')
        print('==================================================================================')
        sys.exit(1)
    

# 엑셀에서 원천 수집데이터 로딩
def getCollectorExcel():
    
    beforeDf = pd.read_excel(excelFile, engine = "openpyxl", usecols='A,B,I,J,K,L', header=0, sheet_name=excelSheetName)

    checkDataRow(beforeDf) # 데이터 건수 체크
    
    return beforeDf

# 원천 엑셀 데이터로부터 신규 DataFrame 생성 및 데이터 유효성 체크
def getCollectorFrameData(rowData):
    
    rowData.rename(columns = {'계정' : 'account', '검색 키워드' : 'searchKeyword', '알리익스프레스' : 'ali', '알리페이지' : 'ali_page','타오바오' : 'tao','타오페이지' : 'tao_page'}, inplace = True)
       
    df = pd.DataFrame(columns=['account','searchKeyword','ali', 'ali_page','tao','tao_page'])
    for product in range(len(rowData.index)):
        
        # 계정이 없는 경우 예외 발생
        try:
            if str(type(rowData.iloc[product, 0])) != "<class 'str'>":
                raise
        except:
            print('==================================================================================')
            print('Oops!!!')
            print('계정이 없는게 있어서 종료할게~~~')
            print('다시 확인하고 프로그램 돌려줭~')
            print('==================================================================================')
            sys.exit(1)
            
        # 알리익스플레스 또는 타오바오 둘 다 없는 경우 예외 발생!!!
        try:
            if str(type(rowData.iloc[product, 2])) == "<class 'float'>" and str(type(rowData.iloc[product, 4])) == "<class 'float'>":
                raise
        except:
            print('==================================================================================')
            print('Oops!!!')
            print('알리하고 타오바오 주소 둘 다 없는게 있어서 종료할게~~~')
            print('다시 확인하고 프로그램 돌려줭~')
            print('==================================================================================')
            sys.exit(1)

        # 알리익스플레스가 값이 있는데 알리 페이지가 없는 경우
        if(str(type(rowData.iloc[product, 2])) != "<class 'float'>"):
            try:
                if(np.isnan(rowData.iloc[product, 3])):
                    raise
            except:
                print('==================================================================================')
                print('Oops!!!')
                print('알리 페이지가 숫자가 아니거나 내용이 없는게 있어서 종료할게~~~')
                print('다시 확인하고 프로그램 돌려줭~')
                print('==================================================================================')
                sys.exit(1)
    

        # 타오바오가 값이 있는데 타오 페이지가 없는 경우
        if(str(type(rowData.iloc[product, 4])) != "<class 'float'>" and str(type(rowData.iloc[product, 4])) != "<class 'numpy.float64'>"):
            try:
                if(np.isnan(rowData.iloc[product, 5])):
                    raise
            except:
                print('==================================================================================')
                print('Oops!!!')
                print('타오 페이지가 숫자가 아니거나 내용이 없는게 있어서 종료할게~~~')
                print('다시 확인하고 프로그램 돌려줭~')
                print('==================================================================================')
                sys.exit(1)               

        # 미서폴더에 내용이 없는 경우
        if str(type(rowData.iloc[product, 1])) == "<class 'float'>":
            try: 
                if(np.isnan(rowData.iloc[product, 1])):
                    raise
            except:
                print('==================================================================================')
                print('Oops!!!')
                print('미서 폴더에 값이 없는게 있네~~~~')
                print('다시 확인하고 프로그램 돌려줭~')
                print('==================================================================================')
                sys.exit(1)
  

        ali = ''
        tao = ''
        ali_page = ''
        tao_page = ''
        account = rowData.iloc[product, 0]
        
        if(str(type(rowData.iloc[product, 2])) != "<class 'float'>"):
            ali = str(rowData.iloc[product, 2])
            ali_page = str(int(rowData.iloc[product, 3]))
        else:
            ali = ''

       
        if(str(type(rowData.iloc[product, 4])) != "<class 'float'>" and str(type(rowData.iloc[product, 4])) != "<class 'numpy.float64'>"):
            tao = str(rowData.iloc[product, 4])
            tao_page = str(int(rowData.iloc[product, 5]))
        else:
            tao = ''

        searchKeyword = ''
    
        if str(type(rowData.iloc[product, 1])) == "<class 'float'>":
            searchKeyword = str(int(rowData.iloc[product, 1]))
        else:
            searchKeyword = rowData.iloc[product, 1]

        df.loc[product] =[account, searchKeyword, ali, ali_page, tao, tao_page]
    
    df_sort_values = df.sort_values(by='account',ascending=True)
    
    return df_sort_values

        