# -*- coding = utf-8 -*-
# @time=2021/2/9 22:53
# @file daka.py






from mail2 import mail
from selenium import webdriver
import time
from fefe import TestFunc


def code():
    driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[4]').click()
    time.sleep(1)
    captcha = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/img')
    captcha.screenshot('D:/shibie/4.png')
    img = TestFunc()
    print('code:',img)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[3]/div/input').send_keys(img)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/button').click()

root = '学工号'   #填写自己的登录信息
password = '密码'
address='你的住址'
url = 'https://fangkong.hnu.edu.cn/app/'
driver = webdriver.Edge(executable_path="C:\ProgramData\Anaconda3\envs\疫情打卡\Scripts\msedgedriver.exe")


try:
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/input').send_keys(root)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/input').send_keys(password)

    while driver.current_url == 'https://fangkong.hnu.edu.cn/app/#/login':
        code()
        time.sleep(2)
    print('登录成功')

    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div[2]/div[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div/div[2]/div[1]/ul/li[3]').click()
    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div/div[2]/div[1]/ul/li[5]').click()
    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div/div[2]/div[1]/ul/li[7]').click()
    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div/div[2]/div[1]/ul/li[9]').click()
    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div/div[2]/div[1]/ul/li[10]').click()
    time.sleep(1)
    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div/div[2]/div[2]/ul/li[3]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div/div[2]/div[2]/ul/li[5]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div/div[2]/div[2]/ul/li[6]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div/div[1]/button[2]').click()
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/input').send_keys(
        address)
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[3]/div[2]/div[2]/div/i').click()
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[4]/div[2]/div[1]/div/i').click()
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[5]/div[2]/div[2]/div/i').click()
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[6]/div[2]/div[2]/div/i').click()
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[7]/div[2]/div[2]/div/i').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/button').click()

    time.sleep(2)

    driver.close()

except:
    mail('打卡失败')
else:
    mail('打卡成功')






