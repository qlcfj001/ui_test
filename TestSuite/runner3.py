import time
import pyautogui
from Page.Base import base
from pageobjct.SearcH import Searchpage
from selenium.webdriver.common.by import By
from TestSuite.Variablelayer.Variable import *
from TestSuite.Data.readdata import *
from TestSuite.setlog.log import *
from TestSuite.runner2 import *
lg=Logger('MyTestCase').getlog()
import unittest
import threading
#大指量的测试用例也通过suite去添加执行？
#定义测试用例的目录为当前目录
threads=[]
# test_dir='./'#'./'当前目录
# discover=unittest.defaultTestLoader.discover(test_dir,pattern='runner2.py')
# runner=unittest.TextTestRunner()
# t1=threading.Thread(target=runner.run(discover))
# threads.append(t1)
# print(threads)
lg=MyTestCase1()
t1=threading.Thread(target=test_1())
threads.append(t1)
print(len(threads))
a=0
if __name__ == '__main__':
    for t in threads:
        t.start()
        a+=1
    print(a)
    for t in threads:
        t.join()

# lg=MyTestCase1()
# t1=threading.Thread(target=lg.test_1())
# threads.append(t1)