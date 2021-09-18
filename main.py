# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import time
import urllib.request

import pygame
import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # 循环
    print("1.循环")
    for i in range(1, 10):
        print(i)
    # 列表
    print("2.列表")
    stringList = ["apple", "pear", "orange", "purple"]
    for str in stringList:
        print(str)
    # 字典
    print("3.字典")
    dicList = {0: 'apple', 1: 'pear', 2: 'orange', 3: 'purple'}
    for i in range(0, 4):
        print(dicList[i])

    # 时间
    print("4.时间")
    print("当前的时间戳为：{}".format(time.time()))

    # IO
    print("5.IO")
    # raw = input("请输入：")
    # print("你输入的是：{}".format(raw))

    # 文件读取
    print("6.文件读取")
    # with open('ofile.txt',"r") as f:
    #     print(f.read())
    # 每行读取
    file = open('ofile.txt', "r")
    for line in file.readlines():
        line = line.strip()
        print(line)
    file.close()
    # 网络请求
    print("网络请求")
    # response = urllib.request.urlopen("http://www.zhihu.com")
    # print(response.read())
    proxy = {
        "http":"http://127.0.0.1:7890",
        "https":"http://127.0.0.1:7890"
    }
    resp = requests.get("http://www.google.com",proxies=proxy)
    print(resp.text)
class Android():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("logo.ico")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_right==True:
            self.center+=0.1
        if self.moving_left==True:
            self.center-=0.1

        self.rect.centerx = self.center



#配置
class Settings():
    screen_width = 400
    screen_height = 400
    bg_color = (230, 230, 230)

def runGame():
    print("开启游戏...")
    # 初始化游戏
    pygame.init()
    settings = Settings
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    # 初始化
    android = Android(screen)
    # 设置图标0
    logo= pygame.image.load('logo.ico')
    pygame.display.set_icon(logo)
    # 设置标题
    pygame.display.set_caption("my game")
    # 游戏循环
    while True:
        check_event(android)
        update_screen(screen,settings.bg_color,android)
# 监听事件
def check_event(android):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                android.moving_right=True
                android.moving_left = False
            if event.key==pygame.K_a:
                android.moving_left=True
                android.moving_right=False
        elif event.type==pygame.KEYUP:
            android.moving_right=False
            android.moving_left=False


# 刷新屏幕
def update_screen(screen,bg_color,android):
    screen.fill(bg_color)
    android.blitme()
    android.update()
    pygame.display.flip()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    runGame()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
