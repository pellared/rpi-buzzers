#!/usr/bin/python3

import gpiozero
import time

def main():
    led = gpiozero.LED(17) 
    led.on() # light when app is running

    active_buzzer = gpiozero.Buzzer(20)

    button1 = gpiozero.Button(26)
    button2 = gpiozero.Button(19)
    button3 = gpiozero.Button(13)
    button4 = gpiozero.Button(6)
    button5 = gpiozero.Button(5)
    button6 = gpiozero.Button(22)
    button7 = gpiozero.Button(27)

    button1.when_pressed = active_buzzer.toggle
    button2.when_pressed = active_buzzer.on
    button3.when_pressed = active_buzzer.off
    button4.when_pressed = active_buzzer.beep
    button5.when_pressed = lambda: active_buzzer.beep(0.1, 0.1, 1)
    button6.when_pressed = lambda: active_buzzer.beep(0.3, 0.1, 1)

    running = True
    def close():
        nonlocal running
        print("closing...")
        running = False
    button7.when_pressed = close
    
    while running:
        pass

if __name__ == "__main__":
    main()
