from inputs import Sensor
from ..core.average import RollingAverage

class Distance:
    @staticmethod
    def get():
        sensor = Sensor()
        reading = sensor.distance()

        return reading