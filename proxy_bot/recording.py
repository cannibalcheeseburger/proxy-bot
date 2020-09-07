from pynput.keyboard import Key, Controller
import time

#obs must be installed 

keyboard = Controller()


def start_rec():
    print("OBS Recording Started")
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.shift)
    keyboard.press('v')
    time.sleep(1)
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.shift)
    keyboard.release('v')

def stop_rec():
    print("OBS Recording Stopped")    
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.shift)
    keyboard.press('s')
    time.sleep(1)
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.shift)
    keyboard.release('s')

def pause():
    print("OBS Recording Paused")    
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.shift)
    keyboard.press('l')
    time.sleep(1)
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.shift)
    keyboard.release('l')

def resume():
    print("OBS Recording Resumed")
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.shift)
    keyboard.press('u')
    time.sleep(1)
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.shift)
    keyboard.release('u')
