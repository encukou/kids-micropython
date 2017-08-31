# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
#import webrepl
#webrepl.start()
gc.collect()


from machine import Pin, PWM
from neopixel import NeoPixel
from time import sleep

flash = Pin(0, Pin.IN)                      # D3/FLASH
led = Pin(5, Pin.OUT)                       # D1
btn = Pin(14, Pin.IN, Pin.PULL_UP)                       # D5
strip = NeoPixel(Pin(12, Pin.OUT), 8)       # D6

Pin(2, Pin.OUT).value(1)    # D4/TXD1
Pin(4, Pin.OUT).value(0)    # D2
led.value(0)

BLACK = OFF = 0, 0, 0
WHITE = 10, 10, 10
RED = 10, 0, 0
ORANGE = 10, 5, 0
YELLOW = 10, 10, 0
GREEN = 0, 10, 0
CYAN = 0, 10, 10
BLUE = 0, 0, 10
VIOLET = PURPLE = PINK = 10, 0, 10
GRAY = 5, 5, 5


if not btn.value():
    # System test
    servo = PWM(Pin(15, Pin.OUT), freq=50)      # D8
    servo.duty(120)
    for i in range(8):
        strip[i] = CYAN
        strip.write()
        sleep(0.1)
    servo.deinit()

    buzzer = PWM(Pin(13, Pin.OUT), duty=512)    # D7

    buzzer.freq(440)
    servo.duty(120)
    led.value(1)
    for i in range(8):
        strip[i] = RED
    strip.write()
    sleep(0.1)

    buzzer.freq(550)
    led.value(0)
    for i in range(8):
        strip[i] = GREEN
    strip.write()
    sleep(0.1)

    buzzer.freq(660)
    led.value(1)
    for i in range(8):
        strip[i] = BLUE
    strip.write()
    sleep(0.1)

    buzzer.deinit()

    servo = PWM(Pin(15, Pin.OUT), freq=50)
    servo.duty(40)
    led.value(0)
    for i in range(8):
        strip[i] = WHITE
    strip.write()
    sleep(0.3)

    servo.deinit()


# Reset
led.value(0)
for i in range(8):
    strip[i] = OFF
strip.write()

buzzer = PWM(Pin(13, Pin.OUT), duty=0)
servo = PWM(Pin(15, Pin.OUT), freq=50, duty=0)
