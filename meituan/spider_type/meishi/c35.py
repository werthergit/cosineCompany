
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

    session = requests.session()
    ips = session.get('http://pvt.daxiangdaili.com/ip/?tid=559621594650685&num=1').text
    #print('--proxy-server=%s' % ips)
    #proxies = {'http': ips}
    #PROXY = "23.23.23.23:3128"  # IP:PORT or HOST:PORT

    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % ips)


    print(randHeader())
    #agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36'
    agent = randHeader()
    options.add_argument('--user-agent=%s' % agent)
    #origin = 'wh.meituan.com'
    #options.add_argument("--host=%s" % origin)
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    #chrome正受到自动测试软件的控制
    options.add_argument('disable-infobars')
    #不加载图片 start
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2
        }
    }
    options.add_experimental_option('prefs', prefs)
    ##不加载图片


    browser = webdriver.Chrome(chrome_options=options) # Get local session of firefox

    url="http://"+city+".meituan.com/meishi/"+type+"/"+name+'/'
    print(url)

    try:
        #browser.get(r"http://wh.meituan.com/")
        #time.sleep(2)
        print('dddddddd')
        browser.get(url)  # Load page
        html = browser.page_source
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
    browser.close()


if '__main__' == __name__:
    for i in range(1, 2): #18
        get_start_menu_links('pn'+str(i))
        time.sleep(random.randint(30, 80))  # Let the page load, will be added to the API