# coding=utf-8

from appium import webdriver
import os
import time

class AppDouYinCraw(object):
  """
  抖音App爬取
  __list 需要爬取的所有账号列表
  """
  __data = []
  __driver = None


  """
  # 小米8
  """
  __desired_caps = {
    'platformName': 'Android',
    'deviceName': 'cee23fd3', 
    'platformVersion': '10',
    'appPackage': 'com.ss.android.ugc.aweme',
    "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True,
  }

  """
  oppo 嘉安测试机
  """
  # __desired_caps = {
  #   'platformName': 'Android',
  #   'deviceName': '75AQZL79BQZSMVG6', 
  #   'platformVersion': '9',
  #   'appPackage': 'com.ss.android.ugc.aweme',
  #   "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
  #   'unicodeKeyboard': True,
  #   'resetKeyboard': True,
  # }

      
  def __init__(self, object):
    AppDouYinCraw.__data = object[0]


  def start(self):
    """
    docstring
    """
    self.__driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.__desired_caps) 

    self.click_id('com.ss.android.ugc.aweme:id/am5') # 点击同意政策
    self.swipe_up()
    self.tap(500,500) 
    self.click_xpath('//android.widget.Button[@content-desc="搜索"]') 
    self.input_id('com.ss.android.ugc.aweme:id/ai4','bkswag')
    self.__driver.implicitly_wait(10)
    time.sleep(2)
    self.tap(961,2076) # 点击搜索
    self.click_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/ \
          android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/ \
          android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/ \
          android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/ \
          android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[3]/android.widget.TextView') # 点击用户Tab
    self.__driver.implicitly_wait(10)
    # self.__driver.find_elements_by_class_name('android.view.ViewGroup')[0].click()
    self.click_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/ \
          android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/ \
          android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/ \
          android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/ \
          android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/ \
          androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/ \
          android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/ \
          android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup') # 点击第一个用户
    self.__driver.implicitly_wait(10)
    """
    获取粉丝、关注、点赞、简介、抖音号、年龄、地区
    """
    douyinid = self.__driver.find_element_by_id('com.ss.android.ugc.aweme:id/i94').text
    fansi = self.__driver.find_element_by_id('com.ss.android.ugc.aweme:id/bqv').text
    age = self.__driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/ \
              android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/ \
              android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/ \
              android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/ \
              android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/ \
              android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/ \
              android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]').text
    area = self.__driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/ \
              android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/ \
              android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/ \
              android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/ \
              android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/ \
              android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/ \
              android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]').text
    jj = self.__driver.find_element_by_id('com.ss.android.ugc.aweme:id/i_3').text

    print('id',douyinid)
    print('fansi',fansi)
    print('age',age)
    print('area',area)
    print('jj',jj)

    # -------------------获取抖音详情页作品信息--------------------
    try:
      # 点击作品tab
      self.click_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/ \
                android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/ \
                android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/ \
                android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/ \
                android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/ \
                android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/ \
                android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[2]/android.widget.RelativeLayout/ \
                android.widget.RelativeLayout/android.widget.TextView')
    except:
      print('点击-作品tab-出新问题')

    contents_obj = self.__driver.find_elements_by_id('com.ss.android.ugc.aweme:id/as9')

    for index,item in enumerate(contents_obj):
      if index == 3: #只抓3个作品 
        break
      # 进入作品详情页
      time.sleep(2)
      item.click()
      # 点击 BGM 图标
      time.sleep(2)
      self.tap(973,1922)
      # self.__driver.find_element_by_id('com.ss.android.ugc.aweme:id/ekd').click
      # 获取BGM名称
      bgm_name = self.__driver.find_element_by_id('com.ss.android.ugc.aweme:id/e9v').text
      # 获取BGM使用人数
      bgm_n = self.__driver.find_element_by_id('com.ss.android.ugc.aweme:id/i86').text
      # 返回
      print('歌名',bgm_name,'使用人数',bgm_n)
      self.__driver.keyevent(4)
      self.__driver.implicitly_wait(2)
      self.__driver.keyevent(4)
    
  
  def quit(self):
    self.__driver.quit()


  def input_id(self,id,value):
    """
    输入框
    """
    self.__driver.implicitly_wait(10)
    self.__driver.find_element_by_id(id).click()
    self.__driver.find_element_by_id(id).send_keys(value)



  def swipe_left(self):
    """
    向左滑动
    """
    x = self.__driver.get_window_size()['width']
    y = self.__driver.get_window_size()['height']
    self.__driver.implicitly_wait(10)
    self.__driver.swipe(1/2*x, 1/7*y, 1/2*x, 6/7*y, 200)


  def swipe_up(self):
    """
    向上滑动
    """
    x = self.__driver.get_window_size()['width']
    y = self.__driver.get_window_size()['height']
    self.__driver.implicitly_wait(10)
    self.__driver.swipe(1/2*x, 1/2*y, 1/2*x, 1/7*y, 200)


  def tap(self,x,y):
    self.__driver.implicitly_wait(10)
    self.__driver.tap([(x,y),(x+1,y+1)])


  def click_id(self,value):
    self.__driver.implicitly_wait(10)
    self.__driver.find_element_by_id(value).click()


  def click_xpath(self,value):
    self.__driver.implicitly_wait(10)
    self.__driver.find_element_by_xpath(value).click()





if __name__ == "__main__":

    obj = []
    douyinIds = ['bkswag','小南']
    obj.append(douyinIds)

    dy = AppDouYinCraw(obj)
    dy.start()


      

  

    



        



