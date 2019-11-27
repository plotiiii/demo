from selenium import webdriver

wd = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
wd.implicitly_wait(5)

wd.get('http://127.0.0.1/mgr/sign.html')

wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')

wd.find_element_by_tag_name('button').click()

menu=wd.find_element_by_class_name('sidebar-menu')

sp=menu.find_elements_by_tag_name('span')
arr=[]
for ele in sp:
    print(ele.text)
    arr.append(ele.text)

print('**检查点**  侧边栏菜单是否正确', end='')
if arr[:3] ==['客户', '药品', '订单']:
    print("通过")
else:
    print('不通过')
    exit(1)
    wd.quit()



