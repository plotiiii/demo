from selenium import webdriver
from time import sleep


wd = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
wd.implicitly_wait(5)

wd.get('http://127.0.0.1/mgr/sign.html')

# 根据 ID 选择元素，并且输入字符串
wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')
wd.find_element_by_tag_name('button').click()

wd.find_element_by_css_selector('.sidebar-menu li:nth-of-type(3)').click()
wd.find_element_by_class_name('glyphicon-plus').click()
inputs=wd.find_elements_by_css_selector('.add-one-area .form-control')

inputs[0].send_keys('青霉素盒装1')
# 输入 编号
inputs[1].send_keys('YP-32342349')
# 输入 描述
inputs[2].send_keys('青霉素注射液，每支15ml，20支装')

wd.find_element_by_css_selector('.add-one-area .btn-xs').click()
#点击创建后记得sleep 1S
sleep(1)
items=wd.find_elements_by_css_selector('div.search-result-item span')[:6]
texts=[item.text for item in items]
print(texts)
print('---------------------')
expected=[
'药品：',
'青霉素盒装1',
'编号：',
'YP-32342349',
'描述：',
'青霉素注射液，每支15ml，20支装'
]
if texts==expected:
    print('1')
else:
    print('2')
    exit(1)
wd.quit()


