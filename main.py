from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
# 从selenium.webdriver.chrome.service导入Service类
# 创建一个Service对象,传入chromedriver的路径
# 在初始化ChromeDriver时,通过service=service参数传入这个Service对象


service = Service(executable_path=r'C:\Users\GentlemanLin\AppData\Local\Programs\Python\Python310\chromedriver.exe')
driver = webdriver.Chrome(service=service)

book_name = 'dpcq'
with open(book_name+".txt",'a+',encoding='utf-8') as f:
    f.write('%'+"斗破苍穹--天蚕土豆"+'%')
    f.write('\n')
    f.close()

for i in range(12657,14302):
    driver.get('https://m.hetushu.com/book/17/'+str(i)+'.html')
    driver.implicitly_wait(5)
    with open(book_name+".txt", 'a+', encoding='utf-8') as f:
        # 通过类名定位
        name = driver.find_element(By.CLASS_NAME, 'title')
        # 输出每章名称
        print(name.text)
        f.write('# ' + name.text + '\n\n')
        u = driver.find_element(By.ID, 'content')
        u = u.text
        for line in u.split("\n"):
            f.write("      " + line + "\n\n")
        f.close()
