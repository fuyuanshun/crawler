from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client
from selenium.webdriver.chrome.options import Options
import time

url = "https://kyfw.12306.cn/otn/resources/login.html"

def verify_img(web):
    chaojiying = Chaojiying_Client('17839002230', 'fkpfkp521', '914747')  # 用户中心>>软件ID 生成一个替换 96001
    img_ele = web.find_element_by_xpath('//*[@id="J-loginImg"]')
    img_byte = img_ele.screenshot_as_png
    for i in chaojiying.PostPic(img_byte, 9004)['pic_str'].split("|"):
        chain = ActionChains(web)
        chain.move_to_element_with_offset(img_ele, int(i.split(",")[0]), int(i.split(",")[1])).click().perform()
    web.find_element_by_xpath('//*[@id="J-login"]').click()
    time.sleep(3)
    img = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
    ActionChains(web).drag_and_drop_by_offset(img, 300, 0).perform()
if __name__ == '__main__':
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    web = Chrome(options = options)
    web.get(url)
    web.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a").click()
    web.find_element_by_xpath('//*[@id="J-userName"]').send_keys("849485789@qq.com")
    web.find_element_by_xpath('//*[@id="J-password"]').send_keys("fukaipeng_789")
    verify_img(web)