from outputs import LED

class LEDOutput:
    @staticmethod
    def run(slider_distance, average, sensor_reading):
        if abs(sensor_reading - average) > (0.5 * slider_distance):
            LED.red.on()
            LED_status = "On"
        else:
            LED.red.off()
            LED_status = "Off"

        return LED_status