from flask import Flask,render_template,Response,redirect,url_for
import cv2
import HandTrackingModule as htm
import autopy
import numpy as np
import pyautogui
import screen_brightness_control as scb
from time import sleep
app=Flask(_name_)
camera=cv2.VideoCapture(0)
detector=htm.handDetector(maxHands=1)
wScr,hScr=autopy.screen.size()
def generate_frames():
    counter=0
    mc=0
    while True:
        success,frame=camera.read()
        if not success: 
            break
        else:
            plocX,plocY=0,0
            clocX,clocY=0,0
            smoothening=7
            frameR=100
            frame=detector.findHands(frame)
            lmList,bbox=detector.findPosition(frame)
            counter=counter+1
            mc=mc+1
            if len(lmList)!=0:
                x1,y1=lmList[8][1:]
                x2,y2=lmList[12][1:]
                fingers=detector.fingersUp()
                if mc%5==0:
                    if fingers[1]==1 and fingers[2]==0 and fingers[0]==0 and fingers[3]==0 and fingers[4]==0:
                        cv2.rectangle(frame,(frameR,frameR),(640-frameR,480-frameR),(255,0,255),2)
                        x3 = np.interp(x1, (frameR, 640-frameR), (0, wScr))
                        y3 = np.interp(y1, (frameR,480-frameR), (0, hScr))
                        clocX=plocX+(x3-plocX)/smoothening
                        clocY=plocY+(y3-plocY)/smoothening
                        autopy.mouse.move(x3,y3)
                        cv2.circle(frame,(x1,y1),15,(255,0,255),cv2.FILLED)
                        plocX,plocY=clocX,clocY
                    if fingers[1]==1 and fingers[2]==1 and fingers[0]==0 and fingers[3]==0 and fingers[4]==0:
                        length,frame,lineInfo=detector.findDistance(8,12,frame)
                        if length<40:
                            cv2.circle(frame,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
                            autopy.mouse.click()
                    mc=0
                if counter%30==0:
                    if fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[0]==0  and fingers[4]==0:
                        pyautogui.press("up")
                        sleep(2)
                    if fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
                        pyautogui.press("down")
                        sleep(2)
                    if fingers[0]==1 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1:
                        pyautogui.press("space")
                        sleep(2)
                    if fingers[0]==0 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1:
                        pyautogui.press("right")
                        sleep(2)
                    if fingers[0]==1 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==0:
                        pyautogui.press("left")
                        sleep(2)
                    if fingers[0]==1 and fingers[1]==1 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
                        length,frame,lineInfo=detector.findDistance(4,8,frame)
                        blevel=np.interp(length,[25,145],[0,100])
                        blevel=int(blevel)
                        scb.set_brightness(blevel)
                    counter=0
        ret,buffer=cv2.imencode('.jpg',frame)
        frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/start',methods=['POST'])
def start():
    return redirect(url_for('main'))

@app.route('/index')
def main():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if _name=="main_":
    app.run(debug=True)