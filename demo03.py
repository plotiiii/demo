from selenium import webdriver
wd=webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
wd.get('http://f.python3.vip/webauto/sample1a.html')

ele=wd.find_elements_by_css_selector('#t1>span,#t1>p')
for element in ele:
    print(element.text)