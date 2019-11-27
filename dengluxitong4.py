from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

def adda(a,b,c):
    wd.find_element_by_class_name('glyphicon-plus').click()
    inputs=wd.find_elements_by_css_selector('.add-one-area .form-control')
    inputs[0].send_keys(a)
    inputs[1].send_keys(b)
    inputs[2].send_keys(c)

    wd.find_element_by_css_selector('.add-one-area .btn-xs').click()
    time.sleep(1)


wd = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
wd.implicitly_wait(5)

wd.get('http://127.0.0.1/mgr/sign.html')

# 根据 ID 选择元素，并且输入字符串
wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')
wd.find_element_by_tag_name('button').click()
#li:nth-of-type(2)
wd.find_element_by_css_selector('.sidebar-menu li:nth-of-type(2)').click()
adda('南京中医院1','2551867851','江苏省-南京市-秦淮区-汉中路-501')
adda('南京中医院2','2551867852','江苏省-南京市-秦淮区-汉中路-502')
adda('南京中医院3','2551867853','江苏省-南京市-秦淮区-汉中路-503')

wd.find_element_by_css_selector('.sidebar-menu li:nth-of-type(3)').click()
adda('南京中医院1','2551867851','江苏省-南京市-秦淮区-汉中路-501')
adda('南京中医院2','2551867852','江苏省-南京市-秦淮区-汉中路-502')
adda('南京中医院3','2551867853','江苏省-南京市-秦淮区-汉中路-503')

wd.find_element_by_css_selector('.sidebar-menu li:nth-of-type(4)').click()
wd.find_element_by_class_name('glyphicon-plus').click()
name=wd.find_element_by_css_selector('.add-one-area .form-control')
name.send_keys('南中订单1')

selecet=wd.find_elements_by_css_selector('.add-one-area select')
# 选择客户
Select(selecet[0]).select_by_visible_text("南京中医院2")
# 选择药品
Select(selecet[1]).select_by_visible_text("青霉素盒装1")

wd.find_element_by_css_selector('.add-one-area input[type=number]')\
                                .send_keys('100')

wd.find_element_by_css_selector('.add-one-area .btn-xs').click()
wd.quit()