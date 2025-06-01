import time

from outputs import Motor

from ..core.rotation_time import RotationTime

class RackMotion:
    @staticmethod
    def push_slider(slider_diameter, slider_distance, SPR):
        distance_traveled = 0

        rot_time = RotationTime.calculate(slider_distance, slider_diameter, SPR)
        
        Motor.slider.forward()
        time.sleep(rot_time)
        Motor.slider.stop()

        distance_traveled += slider_distance

        return distance_traveled

    @staticmethod
    def return_slider(distance_traveled, slider_diameter, SPR):
        return_time = RotationTime.calculate(distance_traveled, slider_diameter, SPR)

        Motor.slider.backward()
        time.sleep(return_time)
        Motor.slider.stop()