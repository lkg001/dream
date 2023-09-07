from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(url="http://www.xinfadi.com.cn/priceDetail.html")

li = []
# 爬取页数
for j in range(45):
    # 每页数据
    for i in range(20):
        time.sleep(0.5)
        res = driver.find_element_by_xpath(f'//div[@class="tablebox"]//tbody//tr[{i+1}]')
        res = res.text
        li.append(res.split(" "))
    # print(li, type(li),li[1])
    time.sleep(1)
    # 换页
    driver.find_element_by_class_name('layui-laypage-next').click()
    time.sleep(1)

# 数据持久化
with open("xfd8-30.csv", "a", encoding="utf-8") as f:
    for i in li:
        # print(i)
        for j in i:
            f.write(j)
            f.write(",")
        f.write("\n")

# time.sleep(1)
# res = driver.find_element_by_xpath(f'//div[@class="tablebox"]//tbody//tr')
# res = res.text
# li = res.split(" ")
# print(li, type(li),li[1])


time.sleep(10)
driver.close()
driver.quit()
