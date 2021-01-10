# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class wyCraw:
    """
    爬取网易各个歌曲排行榜
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
        # list_name = __list
        for a in __list:
            # 把排行榜中的链接遍历到列表list_link中
            list_link.append(a.find_element_by_tag_name('a').get_attribute("href"))
            list_name.append(a.text)

        print('排行榜列表名称', [name.text for name in __list])
        print('排行榜列表link', [link for link in list_link])

        # 当前所在的排行榜名称
        p = r'//*[@id="toplist"]/div[2]/div/div[1]/div/div[2]/div/div[1]/h2'
        name = self.__browser.find_element_by_xpath(p).text
        print("当前所在的榜单名称：", name)


        for link in list_link:
            self.__browser.get(link)
            self.__browser.switch_to.frame('contentFrame')
            # self.implicitly_wait()
            list_song.append(self.getSongs())
        
        return list_name, list_link ,list_song


    def getSongs(self):
        """
        获取排行榜中的歌曲列表
        [['排名','歌曲名称','演唱者','链接'],[],...]
        """
        songs = [['排名','歌曲名称','演唱者','链接']]

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
            print('--->',rank,name,who,song)
            songs.append(song)
        return songs


# https://www.jianshu.com/p/1531e12f8852
if __name__ == "__main__":
    wy = wyCraw()
    wy.start_handless()
    # wy.start_ui()
    wy.getAllData()
    # wy.quit()