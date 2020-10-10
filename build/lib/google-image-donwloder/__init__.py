import os
import requests as req
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen, urlretrieve


class Downloader:
    count: int = 1

    def __init__(self, keyword, url):
        self.keyword = keyword
        self.url = url

    def createBroswer(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

        path = "./driver/chromedriver.exe"

        if not os.path.exists(path):
            path = "chromedriver.exe"

        self.browser = webdriver.Chrome(
            executable_path=path)
        self.browser.get(self.url.format(self.keyword))

    def download(self):
        self.createBroswer()

        if not os.path.exists(self.keyword):
            os.mkdir(self.keyword)

        for _ in range(500):
            self.browser.execute_script("window.scrollBy(0,10000)")

        for x in self.browser.find_elements_by_tag_name("img"):
            url = x.get_attribute('src')

            if url != None:
                if url[0] == 'h':
                    print("[+] url : ", url)

                    target = urlopen(url).read()
                    image = "{}_".format(self.keyword) + \
                        str(self.count) + ".png"

                    urlretrieve(url, './{}/'.format(self.keyword) + image)
                    self.count += 1
                else:
                    pass
            else:
                pass

        print('[+] download image : ', self.count - 1)

        self.browser.close()
