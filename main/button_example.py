"""button test"""

from machine import Pin, PWM
from time import sleep

led = Pin(32, Pin.OUT)
button = Pin(15, Pin.IN)



while True:
  button_state = button.value()
  buzz=PWM(Pin(32), freq=180)
  buzz.duty(512) if button_state==1 else buzz.duty(0)

      
      #led.value(button_state)
    

  #sleep(0.1)
