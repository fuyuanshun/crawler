from selenium.webdriver import Chrome
# import selenium
from selenium.webdriver.common.keys import Keys
import time
import selenium
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    opt = Options()
    opt.add_argument("--headless")
    opt.add_argument("--disable-gpu")

    web = Chrome(options=opt)
    web.get("https://www.endata.com.cn/BoxOffice/BO/Day/index.html")
    time.sleep(3)
    print(web.page_source)
    # print(web.find_element_by_xpath("/html").text)
    # web.find_element_by_xpath('//*[@id="kw"]').send_keys("java", Keys.ENTER)
    # time.sleep(1)
    # web.find_element_by_xpath('//*[@id="3002"]/div[1]/h3/a').click()

    # select_ele = web.find_element_by_xpath('//*[@id="OptionDate"]')
    # select = Select(select_ele)
    # for i in range(len(select.options)):
    #     select.select_by_index(i)
    #     time.sleep(2)
    #     print(web.find_element_by_xpath('//*[@id="TableList"]/table').text)
