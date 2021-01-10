
from mUtils.datetimeUtil import TimeUtil
from mUtils.editExcel import WriteExcel
from craw.wangyimusic import wyCraw
import config


"""
程序入口
1. 爬取数据、清洗
2. 导出excel
"""
def start():
    carw_wangyi_music()


def toExcel(data, all_sheet=['sheet1'], filename=''):
    """
    导出Excel
    data与sheet 需要一一对应
    1个sheet里包含一个data
    """
    we = WriteExcel()
    for i in range(len(data)):
        we.addSheet(all_sheet[i])
        we.put_value_in_area(data[i],sheet_name=all_sheet[i])
    
    f_path = config.FILE_PATH + filename + TimeUtil().get_chinesedatetime() + '.xls'
    we.save_excel(str(f_path))


def carw_wangyi_music():
    """
    爬取网易歌曲排行榜
    """
    wy = wyCraw()
    wy.start_handless()
    # wy.start_ui()
    all_sheet, all_link, list_song = wy.getAllData()
    wy.quit()
    toExcel(data = list_song, all_sheet=all_sheet, filename='网易')


if __name__ == "__main__":
    start()