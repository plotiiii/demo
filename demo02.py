from selenium import webdriver
wd=webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# 指每隔0.5秒重新搜索元素 超过10S报错误
wd.implicitly_wait(10)


wd.get('https://www.baidu.com')
ele=wd.find_element_by_id('kw')
ele.send_keys('nba\n')

ele=wd.find_element_by_id('1')
print(ele.text)