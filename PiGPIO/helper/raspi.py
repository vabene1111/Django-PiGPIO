import RPi.GPIO as GPIO


def set_mode(mode):
    """
    Sets Mode of board (defines pin numbering)
    Board: Pins are numbered by their placement on the board
    BCM: Pins are numbered by their GPIO number
    :param mode: 1 for BCM, all other for Board
    :return:
    """
    if mode == 1:
        GPIO.setmode(GPIO.BCM)
    else:
        GPIO.setmode(GPIO.BOARD)


def setup_pin(pin, mode):
    """
    Sets pin mode
    :param pin: pin to set
    :param mode: 1 for output, all other input
    :return:
    """
    if mode == 1:
        GPIO.setup(pin, GPIO.OUT)
    else:
        GPIO.setup(pin, GPIO.IN)


def set_output(pin, state):
    """
    Sets output of pin
    :param pin: number of pin according to gpio mode
    :param state: False for low signal and True for high signal
    """
    GPIO.output(pin, state)
