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

#搜索添加客户按钮
wd.find_element_by_class_name('glyphicon-plus').click()
inputs=wd.find_element_by_class_name('add-one-area')\
    .find_elements_by_class_name('form-control')
inputs[0].send_keys('南京中医院')
inputs[1].send_keys('2551867858')
inputs[2].send_keys('江苏省-南京市-秦淮区-汉中路-16栋504')

wd.find_element_by_class_name('add-one-area')\
    .find_element_by_class_name('btn-xs').click()
#点击后记得等待1S
sleep(1)
#要加item
item=wd.find_elements_by_class_name('search-result-item')[0]
fields=item.find_elements_by_tag_name('span')[:6]
texts=[field.text for field in fields]
print(texts)

expected=[
'客户名：',
'南京中医院',
'联系电话：',
'2551867858',
'地址：',
'江苏省-南京市-秦淮区-汉中路-16栋504'
]

print('----------------------')
#要texts等于自己创建的数组
if texts==expected:
    print('通过')
else:
    print(不通过)
    exit(1)
wd.quit()










