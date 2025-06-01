from gpiozero import Motor as GpioMotor, LED as GpioLED

class Motor:
    slider = GpioMotor(forward=16, backward=12)
    cutter = GpioMotor(forward=8, backward=7)

class LED:
    red = GpioLED(6)
