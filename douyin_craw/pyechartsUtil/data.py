# encoding utf-8
import xlrd

'''
【业务】数据读取

1 数据收集 - 2种方式（接口、Excel）
2 数据清洗
3 数据导出
'''


def getExcelToData1():
    '''
    用于动态矩形图 timeline_bar_reversal

    get 固定格式1
    row = '渠道1'，'渠道2'，'渠道3'，'渠道4'
    col = '2020-01-01'，'2020-01-02'，'2020-01-03'，'2020-01-04'
    col data = 0.23, 0.33, 0.44, 0.44
    
    return 
    {
        'date': ['2020-01-01'，'2020-01-02'，'2020-01-03'，'2020-01-04'],
        'kanaal': ['渠道1'，'渠道2'，'渠道3'，'渠道4'],
        'values': [[0.23, 0.33, 0.44, 0.44],[0.23, 0.33, 0.44, 0.44]]
    }
    '''
    res = {}
    filename = '渠道留存0612-0910.xlsx'
    wb = xlrd.open_workbook(filename)
    sheet1 = wb.sheet_by_index(0)
    nrows = sheet1.nrows
    # 日期组
    date = list(set(sheet1.col_values(0)[1:]))
    date.sort(reverse=False)

    # 渠道去重
    kanaal = list(set(sheet1.col_values(1)[1:]))

    # 原始数据所有行数据 rows_data
    i = 1
    rows_data = []
    while nrows-1 > i:
        rows_data.append(sheet1.row_values(i))
        i = i+1
        # print('--->\n',sheet1.row_values(i))
    
    '''
    将原始数据进行装载 - 日期
    '''
    res['date'] = date

    '''
    将原始数据进行装载 - 渠道
    '''
    res['kanaal'] = []
    for item in kanaal:
        res['kanaal'].append(item)

    '''
    将原始数据进行装载 - 值
    '''
    print(res['date'])

    res['values'] = []
    da = []
    for d in res['date']:
        for i in range(1,nrows):
            if d == sheet1.row_values(i)[0]: # 日期判断
                da.append(sheet1.row_values(i)[2])
                continue
            if da != []:
                res['values'].append(da)
                print('--values>',da)
                da = []
                continue
        
    return res
    



def getAPIToData():
    pass


# if __name__ == "__main__":
#     getExcelToData1()



