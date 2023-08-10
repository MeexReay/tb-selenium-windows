from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os
import time

def get_tor_driver(geckodriver_path,tor_dir_path):
    tor_dir_path = tor_dir_path.replace("/","\\")
    if tor_dir_path.endswith("\\"): tor_dir_path = tor_dir_path[:2]
    geckodriver_path = geckodriver_path.replace("/","\\")
    if geckodriver_path.endswith("\\"): geckodriver_path = geckodriver_path[:2]
    os.environ['TOR_SOCKS_HOST'] = '127.0.0.1'
    os.environ['TOR_SOCKS_PORT'] = '9150'
    options = Options()
    options.set_preference("profile",tor_dir_path+'\\Browser\\TorBrowser\\Data\Browser\\profile.default')
    options.set_preference('network.proxy.type', 1)
    options.set_preference('network.proxy.socks', '127.0.0.1')
    options.set_preference('network.proxy.socks_port', 9150)
    options.set_preference("network.proxy.socks_remote_dns", False)
    options.set_preference("intl.language_notification.shown", True)
    options.set_preference("intl.locale.requested", "en-US,ru-RU")
    options.set_preference("torbrowser.migration.version", 1)
    options.set_preference("torbrowser.settings.bridges.builtin_type", "")
    options.set_preference("torbrowser.settings.bridges.enabled", False)
    options.set_preference("torbrowser.settings.bridges.source", -1)
    options.set_preference("torbrowser.migration.version", 1)
    options.set_preference("torbrowser.settings.enabled", True)
    options.set_preference("torbrowser.settings.firewall.enabled", False)
    options.set_preference("torbrowser.settings.proxy.enabled", False)
    options.set_preference("torbrowser.settings.quickstart.enabled", True)
    options.binary_location = tor_dir_path+'\\Browser\\firefox.exe'
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(options=options, service=service)
    time.sleep(1)
    driver.find_element(By.ID,"connectButton").click()
    time.sleep(1)
    driver.find_element(By.ID,"connectButton").click()
    time.sleep(1)
    return driver

if __name__ == "__main__":
    import atexit
    
    driver = get_tor_driver(
      "C:/Program Files/geckodriver/geckodriver.exe",
      "C:/Users/User/Desktop/Tor Browser/")
    
    atexit.register(driver.quit) # quit tor at exit
    
    driver.get("http://check.torproject.org")
