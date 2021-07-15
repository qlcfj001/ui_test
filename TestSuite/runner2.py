import unittest
import time
import pyautogui
from Page.Base import base
from pageobjct.SearcH import Searchpage
from selenium.webdriver.common.by import By
from vva.Vare import *
from Data.readdata import *
from setlog.log import *
import threading
lg=Logger('MyTestCase').getlog()
class MyTestCase(unittest.TestCase):
    # def test_1(self):
    leave = []
    leave_data = []
    arrive = []
    arrive_data = []
    with open(R"C:\Users\Administrator\Desktop\12.txt", "r") as file:
        # 读取文件内容
        lines = file.readlines()
        for line in lines:
            # # 分割字符串
            leave.append(line.split(',')[0])
            leave_data.append(line.split(',')[1])
            arrive.append(line.split(',')[2])
            arrive_data.append(line.split(',')[3])
        # return leave, leave_data, arrive, arrive_data
class MyTestCase1(MyTestCase,Searchpage,base):

    def test_1(self):
        ba=base()
        time.sleep(10)
        # 点击火车
        self.search().click()
        # 往返
        self.search1().click()
        # 输入起点位置
        self.search2().send_keys(MyTestCase.leave[1])
        lg.info("起点位置:"+MyTestCase.leave[1])
        time.sleep(2)
        # 输入出发发时间
        self.search3().send_keys(MyTestCase.leave_data[1])
        lg.info("出发时间:" + MyTestCase.leave_data[1])
        time.sleep(5)
        # 输入终点站MyTestCase.arrive[0]
        self.search5().send_keys(MyTestCase.arrive_data[1])
        lg.info("终点站:" + MyTestCase.arrive_data[1])
        time.sleep(3)
        # # 输入到达时间MyTestCase.arrive_data[0]
        self.search4().send_keys(MyTestCase.arrive[1])
        lg.info("到达时间:" + MyTestCase.arrive[1])
        lg.exception('oppp',exc_info=True)
        # 输入返程日期后点击空白处，让日期框消失
        # pyautogui.moveTo(580, 432)
        # pyautogui.click()
        # print('ss')
        time.sleep(5)
        # 点击搜索
        self.search6().click()
        ff=self.driver.find_element_by_xpath('//*[@id="base_bd"]/div[1]/b').text
        self.assertEqual(ff, '福州到成都火车票','pass')
        lg.info('搜索到的火车票是:' + ff)
    time.sleep(2)
    # def test_2(self):
    #     ba=base()
    #     time.sleep(10)
    #     # 点击火车
    #     self.search().click()
    #     # 往返
    #     self.search1().click()
    #     # 输入起点位置
    #     self.search2().send_keys(MyTestCase.leave[0])
    #     lg.info("起点位置:"+MyTestCase.leave[0])
    #     time.sleep(2)
    #     # 输入出发发时间
    #     self.search3().send_keys(MyTestCase.leave_data[0])
    #     lg.info("出发时间:" + MyTestCase.leave_data[0])
    #     time.sleep(5)
    #     # 输入终点站MyTestCase.arrive[0]
    #     self.search5().send_keys(MyTestCase.arrive_data[0])
    #     lg.info("终点站:" + MyTestCase.arrive_data[0])
    #     time.sleep(3)
    #     # # 输入到达时间MyTestCase.arrive_data[0]
    #     self.search4().send_keys(MyTestCase.arrive[0])
    #     lg.info("到达时间:" + MyTestCase.arrive[0])
    #     # 输入返程日期后点击空白处，让日期框消失
    #     # pyautogui.moveTo(580, 432)
    #     # pyautogui.click()
    #     # print('ss')
    #     time.sleep(5)
    #     # 点击搜索
    #     self.search6().click()
    #     ff=self.driver.find_element_by_xpath('//*[@id="base_bd"]/div[1]/b').text
    #     lg.info('搜索到的火车票是:'+ff)
    #     # self.assertEqual(ff, '福州到成都的火车票','pass'
    threads=[]
    t1=threading.Thread(target=test_1())
    threads.append(t1)
    print(len(threads))
a=0
if __name__ == '__main__':
    for t in MyTestCase1.threads:
        t.start()
        a+=1
    print(a)
    for t in MyTestCase1.threads:
        t.join()
