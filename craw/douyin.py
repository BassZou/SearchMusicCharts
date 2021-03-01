# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class DouCCCraw:
    """
    爬取抖因
    """
    # browser用于存放浏览器对象，读取数据时主要操作此对象
    __browser = None
    __chrome_options = None
    __url = 'https://www.douchacha.com/uppoint'

    def __init__(self):
        pass

    def start_ui(self, parameter_list=None):
        """
        启动带ui的爬取方式
        """
        DouCCCraw.__chrome_options = webdriver.ChromeOptions()
        # 使用headless无界面浏览器模式
        self.__chrome_options.add_argument('--disable-gpu') # 如果不加这个选项，有时定位会出现问题
        self.__chrome_options.add_argument(r"user-data-dir=/Users/zw/Library/Application Support/Google/Chrome/")
        self.__browser = webdriver.Chrome(chrome_options=self.__chrome_options)
        self.__browser.get(self.__url)


    def start_handless(self, parameter_list=None):
        """
        启动无ui的爬取形式，Headless方式启动
        mac和linux环境要求chrome版本是59+，而windows版本的chrome要求是60+，同时chromedriver要求2.30+版本
        """
        DouCCCraw.__chrome_options = webdriver.ChromeOptions()
        # 使用headless无界面浏览器模式
        self.__chrome_options.add_argument('--headless') # 增加无界面选项
        self.__chrome_options.add_argument('--disable-gpu') # 如果不加这个选项，有时定位会出现问题
        # 用浏览器的coolkie
        self.__chrome_options.add_argument(r"user-data-dir=/Users/zw/Library/Application Support/Google/Chrome/")

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
        """
        m = self.__browser.find_element_by_xpath('//*[@id="content-container"]/div[1]/div[2]/div[2]/div/span[15]/button')
        m.click()
        self.implicitly_wait()
        # js="var q=document.getElementById('id').scrollTop=10000"
        # self.__browser.execute_script(js)
        whos = []
        content = self.__browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div[1]/div[2]/div[3]/div/div[3]/table/tbody').find_elements_by_tag_name('tr')
        for item in content:
            w = []
            print('集合长度',len(content))
            lie = item.find_elements_by_tag_name('td')
            rank = lie[0].text
            print('rank',rank)

            name = lie[1].find_element_by_tag_name('span').text
            print('name',name)
            
            fansi = lie[3].find_element_by_tag_name('span').text
            print('fansi',fansi)

            w.append(rank)
            w.append(name)
            w.append(fansi)

            lie[1].click()



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

            print('抖音--->',rank,name,who,link)

        return songs


if __name__ == "__main__":
    dy = DouCCCraw()
    # dy.start_handless()
    dy.start_ui()
    dy.getAllData()
    # dy.quit()
