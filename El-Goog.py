import requests
import time
import json
import datetime
import os

os.system('cls')
ipAddress = 'http://' + input('IP Address: ') + ':8008'
interval = (float(input('Interval: ')) * 60)

def albola ():

    os.system('cls')
    
    while True:

        info = json.loads(requests.get('{}/setup/assistant/alarms'.format(ipAddress)).text)
        alarms = len(info['alarm'])

        if alarms != 0:
            print('----------------------------------------------------------------')
            print('[{}] {} alarm(s) detected!'.format(datetime.datetime.now().strftime('%X'), alarms))
            for i in info['alarm']:
                alarmID = i['id']
                requests.post('{}/setup/assistant/alarms/delete'.format(ipAddress), json={'ids': [alarmID]})
                print('[{}] Destroyed alarm: {}'.format(datetime.datetime.now().strftime('%X'), alarmID.replace('alarm/', '')))
            print('----------------------------------------------------------------')
        else:
            print('[{}] No alarms detected.'.format(datetime.datetime.now().strftime('%X')))
        
        time.sleep(interval)

def reboot ():
    os.system('cls')
    requests.post('{}/setup/reboot'.format(ipAddress), json={"params": "now"})
    print('[{}] BOOM! You just got dat rebooterino son!'.format(datetime.datetime.now().strftime('%X')))
    time.sleep(2)
    input('\n[{}] Press ENTER to go back to the main menu...'.format(datetime.datetime.now().strftime('%X')))
    mainMenu()

def factoryReset ():
    os.system('cls')
    requests.post('{}/setup/reboot'.format(ipAddress), json={"params": "fdr"})
    print('[{}] Deadass B? You just factory reset that bitch!'.format(datetime.datetime.now().strftime('%X')))
    time.sleep(2)
    input('\n[{}] Press ENTER to go back to the main menu...'.format(datetime.datetime.now().strftime('%X')))
    mainMenu()

def mainMenu ():
    os.system('cls')
    print('-----------------------')
    print('| Welcome to El Goog! |')
    print('-----------------------\n')
    choice = input('[1] Fuck Your Alarms\n[2] Rebooterino\n[3] Factory Reseterino\n\n> ')
    if choice == '1':
        albola()
    if choice == '2':
        reboot()
    if choice == '3':
        factoryReset()
    else:
        mainMenu()

mainMenu()