import time
import unittest

import HTMLTestRunnerNew

test_dir = './'

# 执行所有用例将 pattern 参数改成 *
# discover0 = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='class_0614_testcase.py')


if __name__ == "__main__":
    now = time.strftime('%Y-%m-%d_%H_%M_%S')  # 引入时间戳，获取当前时间
    file_path = 'home_work' + now + '.html'
    fp = open(file_path, 'wb')  # 打开一个保存结果的html文件
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=fp, title='api测试报告', description='测试情况')
    runner.run(discover)