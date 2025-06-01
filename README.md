# IBEHS_1P10_DP3
This project is a Python-based automation system that uses sensors, motors, and control logic to cut food items to a user-specified size. It operates on a Raspberry Pi and integrates hardware I/O with modular software architecture for control and feedback.

## How It Works
1. User selects cut length using 3 physical buttons.
2. A distance sensor takes multiple readings to calculate average object length.
3. If within range, the slider moves the food by the cut distance.
4. The cutter motor activates to perform a cut.
5. This loop repeats until the slider reaches the maximum distance or the item is removed.

## Hardware Requirements
Raspberry Pi (or compatible GPIO controller)

3 Buttons

1 Distance Sensor (Time of Flight VL530X Distance Sensor)

2 DC Motors (1 for cutter, 1 for slider)

Red LED

## To Run
Connect all hardware to correct GPIO pins (see outputs.py and inputs.py).

Ensure you have all dependencies:
pip install gpiozero

Run the program:
python3 main.py