import time
import datetime
import locale


class test:
   
    def __init__(self, curtime=None):
        self.curtime = curtime
 

    def get_timestemp(self):
        """时间戳"""
        return time.time()
 
    def get_date(self):
        """日期"""
        return time.strftime("%Y-%m-%d")
 
    def get_time(self):
        """时间"""
        return time.strftime("%H:%M:%S")
 
    def get_datetime(self):
        """日期和时间"""
        return time.strftime("%Y-%m-%d %H:%M:%S")
 
    def get_chinesedate(self):
        strTime = time.strftime("%Y年%m月%d日", time.localtime())
        return strTime
 
    def get_chinesetime(self):
        strTime = time.strftime("%H时%M分%S秒", time.localtime())
        return strTime
 
    def get_chinesedatetime(self):
        # locale.setlocale(locale.LC_CTYPE, 'chinese')  # 如果是win，需要加上这个，mac 可以不使用
        strTime = time.strftime("%Y年%m月%d日%H时%M分%S秒", time.localtime())
        return strTime
 
    def compute_date(self, day_interval):
        # 获取今天的日期
        today = datetime.date.today()
        # 在今天的日期上再减10天
        if isinstance(day_interval, int) and day_interval >= 0:
            return today + datetime.timedelta(days=day_interval)
        elif isinstance(day_interval, int) and day_interval < 0:
            return today - datetime.timedelta(days=abs(day_interval))
 
    def timestamp_to_date(self, timestamp):
        if not isinstance(timestamp, (int, float)):
            return None
        time_tuple = time.localtime(timestamp)
 
        return str(time_tuple[0]) + "年" + str(time_tuple[1]) + "月" + str(time_tuple[2]) + "日"
 
    def timestamp_to_time(self, timestamp):
        if not isinstance(timestamp, (int, float)):
            return None
        time_tuple = time.localtime(timestamp)
        return str(time_tuple[4]) + "时" + str(time_tuple[5]) + "分" + str(time_tuple[6]) + "秒"
 
    def timestamp_to_datetime(self, timestamp):
        return self.timestamp_to_date(timestamp) + self.timestamp_to_time(timestamp)
 
    def getEveryDay(self, start, end):
        date_list = []
        begin_date = datetime.datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m-%d")
            date_list.append(date_str)
            begin_date += datetime.timedelta(days=1)
        print('共生成了%s天' % str(len(date_list)))
        return date_list
 
    def getTime(self, t):
        """单个日期初始化时间戳"""
        dt = time.strptime(t, '%Y-%m-%d %H:%M:%S')
        time_stamp = int(time.mktime(dt))
        return time_stamp
  