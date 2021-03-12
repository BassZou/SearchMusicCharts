
from mUtils.datetimeUtil import TimeUtil
from mUtils.editExcel import WriteExcel
from craw.wangyimusic import wyCraw,WyMusicDetails
from craw.tmeMusic import qqCraw
from craw.tmeMusic import kugouCraw
from craw.tmeMusic import kuwoCraw
import config
from mUtils.bot import FeiShuBot
import threading #Timer（定时器）是Thread的派生类
from db.mongodb import MyMongodb


"""
程序入口
1. 爬取数据、清洗
2. 导出excel
"""
def start():
    timer = threading.Timer(5800, start) 

    all_sheet, all_link, list_song = carw_wangyi_music()
    carw_qq_music()
    carw_kugou_music()
    carw_kuwo_music()
    # 网易歌曲详情
    # carw_wangyi_music_details(list_song,all_sheet,all_link)
    timer.start()


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


def carw_wangyi_music_details(list_song,all_sheet,all_link):
    """
    爬取网易歌曲详情页数据
    """
    # ----------------------测试只做一个排行榜
    # del list_song[1:]
    # del all_sheet[1:]
    # print('list_song',len(list_song))
    # print('all_sheet',len(all_sheet))
    # ----------------------

    songslist,songs,title = [],[],['排名','歌曲名称','演唱者','主页', '下载地址','评论数',
                        '专辑名','专辑url','歌词','发行公司','发行时间',
                        '专辑转发数','专辑评论数','专辑歌曲数','专辑介绍']
    songs.append(title)

    for index1,item in enumerate(list_song):
        #----------del
        sss = []
        #----------end
        for index,song in enumerate(item):
            if index == 0: # 头部
                continue
            # if index == 20: # 只爬取index首歌曲
            #     break
            rank = song[0]
            name = song[1]
            who = song[2]
            link = song[3]
            dwonload_url = song[4]
            print('详情页数据获取中---',name ,link)
            obj = [str(name),str(link)]

            wy = WyMusicDetails(obj)
            wy.start_handless()
            # wy.start_ui()
            song_details = wy.getAllData()
            wy.quit()
            print('详情页数据获取中----歌手',song_details[0])
            print('详情页数据获取中----歌名',song_details[1])
            print('详情页数据获取中----评论数',song_details[2])
            print('详情页数据获取中----专辑名',song_details[3])
            print('详情页数据获取中----专辑url',song_details[4])
            print('详情页数据获取中----歌词',song_details[5])
            print('详情页数据获取中----发行公司',song_details[6])
            print('详情页数据获取中----发行时间',song_details[7])
            print('详情页数据获取中----专辑转发数',song_details[8])
            print('详情页数据获取中----专辑评论数',song_details[9])
            print('详情页数据获取中----专辑歌曲数',song_details[10])
            print('详情页数据获取中----专辑介绍',song_details[11])
            s = [rank,name,who,link, dwonload_url,
                song_details[2],
                song_details[3],
                song_details[4],
                song_details[5],
                song_details[6],
                song_details[7],
                song_details[8],
                song_details[9],
                song_details[10],
                song_details[11],
                ]
            songs.append(s)
            # #----------del----下方测试数据
            if index == 99: # 20首歌曲时导出一次
                sss.append(songs)
                toExcel(data = sss, all_sheet=all_sheet, filename='网易排行榜(详细)99'+name)
            # #----------end
        songslist.append(songs)
        #----------del----下方测试数据
        toExcel(data = songslist, all_sheet=all_sheet, filename='网易排行榜(详细)'+all_sheet[index1])
        # ---------end

    toExcel(data = songslist, all_sheet=all_sheet, filename='网易排行榜(详细)')
    # 查看是否有命中的歌曲
    # objective_songs(list_song, all_sheet, all_link)


def carw_wangyi_music():
    """
    爬取网易歌曲排行榜
    """
    wy = wyCraw()
    wy.start_handless()
    # wy.start_ui()
    all_sheet, all_link, list_song = wy.getAllData()
    wy.quit()
    toExcel(data = list_song, all_sheet=all_sheet, filename='网易排行榜')
    # 查看是否有命中的歌曲
    objective_songs(list_song, all_sheet, all_link)
    return all_sheet, all_link, list_song


def carw_kuwo_music():
    """
    爬取酷我排行榜
    """
    kw = kuwoCraw()
    kw.start_handless()
    # kw.start_ui()
    all_sheet, all_link, list_song = kw.getAllData()
    kw.quit()
    toExcel(data = list_song, all_sheet=all_sheet, filename='酷我排行榜')
    # 查看是否有命中的歌曲
    objective_songs(list_song, all_sheet, all_link)


def carw_kugou_music():
    """
    爬取酷狗排行榜
    """
    kugou = kugouCraw()
    kugou.start_handless()
    # kugou.start_ui()
    all_sheet, all_link, list_song = kugou.getAllData()
    kugou.quit()
    toExcel(data = list_song, all_sheet=all_sheet, filename='酷狗排行榜')
    # 查看是否有命中的歌曲
    objective_songs(list_song, all_sheet, all_link)


def carw_qq_music():
    """
    爬取QQ音乐排行榜
    """
    qq = qqCraw()
    qq.start_handless()
    # qq.start_ui()
    all_sheet, all_link, list_song = qq.getAllData()
    qq.quit()
    toExcel(data = list_song, all_sheet=all_sheet, filename='qq音乐排行榜')
    # 查看是否有命中的歌曲
    objective_songs(list_song, all_sheet, all_link)


def objective_songs(data, all_sheet, all_link):
    """
    查看是否有命中的歌曲
    监控平台歌曲集合 data
    榜单名字 all_sheet
    榜单链接 all_link
    """
    for song in config.SONGS:
        # 目标歌曲名称、演唱者
        song_name = song[0]
        song_who = song[1]
        for index,rank in enumerate(data):
            for r in rank:
                r_song_name = r[1]
                r_song_who = r[2]
                if r_song_name == song_name:
                    print('all_sheet---排行榜数量------',len(all_sheet))
                    print('all_link---排行榜链接---',len(all_link))
                    print('data---排行榜内容---',len(data))
                    print('发现推红歌曲', all_sheet[index], all_link[index], r)
                    FeiShuBot().send_msg('发现推红歌曲', '【排行榜名称】\n'+all_sheet[index]+ '\n 【排行榜链接】\n'+ all_link[index] + '\n 【排名】'+ str(r[0])+ '\n 【歌名】'+ str(r[1])+ '\n 【歌手】'+ str(r[2])+ '\n 【歌曲主页】\n'+ str(r[3]))

                elif r_song_who == song_who:
                    print('发现推红歌曲中的作者', all_sheet[index], all_link[index], r)
                else:
                    continue


if __name__ == "__main__":
    start()