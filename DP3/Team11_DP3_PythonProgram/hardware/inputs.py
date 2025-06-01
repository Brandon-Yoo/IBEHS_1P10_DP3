from gpiozero import Button as GpioButton
from sensor_library import Distance_Sensor

class ButtonSet:
    def __init__(self):
        self.push1 = GpioButton(21)
        self.push2 = GpioButton(20)
        self.push3 = GpioButton(1)

class Sensor:
    def __init__(self):
        self.sensor = Distance_Sensor()

    def distance(self):
        return self.sensor.distance()
