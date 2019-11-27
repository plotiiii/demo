from selenium import webdriver
from time import sleep

wd = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
wd.implicitly_wait(5)

wd.get('http://127.0.0.1/mgr/sign.html')

# 根据 ID 选择元素，并且输入字符串
wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')
wd.find_element_by_tag_name('button').click()

#找到上层节点，缩小搜索范围
sidebar=wd.find_element_by_class_name('sidebar-menu')
sp=sidebar.find_elements_by_tag_name('span')
#点击第几个在SP后面添加
sp[0].click()
sleep(1)

wd.find_element_by_css_selector(
    '.search-result-item-actionbar label').click()

cli=wd.find_element_by_css_selector(
    '.search-result-item input')
cli.clear()

cli.send_keys('南京省中医院')

wd.find_element_by_css_selector('.search-result-item-actionbar label').click()

wd.quit()