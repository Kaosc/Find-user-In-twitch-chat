from selenium import webdriver
from selenium.webdriver.common.by import By
from colored import fg, attr
import time
import warnings
import os
import sys

warnings.filterwarnings("ignore", category=DeprecationWarning)

class Twitch:

    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_argument("--log-level=3")
        self.browserProfile.add_argument('--hide-scrollbars')
        self.browserProfile.add_argument('--lang=en')
        self.browserProfile.add_argument('--headless')
        self.browserProfile.add_argument('--disable-gpu')
        self.browserProfile.add_argument('--mute-audio')
        self.browserProfile.add_argument('window-size=1920,1080')
        self.browserProfile.add_argument('window-position=0,0')
        self.browserProfile.add_experimental_option('excludeSwitches',['enable-logging'])
        self.browserProfile.add_experimental_option('prefs',{"intl.accept_languages":"en,en_US"})

    def listCheck(self, nickname):
        os.system("cls")
        self.nickname = nickname
        count = 0
        founded = False
        channels = []

        collectLink = f"https://www.twitchdatabase.com/following/{self.nickname}"

        self.browser = webdriver.Chrome("driver/chromedriver.exe", chrome_options=self.browserProfile)
        
        self.browser.get(collectLink)
        time.sleep(2)

        row = self.browser.find_elements(By.CLASS_NAME, "row")
        channelEl = row[2].find_elements(By.TAG_NAME, 'a')

        for i in channelEl:
            channels.append(i.get_attribute("href"))
        
        while count < len(channels):
            print(f"%s\n - CONNECTED CHANNEL {channels[count]} %s" % (fg(56), attr(0)))
            self.browser.get(channels[count])
            time.sleep(1)

            try:
                self.browser.find_element(By.XPATH,'//*[@aria-label="Community"]').click()
            except:
                print(f"\n%s - CHANNEL OFFLINE %s" % (fg(1), attr(0)))
                count+=1
                continue

            print(f"%s\n - SEARCHING THE USER%s" % (fg(3), attr(0)))
            time.sleep(3)
            self.browser.find_element(By.XPATH,'//*[@placeholder="Filter"]').send_keys(self.nickname)
            print(f"%s - RESULTS ARE LOADING%s" % (fg(3), attr(0)))
            time.sleep(2)

            try:
                userpath = f'//*[@aria-label="Open details for {str(self.nickname)}"]'
                self.browser.find_element(By.XPATH, userpath)
                print(f"%s - USER CONFIRMED AT {channels[count]} %s" % (fg(2), attr(0)))
                self.browser.close()
                founded = True
            except:
                print(f"%s - USER CANNOT FOUND%s" % (fg(88), attr(0)))
                count+=1
        
            if(founded == True):
                break
        
        os.system("cls")
        print(f"%s\n - USER CANNOT FOUND AT ALL%s" % (fg(1), attr(0)))
        self.browser.close()

    def soloCheck(self,channel,nickname):
        os.system("cls")
        
        count = 0
        founded = False
        self.nickname = nickname
        self.channel = channel
        self.browser = webdriver.Chrome("driver/chromedriver.exe", chrome_options=self.browserProfile)

        while True:
            os.system("cls")
            self.browser.get(f"https://www.twitch.tv/{self.channel}")
            print(f"%s\n - CONNECTED TO CHANNEL%s" % (fg(3), attr(0)))
            time.sleep(2)
            
            try:
                self.browser.find_element(By.XPATH,'//*[@aria-label="Community"]').click()
            except:
                self.browser.close()
                print(f"%s\n CHANNEL OFFLINE %s" % (fg(1), attr(0)))
                break
                
            print(f"%s - SEARCHING THE USER%s" % (fg(3), attr(0)))
            time.sleep(2)
            self.browser.find_element(By.XPATH,'//*[@placeholder="Filter"]').send_keys(self.nickname)
            print(f"%s - RESULTS ARE LOADING%s" % (fg(3), attr(0)))
            time.sleep(2)

            try:
                userpath = f'//*[@aria-label="Open details for {str(self.nickname)}"]'
                self.browser.find_element(By.XPATH, userpath)
                print(f"%s - USER CONFIRMED AT {channel} %s" % (fg(2), attr(0)))
                self.browser.close()
                founded = True
            except:
                print(f"%s - USER CANNOT FOUND%s" % (fg(1), attr(0)))
                count+=1

            if(founded == True):
                break

            totalcount = str(count)
            print(f"%s\n - Total Checks: {totalcount}%s" % (fg(61), attr(0)))

            for timer in range(10,0,-1):
                time.sleep(1)
                os.system("cls")
                print(f"%s\n -> Trying again in: {timer} %s" % (fg(70), attr(0)))

twitch = Twitch()

while True:
    print(f"%s\n The user nick name is case sensitive! %s\n" % (fg(1), attr(0)))
    print("%s - - - TWITCH USER FINDER - - - \n %s" % (fg(57), attr(0)))
    opt = input("""%s [1] - Find in following channels \n [2] - Search in a spesific channel (Loop) \n [3] - Exit \n\n Enter Number:  %s""" % (fg(57), attr(0)))
    if opt == "3":
        sys.exit()
    elif opt == "2":
        nick = input(f"%s\n User Nickname: %s" % (fg(2), attr(0)))
        target = input(f"%s\n Target Channel: %s" % (fg(2), attr(0)))
        twitch.soloCheck(nickname=nick,channel=target)
    elif opt == "1":
        nick = input(f"%s\n User Nickname: %s" % (fg(2), attr(0)))
        twitch.listCheck(nick)