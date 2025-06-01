import time
from actuators.outputs import Motor  # Make sure this imports the corrected Motor class

class CutMotion:
    @staticmethod
    def run(SPR, ratio):
        cut_SPR = SPR * ratio
        Motor.cutter.forward()
        time.sleep(2 * cut_SPR)  # optional: drop multiplier if not needed
        Motor.cutter.stop()
