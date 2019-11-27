from selenium import webdriver
wd=webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
wd.get('http://f.python3.vip/webauto/sample2.html')
#wd.switch_to.frame(wd.find_elements_by_tag_name('iframe'))
wd.switch_to.frame('innerFrame')
ele=wd.find_elements_by_class_name('plant')
for element in ele:
    print(element.text)

wd.switch_to.default_content()
wd.find_element_by_id('outerbutton').click()
