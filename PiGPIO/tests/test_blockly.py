# views (uses selenium)
import re
import unittest

from selenium import webdriver


class TestBlockly(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/vabene1111/Downloads/chromedriver.exe") # TODO make correct path

    def test_blockly_custom(self):
        self.driver.get("http://192.168.178.83:8000/pigpio/tests/blockly_custom/") # TODO reverse URL

        code = self.driver.execute_script("return getCode()")

        clean_code = re.sub('[^A-Za-z0-9()",]+', '', code)

        self.assertTrue(clean_code == 'fromPiGPIOhelperimportraspifromtimeimportsleepraspisetmode(1)sleep(5)raspilog(str(test),"LOG")raspisetuppin(5,1)raspisetoutput(5,0)raspilog(str((raspigetinput(7))),"LOG")')

    def tearDown(self):
        self.driver.quit


if __name__ == '__main__':
    unittest.main()
