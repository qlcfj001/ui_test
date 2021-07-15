# -*-coding:utf-8 -*-
import time
import logging
class Logger(object):
    def __init__(self,logger):
        #创建一个loggerLoggr
        self.logger=logging.getLogger(logger)
        #设置日志级别
        self.logger.setLevel(logging.INFO)
        #创建一个handler，用于写入到日志文件
        rq=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
        log_path='./'
        #日志名称
        log_name=log_path+rq+'.log'

        #将日志信息输出那里
        filehandler=logging.FileHandler(log_name,'a')
        filehandler.setLevel(logging.INFO)

        #再创建一个handler,用于输出到控制台
        chandler=logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        #定义handler的输出格式
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(filename)s- %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)
        chandler.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(filehandler)
        self.logger.addHandler(chandler)
    def getlog(self):
        return self.logger

""" % (levelno)s：打印日志级别的数值
    % (levelname)s：打印日志级别的名称
    % (pathname)s：打印当前执行程序的路径，
    % (filename)s：打印当前执行程序名
    % (funcName)s：打印日志的当前函数
    % (lineno)d：打印日志的当前行号
    % (asctime)s：打印日志的时间
    % (thread)d：打印线程ID
    % (threadName)s：打印线程名称
    % (process)d：打印进程ID
    % (message)s：打印日志信息 """
