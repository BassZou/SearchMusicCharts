# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time



class qqCraw:
    """
    爬取qq音乐各个歌曲排行榜
    """
    # browser用于存放浏览器对象，读取数据时主要操作此对象
    __browser = None
    __chrome_options = None
    __url = 'https://y.qq.com/n/yqq/toplist/4.html'

    def __init__(self):
        pass

    def start_ui(self, parameter_list=None):
        """
        启动带ui的爬取方式
        """
        qqCraw.__browser = webdriver.Chrome()
        self.__browser.get(self.__url)


    def start_handless(self, parameter_list=None):
        """
        启动无ui的爬取形式，Headless方式启动
        mac和linux环境要求chrome版本是59+，而windows版本的chrome要求是60+，同时chromedriver要求2.30+版本
        """
        qqCraw.__chrome_options = webdriver.ChromeOptions()
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
        list_type = [] # 排行榜类型，例如：巅峰榜、地区榜、特色榜单
        list_name = [] # 排行榜所有名字
        list_link = [] # 排行榜所有名字对应的跳转链接
        list_song = [] # 所有排行榜中的数据集合，数据结构 [[排行榜类1],[排行榜类2],[排行榜类3]]
        排行榜类中的数据结构[[1行],[2行],[3行]]
        """
        list_type = [] # 排行榜类型，例如：
        list_name = [] # 排行榜所有名字
        list_link = [] # 排行榜所有名字对应的跳转链接
        list_song = [] # 所有排行榜中的数据集合，数据结构 [[排行榜类1],[排行榜类2],[排行榜类3]]

        # 所有排行榜名称
        # self.implicitly_wait(10)

        m = self.__browser.find_element_by_xpath('/html/body/div[2]/div[1]')
        m_type = m.find_elements_by_tag_name('dl') # 各个大类 例如：巅峰榜、地区榜...
        m_type_2 = m.find_elements_by_tag_name('dd') # 子榜单对象,可以拿到名称
        m_type_2_obj = m.find_elements_by_tag_name('a') # 子榜单的对象，可以拿到url

        for t in m_type:
            list_type.append(t.find_element_by_tag_name('dt').text)
            print('QQ音乐榜单分类', t.find_element_by_tag_name('dt').text)

        for t in m_type_2:
            list_name.append(t.text)
            # m_type_2_link_url.append(t.get_attribute('href'))
            print('QQ音乐榜单分类-子榜单', t.text)
            # print('QQ音乐榜单分类-子榜单url', t.get_attribute('href'))

        for t in m_type_2_obj:
            url = t.get_attribute('href')
            list_link.append(url)
            print('QQ音乐榜单分类-子榜单url', url)
        
        for i,url in enumerate(list_link):
            print('切入新的榜单页面','一共',len(list_link),'页面','当前第',i+1,'页',list_name[i], url)
            # 打开排行榜
            if i == 5: # MV榜单页面结构有问题，暂不爬取
                continue
            self.__browser.get(url) 
            self.implicitly_wait(10)
            list_song.append(self.getSongs())

        return list_name, list_link ,list_song


    def getSongs(self):
        """
        获取排行榜中的歌曲列表
        [['排名','歌曲名称','演唱者','链接'],[],...]
        """
        songs = [['排名','歌曲名称','演唱者','主页', '下载地址']]
        b = self.__browser.find_element_by_class_name('songlist__list') # 所有歌曲列表
        
        for li in b.find_elements_by_tag_name('li'):
            self.implicitly_wait(10)
            rank = int(li.get_attribute('ix')) + 1
            name = li.find_element_by_class_name('js_song').text
            who = li.find_element_by_class_name('songlist__artist').text
            link = li.find_element_by_class_name('js_song').get_attribute('href')

            song = []
            song.append(rank)
            song.append(name)
            song.append(who)
            song.append(link)
            songs.append(song)

            print('QQ音乐--->',rank,name,who,link)

        return songs


class kugouCraw():
    """
    爬取酷狗排行榜
    """
    __browser = None
    __chrome_options = None
    __url = 'https://www.kugou.com/yy/html/rank.html'

    def __init__(self):
        pass

    def start_ui(self, parameter_list=None):
        """
        启动带ui的爬取方式
        """
        kugouCraw.__browser = webdriver.Chrome()
        self.__browser.get(self.__url)


    def start_handless(self, parameter_list=None):
        """
        启动无ui的爬取形式，Headless方式启动
        mac和linux环境要求chrome版本是59+，而windows版本的chrome要求是60+，同时chromedriver要求2.30+版本
        """
        kugouCraw.__chrome_options = webdriver.ChromeOptions()
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
        
        # 所有排行榜名称
        self.implicitly_wait(10)
        m = self.__browser.find_element_by_xpath('/html/body/div[3]/div/div[1]')
        __list = m.find_elements_by_tag_name('li')
        for a in __list:
            # 把排行榜中的链接遍历到列表list_link中
            list_link.append(a.find_element_by_tag_name('a').get_attribute("href"))
            list_name.append(a.find_element_by_tag_name('a').get_attribute("title"))

        print('排行榜列表名称', [name.text for name in __list])
        print('排行榜列表link', [link for link in list_link])

        for index,link in enumerate(list_link):
            self.__browser.get(link) # 打开排行榜
            # self.implicitly_wait()
            print('酷狗-切换榜单',list_name[index])
            list_song.append(self.getSongs())
        
        return list_name, list_link ,list_song


    def getSongs(self):
        """
        获取排行榜中的歌曲列表
        [['排名','歌曲名称','演唱者','链接'],[],...]
        """
        songs = [['排名','歌曲名称','演唱者','主页', '下载地址']]

        b = self.__browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]')
        items = b.find_elements_by_tag_name('li')
        for i in items:
            song = []
            rank = int(i.get_attribute('data-index')) + 1
            name_who = i.get_attribute('title').encode("gbk", 'ignore').decode("gbk", 'ignore')
            who = str(name_who).split('-')[0]
            name = str(name_who).split('-')[1]
            link = i.find_element_by_tag_name('a').get_attribute('href')
            song.append(rank)
            song.append(name)
            song.append(who)
            song.append(link)
            print('--->',rank,name,who,link)
            songs.append(song)
        return songs


class kuwoCraw():
    """
    爬取酷wo排行榜
    """
    __browser = None
    __chrome_options = None
    __url = 'https://www.kuwo.cn/rankList'

    def __init__(self):
        pass

    def start_ui(self, parameter_list=None):
        """
        启动带ui的爬取方式
        """
        kuwoCraw.__browser = webdriver.Chrome()
        self.__browser.get(self.__url)


    def start_handless(self, parameter_list=None):
        """
        启动无ui的爬取形式，Headless方式启动
        mac和linux环境要求chrome版本是59+，而windows版本的chrome要求是60+，同时chromedriver要求2.30+版本
        """
        kuwoCraw.__chrome_options = webdriver.ChromeOptions()
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
        list_name_obj = [] # 排行榜所有名字对象
        
        # 所有排行榜名称
        self.implicitly_wait(10)
        m = self.__browser.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div[2]/div[1]/div/ul')
        __list = m.find_elements_by_tag_name('li')
        for a in __list:
            # 把排行榜中的链接遍历到列表list_link中
            list_name_obj.append(a.find_element_by_class_name('name'))
            list_name.append(a.find_element_by_class_name('name').text)
            list_link.append('https://www.kuwo.cn/rankList')

        print('排行榜名称', [name for name in list_name])

        for song_name in list_name_obj:
            # 打开排行榜
            self.implicitly_wait()
            try:
                print('酷wo-切换榜单',song_name.text)
            except:
                print('酷wo-切换榜单,未找到元素song_name.text')
                
            if song_name.text != '会员畅听榜':
                song_name.click()
                time.sleep(1)
                list_song.append(self.getSongs())
        
        return list_name, list_link ,list_song


    def getSongs(self):
        """
        获取排行榜中的歌曲列表
        [['排名','歌曲名称','演唱者','链接'],[],...]
        """
        songs = [['排名','歌曲名称','演唱者','主页', '下载地址']]

        b = self.__browser.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/ul')
        items = b.find_elements_by_tag_name('li')

        for index,item in enumerate(items):
            song = []
            rank = index + 1

            try:
                name = item.find_element_by_tag_name('a').text
            except:
                name = '无'

            try:
                who = item.find_element_by_class_name('song_artist').text
            except:
                who = '无'

            try:
                link = item.find_element_by_tag_name('a').get_attribute('href')
            except:
                link = '无'
                
            song.append(rank)
            song.append(name)
            song.append(who)
            song.append(link)
            print('--->',rank,name,who,link)
            songs.append(song)
        return songs


if __name__ == "__main__":
    # qq = qqCraw()
    # qq.start_handless()
    # # qq.start_ui()
    # qq.getAllData()
    # qq.quit()

    # kugou = kugouCraw()
    # kugou.start_handless()
    # # kugou.start_ui()
    # kugou.getAllData()
    # kugou.quit()

    kuwo = kuwoCraw()
    kuwo.start_handless()
    # kuwo.start_ui()
    kuwo.getAllData()
    kuwo.quit()
