# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class wyCraw:
    """
    爬取网易各个歌曲排行榜列表
    """
    # browser用于存放浏览器对象，读取数据时主要操作此对象
    __browser = None
    __chrome_options = None
    __url = 'https://music.163.com/'

    def __init__(self):
        pass

    def start_ui(self, parameter_list=None):
        """
        启动带ui的爬取方式
        """
        wyCraw.__browser = webdriver.Chrome()
        self.__browser.get(self.__url)


    def start_handless(self, parameter_list=None):
        """
        启动无ui的爬取形式，Headless方式启动
        mac和linux环境要求chrome版本是59+，而windows版本的chrome要求是60+，同时chromedriver要求2.30+版本
        """
        wyCraw.__chrome_options = webdriver.ChromeOptions()
        # 使用headless无界面浏览器模式
        self.__chrome_options.add_argument('--headless') # 增加无界面选项
        self.__chrome_options.add_argument('--disable-gpu') # 如果不加这个选项，有时定位会出现问题

        # 启动浏览器，获取网页源代码
        self.__browser = webdriver.Chrome(chrome_options=self.__chrome_options)
        self.__browser.get(self.__url)
        # print(f"browser text = {self.__browser.page_source}")


    def quit(self):
        self.__browser.quit()


    def implicitly_wait(self, time=10):
        """
        显性等待
        第三种办法就是显性等待，WebDriverWait，配合该类的until()和until_not()方法，就能够根据判断条件而进行灵活地等待了。它主要的意思就是：程序每隔xx秒看一眼，如果条件成立了，则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException。
        wait模块的WebDriverWait类是显性等待类，先看下它有哪些参数与方法：
        """
        self.__browser.implicitly_wait(time)


    def getAllData(self):
        """
        获取所有排行榜名称及链接
        list_name = [] # 排行榜所有名字
        list_link = [] # 排行榜所有名字对应的跳转链接
        list_song = [] # 所有排行榜中的数据集合，数据结构 [[排行榜类1],[排行榜类2],[排行榜类3]]
        排行榜类中的数据结构[[1行],[2行],[3行]]
        """
        list_name = [] # 排行榜所有名字
        list_link = [] # 排行榜所有名字对应的跳转链接
        list_song = [] # 所有排行榜中的数据集合，数据结构 [[排行榜类1],[排行榜类2],[排行榜类3]]

        # 首页点击排行榜
        p = "/html/body/div[1]/div[3]/div/ul/li[2]/a/em"
        # p = r'//*[@id="g_nav2"]/div/ul/li[2]/a/em'
        self.implicitly_wait()
        self.__browser.find_element_by_xpath(p).click()
        print('当前所在网址：', self.__browser.current_url)
        
        # 所有排行榜名称
        self.implicitly_wait(10)
        self.__browser.switch_to.frame('contentFrame')
        m = self.__browser.find_element_by_xpath('//*[@id="toplist"]/div[1]/div/ul[1]')
        __list = m.find_elements_by_class_name('name')
        for a in __list:
            # 把排行榜中的链接遍历到列表list_link中
            list_link.append(a.find_element_by_tag_name('a').get_attribute("href"))
            list_name.append(a.text)

        print('排行榜列表名称', [name.text for name in __list])
        print('排行榜列表link', [link for link in list_link])

        for link in list_link:
            self.__browser.get(link) # 打开排行榜
            self.__browser.switch_to.frame('contentFrame') #进入frame
            p = r'//*[@id="toplist"]/div[2]/div/div[1]/div/div[2]/div/div[1]/h2'
            print("当前所在的榜单名称：", self.__browser.find_element_by_xpath(p).text)
            # self.implicitly_wait()
            list_song.append(self.getSongs())
        
        return list_name, list_link ,list_song


    def getSongs(self):
        """
        获取排行榜中的歌曲列表
        [['排名','歌曲名称','演唱者','链接'],[],...]
        """
        songs = [['排名','歌曲名称','演唱者','主页', '下载地址']]

        b = self.__browser.find_element_by_tag_name('tbody')
        items = b.find_elements_by_tag_name('tr')
        for i in items:
            song = []
            rank = i.find_element_by_class_name('num').text
            name = i.find_element_by_tag_name('b').get_attribute('title').encode("gbk", 'ignore').decode("gbk", 'ignore')
            who = i.find_elements_by_tag_name('td')[3].find_element_by_tag_name('span').get_attribute('title')
            link = i.find_elements_by_tag_name('td')[1].find_element_by_tag_name('a').get_attribute('href')
            song.append(rank)
            song.append(name)
            song.append(who)
            song.append(link)
            url_front="http://music.163.com/song/media/outer/url?id="
            url_real=url_front+str(link.split("=")[1])+".mp3"
            song.append(url_real)
            print('--->',rank,name,who,link,url_real)
            songs.append(song)
        return songs


class WyMusicDetails(object):
    """
    根据歌曲主页爬取与当前歌曲相关的数据
    歌名、歌手、歌曲评论数、发行时间、发行公司、歌词、所属专辑、专辑转发数、专辑评论数、专辑介绍、专辑歌数、歌曲专辑url
    """
    __song_name = None
    __song_url = None
    __browser = None
    __chrome_options = None

    def __init__(self, object):
        WyMusicDetails.__song_name = object[0]
        WyMusicDetails.__song_url = object[1]


    def start_ui(self, parameter_list=None):
        """
        启动带ui的爬取方式
        """
        WyMusicDetails.__browser = webdriver.Chrome()
        self.__browser.get(self.__song_url)


    def start_handless(self, parameter_list=None):
        """
        启动无ui的爬取形式，Headless方式启动
        mac和linux环境要求chrome版本是59+，而windows版本的chrome要求是60+，同时chromedriver要求2.30+版本
        """
        WyMusicDetails.__chrome_options = webdriver.ChromeOptions()
        # 使用headless无界面浏览器模式
        self.__chrome_options.add_argument('--headless') # 增加无界面选项
        self.__chrome_options.add_argument('--disable-gpu') # 如果不加这个选项，有时定位会出现问题

        # 启动浏览器，获取网页源代码
        try:
            self.__browser = webdriver.Chrome(chrome_options=self.__chrome_options)
            self.implicitly_wait(10)
            self.__browser.get(self.__song_url)
        except:
            print('start_handless 报错')
        
        # print(f"browser text = {self.__browser.page_source}")


    def quit(self):
        self.__browser.quit()


    def implicitly_wait(self, time=10):
        self.__browser.implicitly_wait(time)


    def getAllData(self):
        """
        歌名、歌手、歌曲评论数、发行时间、发行公司、歌词、
        所属专辑、专辑转发数、专辑评论数、专辑介绍、专辑歌数、歌曲专辑url
        """
        self.implicitly_wait(10)
        self.__browser.switch_to.frame('contentFrame')
        
        try:
            __song_name = self.__browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div/em').text
        except:
            __song_name = '无'
            print(__song_name,'无歌名')

        try:
            __singer = self.__browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/p[1]/span').text
        except:
            __singer = '无'
            print(__song_name,'无歌名')

        try:
            __song_comments = self.__browser.find_element_by_xpath('//*[@id="cnt_comment_count"]').text
        except:
            __song_comments = '无'
            print(__song_comments,'无评论')

        try:
            pages = self.__browser.find_element_by_link_text("展开")
            self.__browser.execute_script("arguments[0].click();", pages)
            __lyrics = self.__browser.find_element_by_xpath('//*[@id="lyric-content"]').text
            __lyrics = __lyrics + self.__browser.find_element_by_id('flag_more').text
        except:
            __lyrics = '无'
            print(__lyrics,'无歌词')

        try:
            __album_name = self.__browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/p[2]/a').text
            __album_url = self.__browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/p[2]/a').get_attribute('href')
        except:
            __album_name = '无'
            __album_url = '无'
            print(__album_name,'无专辑')
            print(__album_url,'无专辑url')

        try:
            self.implicitly_wait(10)
            self.__browser.get(__album_url)

            self.implicitly_wait(10)
            self.__browser.switch_to.frame('contentFrame')
        except:
            print('getAllData 专辑页面 __album_url 报错',__album_url)


        try:
            __publish_time = str(self.__browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[2]').text)[5:]
        except:
            __publish_time = '无'
            print(__publish_time,'没有发行时间')

        try:
            __publisher = str(self.__browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[3]').text)[5:]
        except:
            __publisher = '无'
            print(__publisher,'没有发行公司')

        try:
            __album_reposts = str(self.__browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[1]/div[2]/div/div[2]/a[4]/i').text)
        except:
            __album_reposts = '无'
            print(__album_reposts,'专辑转发为空')
        
        try:
            __album_comments = str(self.__browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[1]/div[2]/div/div[2]/a[6]/i/span').text)
        except:
            __album_comments = '无'
            print(__album_comments,'专辑评论为空')

        try:
            __album_introduction = self.__browser.find_element_by_id('album-desc-dot').text
        except:
            __album_introduction = '无'
            print(__album_introduction,'专辑介绍为空')

        try:
            __album_num = str(self.__browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[3]/div[1]/span').text)# 专辑歌数 
        except:
            __album_num = '无'
            print(__album_num,'专辑歌曲数量')

        print('歌手',__singer)
        print('歌名',__song_name)
        print('评论数',__song_comments)
        print('专辑名',__album_name)
        print('专辑url',__album_url)
        print('歌词',__lyrics)
        print('发行公司',__publisher)
        print('发行时间',__publish_time)
        print('专辑转发数',__album_reposts)
        print('专辑评论数',__album_comments)
        print('专辑歌曲数',__album_num)
        print('专辑介绍',__album_introduction)

        song_details = [__singer,__song_name,__song_comments,__album_name,__album_url,__lyrics, \
                            __publisher,__publish_time,__album_reposts,__album_comments,__album_num,__album_introduction]
        return song_details


# https://www.jianshu.com/p/1531e12f8852
if __name__ == "__main__":
    # wy = wyCraw()
    # wy.start_handless()
    # # wy.start_ui()
    # wy.getAllData()
    # wy.quit()

    song = ['为什么','https://music.163.com/#/song?id=1811102198']
    wy = WyMusicDetails(song)
    wy.start_handless()
    # wy.start_ui()
    wy.getAllData()
    wy.quit()
    pass