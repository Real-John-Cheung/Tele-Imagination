import sensor
import lcd
import image
import time
import KPU as kpu
from Maix import FPIOA, GPIO
from board import board_info

lcd.init()

sensor.reset()

# main
def alternativeCCTV_main():
    # here should be the main function
    # helper functions should be put in separated files and imported as modules
    return 0

# wrapper for displaying error message
def main():
    try:
        alternativeCCTV_main()
    except Exception as err:
        print("Err: ", e)
        import uio
        str = uio.StringIO()
        sys.print_exection(err, str)
        str = s.getvalue()
        img = image.Image()
        img.draw_string(0, 0, str)
        lcd.display(img)

# exec' the main function when boot or reboot
main()
