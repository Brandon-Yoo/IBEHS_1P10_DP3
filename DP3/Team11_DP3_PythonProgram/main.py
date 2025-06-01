import time

from core.average import RollingAverage
from core.rotation_time import RotationTime

from hardware.buttons import CutLength
from hardware.distance_sensor import Distance

from actuators.cut_motion import CutMotion
from actuators.led_output import LEDOutput
from actuators.rack_motion import RackMotion

def main():
    # Configuration
    window_average = 2                  # Number of values for rolling average
    slider_diameter = 44               # Gear diameter in mm
    SPR = 5 / 22                        # Seconds per rotation (based on testing)
    cutter_ratio = 5 / 2               # Ratio for cutter gear
    range_dis = [135, 200]             # Valid object placement range
    max_travel = 80                    # Total max distance for slider travel
    travel = 0                         # Track current slider position
    sensor_readings = []

    # Get cut distance from buttons
    cut = CutLength.get()
    print(f"Length between cuts is {cut}mm")
    print("Raw  | Avg   | LED  | Slider | Cutter")

    while True:
        reading = Distance.get()
        sensor_readings.append(reading)

        average = RollingAverage.calculate(sensor_readings, window_average)

        if average is not None:
            led_state = LEDOutput.run(cut, average, reading)

            if reading < range_dis[0] or reading > range_dis[1]:
                push_status = "Off"
                cut_status = "Off"

            elif (travel + cut) >= max_travel:
                travel = 0
                RackMotion.return_slider(
                    distance_traveled=cut,
                    slider_diameter=slider_diameter,
                    SPR=SPR
                )
                push_status = "Rev"
                cut_status = "Off"

            else:
                travel += RackMotion.push_slider(
                    slider_diameter=slider_diameter,
                    slider_distance=cut,
                    SPR=SPR
                )
                time.sleep(1)
                CutMotion.run(SPR, cutter_ratio)  # 🔄 updated here
                time.sleep(1)
                push_status = "Fwd"
                cut_status = "On"

            print(f"{reading:<5} | {average:<6} | {led_state:<4} | {push_status:<6} | {cut_status:<6}")

        time.sleep(0.1)