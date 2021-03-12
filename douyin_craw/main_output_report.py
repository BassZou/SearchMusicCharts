# utf - 8

from mongo import MyMongodb


class Organizer(object):
    """
    1. 获取数据库数据
    2. 清洗给出相应的数据
    3. 输出结论、输出图标
    """
    db_data = None # 数据库中查询到的原始数据
    __keys = ['_id','author','link','rank','title','value','time','ranking'] # 需要查询的数据库字段
    count = None # 查询到的行数

    all_data_rege = [] # 热歌榜所有数据
    all_data_bs = [] # 飙升歌榜所有数据
    all_data_yc = [] # 原创歌榜所有数据

    stage_rege = None # 热歌榜更新阶段，例如：热歌榜更新3次，分别在2021-09-10、2021-09-15、2021-09-20
    stage_bs = None # 飙升榜更新阶段
    stage_yc = None # 原唱榜更新阶段

    list_rege = None # 在榜单各个阶段中重复出现的歌曲 ，例如：热歌榜中3个阶段都在出现 星辰大海、xxx，排名分别是xxx
    list_bs = None # 在榜单各个阶段中重复出现的歌曲 ，例如：热歌榜中3个阶段都在出现 星辰大海、xxx，排名分别是xxx
    list_yc = None # 在榜单各个阶段中重复出现的歌曲 ，例如：热歌榜中3个阶段都在出现 星辰大海、xxx，排名分别是xxx

    rising_analysis_rege = None # 榜单中排名有所【提升】的歌曲的【每次】环比、音频使用人数的趋势
    rising_analysis_bs = None # 榜单中排名有所【提升】的歌曲的【每次】环比、音频使用人数的趋势
    rising_analysis_yc = None # 榜单中排名有所【提升】的歌曲的【每次】环比、音频使用人数的趋势

    declining_analysis_rege = None # 榜单中排名有所【下降】的歌曲的【每次】环比、音频使用人数的趋势
    declining_analysis_bs = None # 榜单中排名有所【下降】的歌曲的【每次】环比、音频使用人数的趋势
    declining_analysis_yc = None # 榜单中排名有所【下降】的歌曲的【每次】环比、音频使用人数的趋势

    rising_analysis_rege_day = None # 榜单中排名有所【提升】的歌曲的【日】环比、音频使用人数的趋势
    rising_analysis_bs_day = None # 榜单中排名有所【提升】的歌曲的【日】环比、音频使用人数的趋势
    rising_analysis_yc_day = None # 榜单中排名有所【提升】的歌曲的【日】环比、音频使用人数的趋势

    declining_analysis_rege_day = None # 榜单中排名有所【下降】的歌曲的【日】环比、音频使用人数的趋势
    declining_analysis_bs_day = None # 榜单中排名有所【下降】的歌曲的【日】环比、音频使用人数的趋势
    declining_analysis_yc_day = None # 榜单中排名有所【下降】的歌曲的【日】环比、音频使用人数的趋势



    def __init__(self, *args):
        Organizer.db_data = self.pullAllData()
        self.pullRankings()


    def pullAllData(self):
        """
        拉数据库中所有数据
        """
        # 想要查询数据库里的那些字段
        mydb = MyMongodb()
        data = mydb.queryall(self.__keys)
        self.count = data.count()
        count = self.count
        p(0)
        print('样本行数:',count)
        p(1)
        print('样本数据第1个：',data[0])
        print('样本数据倒数第3个：',data[count - 3])
        print('样本数据倒数第2个：',data[count - 2])
        print('样本数据倒数第1个：',data[count - 1])
        p(2)
        return list(data)


    def pullRankings(self):
        """
        将榜单数据分离
        """
        for rankings in Organizer.db_data:
            if rankings.get('ranking') and '热歌榜' in rankings['ranking']:
                Organizer.all_data_rege.append(rankings)
            elif rankings.get('ranking') and '飙升榜' in rankings.get('ranking'):
                Organizer.all_data_bs.append(rankings)
            elif rankings.get('ranking') and '原创榜' in rankings.get('ranking'):
                Organizer.all_data_yc.append(rankings)
        print('热歌榜总行数：',len(Organizer.all_data_rege))
        print('飙升榜总行数：',len(Organizer.all_data_bs))
        print('原创榜总行数：',len(Organizer.all_data_yc))


    def getStage(self):
        """榜单更新阶段
        """
        reges = 0 # 热歌榜集合
        bss = 0 # 飙升榜集合
        ycs = 0 # 原创榜集合

        print('---',self.all_data_rege[0])
        print('---',self.all_data_rege[1])
        print('---',self.all_data_rege[2])
        p(1)
        


   



def p(args=1,value=''):
        """输出"""
        if args == 1:
            print('-------')
        if args == 0:
            print('\n \n \n-------')
        if args == 2:
            print('-------','\n \n \n-------') 

if __name__ == '__main__':
    organ = Organizer()
    organ.getStage()

    
        
    