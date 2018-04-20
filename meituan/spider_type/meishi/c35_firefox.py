
from selenium import webdriver
import time
import os
import requests
import random

city= "wh"
type="c35"

def randHeader():
    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html, application/xhtml+xml, */*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = [
                       'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
                       'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36',
                       'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
                       'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
                       'Mozilla/5.0 (Linux; Android 6.0.1; SM-G900V Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
                       'Mozilla/5.0 (iPad; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11',
                       'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36']

    header = {
        'Connection': head_connection[0],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]
    }
    #return header
    agent = head_user_agent[random.randrange(0, len(head_user_agent))]
    return agent

def get_start_menu_links(name):

    print(randHeader())
    #agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36'
    agent = randHeader()

    driver = webdriver.Firefox()
    driver.get(r"http://wh.meituan.com/")

    print("登录之前：")

    # 打印打钱页面的title
    title = driver.title
    print(title)


    url="http://"+city+".meituan.com/meishi/"+type+"/"+name+'/'
    print(url)


    try:
        print('dddddddd')
        driver.get(url)  # Load page
        html = driver.page_source
        # basic_values = browser.find_element_by_xpath("//script[@id='lego-widget-fallback-lego-widget-play-mt-map-200-000']/text()")
        # print(basic_values)
        content = html
        content = content.encode("utf-8")
        #print('----->' + content)
        dir = 'E:\\tyc\\company\\'+city+'\\'+type+'\\'
        if os.path.exists(dir) == False:
             os.mkdir(dir)
        f = open(dir + "\\" + name + '.html', 'wb+')
        f.write(content)
        f.close()


    except  Exception:
        assert 0, "list"
    time.sleep(30)
    driver.close()


if '__main__' == __name__:
    for i in range(1, 2): #18
        get_start_menu_links('pn'+str(i))
        time.sleep(random.randint(30, 80))  # Let the page load, will be added to the API