# -*- coding: utf-8 -*-

import os
import subprocess

CMD_SCREEN_SHOT = 'adb shell screencap -p /sdcard/aJump.jpg'
CMD_SAVE_TO_LOCAL = 'adb pull %s %s'
CMD_EXP_PRESS_ACTION = 'adb shell input swipe 500 500 500 500 %s'

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

def runCmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd(), shell=False, startupinfo=globalStartupInfo)
    p.wait()
    re=p.stdout.read().decode()
    return re

def screencap(remote_path, local_path):
    runCmd(CMD_SCREEN_SHOT)
    runCmd(CMD_SAVE_TO_LOCAL%(remote_path, local_path))

def action_press(weight):
    runCmd(CMD_EXP_PRESS_ACTION%weight)