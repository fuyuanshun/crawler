from chaojiying import Chaojiying_Client
from selenium.webdriver import Chrome

url = "http://www.chaojiying.com/user/login/"

if __name__ == '__main__':
    web = Chrome()
    web.get(url)
    web.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input").send_keys("17839002230")
    web.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input").send_keys("fkpfkp521")
    png = web.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/div/img").screenshot_as_png

    chaojiying = Chaojiying_Client('17839002230', 'fkpfkp521', '914747')  # 用户中心>>软件ID 生成一个替换 96001
    web.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input").send_keys(chaojiying.PostPic(png, 1902)['pic_str'])
    web.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input").click()