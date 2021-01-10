
from mUtils.datetimeUtil import TimeUtil
from mUtils.editExcel import WriteExcel
import config


"""
程序入口
1. 爬取数据、清洗
2. 导出excel
"""
def start():
    """
    docstring
    """
    data = [
        ['1','2'],
        ['3','4']
    ]

    toExcel(data)


def toExcel(data):
    """
    导出Excel
    """
    all_sheet = [
        '热歌榜'
    ]

    we = WriteExcel()
    for sheet_name in all_sheet:
        we.addSheet(sheet_name)
        we.set_style()
        we.put_value_in_area(data,sheet_name=sheet_name)
    f_path = config.FILE_PATH + TimeUtil().get_chinesedatetime() + '.xls'
    we.save_excel(str(f_path))



if __name__ == "__main__":
    start()