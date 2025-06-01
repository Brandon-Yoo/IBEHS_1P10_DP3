import time

from .inputs import ButtonSet

class CutLength:
    @staticmethod
    def get():
        cut = 5  # Default cut length accounting for cutter width

        print("Please choose the distance between each cut using the buttons")

        button = ButtonSet()

        while True:
            if button.push1.is_pressed:
                cut += 10
                print("+10mm")
            if button.push2.is_pressed and cut > 15:  # Minimum distance between cuts is 15mm
                cut -= 10
                print("-10mm")
            if button.push3.is_pressed:
                print("Starting")
                break
            time.sleep(0.3)  # Debounce button presses

        return cut