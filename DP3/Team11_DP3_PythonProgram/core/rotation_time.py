import math

class RotationTime:
    @staticmethod
    def calculate(slider_distance, gear_diameter, SPR): 
        rotation_time = ((slider_distance / gear_diameter) / (math.pi)) * SPR
        return rotation_time