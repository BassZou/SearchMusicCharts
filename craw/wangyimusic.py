# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class WangYiMusic:
    """
    爬取网易各个歌曲排行榜
    """
    # browser用于存放浏览器对象，读取数据时主要操作此对象
    browser = None
    url = 'http://www.baidu.com/'

    def __init__(self):
        WangYiMusic.browser = webdriver.Chrome()
        

    def start_ui(self, parameter_list=None):
        """
        启动带ui的爬取方式
        """
        self.browser.get(self.url)
        self.browser.quit()

    def start_handless(self, parameter_list=None):
        """
        启动无ui的爬取形式，Headless方式启动
        mac和linux环境要求chrome版本是59+，而windows版本的chrome要求是60+，同时chromedriver要求2.30+版本
        """
        chrome_options = webdriver.ChromeOptions()
        # 使用headless无界面浏览器模式
        chrome_options.add_argument('--headless') # 增加无界面选项
        chrome_options.add_argument('--disable-gpu') # 如果不加这个选项，有时定位会出现问题

        # 启动浏览器，获取网页源代码
        browser = webdriver.Chrome(chrome_options=chrome_options)
        mainUrl = "https://www.taobao.com/"
        browser.get(mainUrl)
        print(f"browser text = {browser.page_source}")
        browser.quit()




if __name__ == "__main__":
    wy = WangYiMusic()
    wy.start_ui()