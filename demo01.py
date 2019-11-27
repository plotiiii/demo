from selenium import webdriver
wd=webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

wd.get('http://f.python3.vip/webauto/sample1.html')
#搜索在container类下面所有的span元素
element=wd.find_element_by_id('container')
spans=element.find_elements_by_tag_name('span')

for span in spans:
    print(span.text)