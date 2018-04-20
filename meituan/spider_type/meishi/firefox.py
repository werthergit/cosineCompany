
from selenium import webdriver


profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)   #默认值0，就是直接连接；1就是手工配置代理。

profile.set_preference('network.proxy.socks', '123.123.23.3')

profile.set_preference('network.proxy.socks_port', '8080')

# profile.set_preference('network.proxy.ssl','')
# profile.set_preference('network.proxy.ssl_port', '')
profile.update_preferences()
browser = webdriver.Firefox(profile)
browser.get("http://www.ip138.com")