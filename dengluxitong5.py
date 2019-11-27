from selenium import webdriver
import time
# 导入Select类
from selenium.webdriver.support.ui import Select

def delAll(wd):

    while True:
        wd.implicitly_wait(1)
        delButtons = wd.find_elements_by_css_selector(
            '.search-result-item-actionbar label:nth-last-child(1)')

        wd.implicitly_wait(5)

        if not delButtons:
            break

        delButtons[0].click()

        wd.switch_to.alert.accept()

        time.sleep(1)


def addCustomerOrMedicion(field1,field2,field3):
    # 点击添加按钮
    wd.find_element_by_class_name('glyphicon-plus').click()

    # form-contorl 对应3个输入框
    inputs = wd.find_elements_by_css_selector('.add-one-area .form-control')

    # 输入 药品名称
    inputs[0].send_keys(field1)
    # 输入 编号
    inputs[1].send_keys(field2)
    # 输入 描述
    inputs[2].send_keys(field3)

    # 第1个 btn-xs 就是创建按钮， 点击创建按钮
    wd.find_element_by_css_selector('.add-one-area .btn-xs').click()

    # 等待界面刷新稳定
    time.sleep(1)


wd = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
wd.implicitly_wait(5)

wd.get('http://127.0.0.1/mgr/sign.html')

# 根据 ID 选择元素，并且输入字符串
wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')
wd.find_element_by_tag_name('button').click()

# ****  下面是要先删除掉系统中所有的订单、客户和药品  ****

# 点击订单菜单
wd.find_element_by_css_selector('.sidebar-menu li:nth-of-type(4)').click()
delAll(wd)


# 点击药品菜单
wd.find_element_by_css_selector('.sidebar-menu li:nth-of-type(3)').click()
delAll(wd)

# 点击客户菜单
wd.find_element_by_css_selector('.sidebar-menu li:nth-of-type(2)').click()
delAll(wd)


# ****   添加 客户 和 药品 *****

# 点击药品菜单
wd.find_element_by_css_selector('.sidebar-menu li:nth-of-type(2)').click()

addCustomerOrMedicion('南京中医院1','2551867851','江苏省-南京市-秦淮区-汉中路-501')
addCustomerOrMedicion('南京中医院2','2551867852','江苏省-南京市-秦淮区-汉中路-502')
addCustomerOrMedicion('南京中医院3','2551867853','江苏省-南京市-秦淮区-汉中路-503')

# 点击客户菜单
wd.find_element_by_css_selector('.sidebar-menu li:nth-of-type(3)').click()
addCustomerOrMedicion('青霉素盒装1','YP-32342341','青霉素注射液，每支15ml，20支装')
addCustomerOrMedicion('青霉素盒装2','YP-32342342','青霉素注射液，每支15ml，30支装')
addCustomerOrMedicion('青霉素盒装3','YP-32342343','青霉素注射液，每支15ml，40支装')



# ****   添加 订单 *****

# 点击订单菜单
wd.find_element_by_css_selector('.sidebar-menu li:nth-of-type(4)').click()

# 点击添加按钮
wd.find_element_by_class_name('glyphicon-plus').click()

# 输入订单名称
name = wd.find_element_by_css_selector('.add-one-area .form-control')
name.send_keys('南中订单1')

selectElements = wd.find_elements_by_css_selector('.add-one-area select')

Select(selectElements[0]).select_by_visible_text("南京中医院2")
Select(selectElements[1]).select_by_visible_text("青霉素盒装1")

wd.find_element_by_css_selector(
    '.add-one-area input[type=number]')\
    .send_keys('100')


wd.find_element_by_css_selector('.add-one-area .btn-xs').click()


items = wd.find_elements_by_css_selector(
    'div.search-result-item span,div.search-result-item p')[:8]


texts = [item.text for item in items]
print(texts)

orderTime = texts.pop(3)

# 预期内容为
expected = [
'订单：',
'南中订单1',
'日期：',
'客户：',
'南京中医院2',
'药品：',
'青霉素盒装1 * 100'
]

intOrderTime = int(time.mktime(time.strptime(orderTime, '%Y-%m-%d %H:%M:%S')))
curTime = int(time.time())
deviation = abs(intOrderTime-curTime)
print(deviation)

wd.quit()