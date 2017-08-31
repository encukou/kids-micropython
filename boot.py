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

# Pin map
PIN_D0 = 16
PIN_D1 = 5
PIN_D2 = 4
PIN_D3 = PIN_FLASH = 0
PIN_D4 = 2
PIN_D5 = 14
PIN_D6 = 12
PIN_D7 = 13
PIN_D8 = 15

# Number of LEDs on WS2812 strip
STRIP_NUM_LEDS = 8

# Basic colors
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

flash = Pin(PIN_FLASH, Pin.IN)
led = Pin(PIN_D1, Pin.OUT)
btn = Pin(PIN_D5, Pin.IN, Pin.PULL_UP)
strip = NeoPixel(Pin(PIN_D6, Pin.OUT), STRIP_NUM_LEDS)

Pin(PIN_D4, Pin.OUT).value(1)
Pin(PIN_D2, Pin.OUT).value(0)
led.value(0)


if not btn.value():
    # System test
    servo = PWM(Pin(PIN_D8, Pin.OUT), freq=50)
    servo.duty(120)
    for i in range(8):
        strip[i] = CYAN
        strip.write()
        sleep(0.1)
    servo.deinit()

    buzzer = PWM(Pin(PIN_D7, Pin.OUT), duty=512)

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

buzzer = PWM(Pin(PIN_D7, Pin.OUT), duty=0)
servo = PWM(Pin(PIN_D8, Pin.OUT), freq=50, duty=0)
