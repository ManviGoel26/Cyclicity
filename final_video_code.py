import serial
import time
import pyautogui

previous_command = False
next_command = False
speed = 0
for_pause = True
ports = ["com6 " , "com11"]
#ports = ["com6"]
#   com7 for pedal  com8 for handle
while 1:
    for i in ports:
        ArduinoSerial = serial.Serial(i,9600) #Create Serial port object called arduinoSerialData
        time.sleep(2) #wait for 2 seconds for the communication to get established

        incoming = str(ArduinoSerial.readline()) #read the serial data and print it as line
        print(incoming)

        if i==ports[0]:
            if 'rest' in incoming:
                #speed = 0
                for_pause = True
                if speed>0:
                    pyautogui.press('space')



            if 'play' in incoming and for_pause==True:
                for_pause=False
                #pyautogui.typewrite(['space'], 0.2)
                pyautogui.press('space')

                if speed<=5:
                    for i in range(speed+5):
                        print(i)
                        speed+=2
                        #pyautogui.typewrite([''], 0.2)
                        pyautogui.press(']')
                        pyautogui.press(']')
                        #time.sleep(10)
                else:
                    for i in range(speed):
                        speed-=1
                        pyautogui.press('[')
                        #time.sleep(10)
                speed = 0
                #pyautogui.press('space')   

            if 'speedUp0' in incoming:
                for_pause = True

                if speed<=10:
                    speed+=6
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    #time.sleep(10)
                else:
                    for i in range(0,speed-10):
                        speed-=1
                        pyautogui.press('[')
                        #time.sleep(10)

            if 'speedUp1' in incoming:
                for_pause = True
                if speed<=20:
                    speed+=3
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    #time.sleep(20)
                else:
                    for i in range(0,speed-20):
                        speed-=1
                        pyautogui.press('[')
                        time.sleep(10)

            if 'speedUp2' in incoming:
                for_pause = True
                if speed<=30:
                    speed+=6
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    #time.sleep(20)
                else:
                    for i in range(0,speed-30):
                        pyautogui.press('[')
                        #time.sleep(10)

            if 'speedUp3' in incoming:
                for_pause = True
                if speed<=40:
                    speed+=6
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    pyautogui.press(']')
                    #time.sleep(20)
                else:
                    for i in range(0,speed-40):
                        pyautogui.press('[')
                        #time.sleep(10)
            if 'speedmax' in incoming:
                for_pause= True
                pyautogui.press(']')
                time.sleep(5)

        else:
            if len(incoming)>4:
                print(incoming)
                for i in range(2,len(incoming)):
                    if not incoming[i].isdigit():
                        l = incoming[2:i]
                        break
                incoming = int(l)
                left = 230
                right = 130
                rest = 180
                delta1 = 20
                delta2 = 20

                if (incoming<=(left+delta2) and incoming>=(left-delta2)) and previous_command==False:
                    pyautogui.press('p')
                    print("previous")
                    previous_command = True

                elif (incoming<=(rest+delta1) and incoming>=(rest-delta1)):
                    print("same")
                    previous_command = False
                    next_command = False

                elif (incoming<=(right+delta1) and incoming>=(right-delta1)) and next_command==False:
                    print("right")
                    pyautogui.press('n')
                    next_command = True 
