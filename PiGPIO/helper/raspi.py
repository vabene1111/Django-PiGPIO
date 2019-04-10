import RPi.GPIO as GPIO

from PiGPIO.models import Log

DEBUG = False


class ListNotSupportedException(BaseException):
    pass


class UndefinedPinException(BaseException):
    pass


class UnsupportedPinException(BaseException):
    pass


class OutputNotSupportedException(BaseException):
    pass


def set_mode(mode):
    """
    Sets Mode of board (defines pin numbering)
    Board: Pins are numbered by their placement on the board
    BCM: Pins are numbered by their GPIO number
    :param mode: 1 for BCM, all other for Board
    :return:
    """

    if DEBUG:
        log('set mode ' + str(mode))

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

    if type(pin) is list:
        if DEBUG:
            log('set pin array ' + str(pin) + ' to mode ' + str(mode))
        for p in pin:
            setup_pin(p, mode)
        return

    if DEBUG:
        log('set pin ' + str(pin) + ' to mode ' + str(mode))

    if pin is None:
        raise UndefinedPinException()

    if pin < 0:
        raise UnsupportedPinException()

    if mode == 1:
        try:
            GPIO.setup(pin, GPIO.OUT)
        except ValueError:
            raise OutputNotSupportedException(pin)
    else:
        GPIO.setup(pin, GPIO.IN)


def set_output(pin, state):
    """
    Sets output of pin
    :param pin: number of pin according to gpio mode
    :param state: False for low signal and True for high signal
    """
    if type(pin) is list:
        if DEBUG:
            log('set pin array ' + str(pin) + ' to state ' + str(state))
        for p in pin:
            set_output(p, state)
        return

    if DEBUG:
        log('set pin ' + str(pin) + ' to state ' + str(state))

    if pin is None:
        raise UndefinedPinException()

    if pin < 0:
        raise UnsupportedPinException()

    try:
        GPIO.output(pin, state)
    except ValueError:
        raise OutputNotSupportedException(pin)


def get_input(pin):
    """
    Reads the current input value of pin
    :param pin: number of pin according to gpio mode
    """
    setup_pin(pin, 0)

    if DEBUG:
        log('reading ' + str(pin))

    if type(pin) is list:
        raise ListNotSupportedException(pin)

    if pin is None:
        raise UndefinedPinException()

    if pin < 0:
        raise UnsupportedPinException()

    try:
        pin_val = GPIO.input(pin)
        if DEBUG:
            log('read pin ' + str(pin) + ' - value: ' + str(pin_val))
        return pin_val
    except ValueError:
        raise OutputNotSupportedException(pin)


def log(data):
    log_entry = Log()
    log_entry.data = str(data)
    log_entry.save()
