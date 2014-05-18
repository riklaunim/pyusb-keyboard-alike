from keyboard_alike import reader


class BarCodeReader(reader.Reader):
    """
    This class supports Lindy USB bar code scanner configured to work as a keyboard
    http://www.lindy.co.uk/accessories-c9/input-devices-c357/barcode-scanners-c360/barcode-scanner-ccd-usb-p1352
    """
    pass


if __name__ == "__main__":
    reader = BarCodeReader(0x03eb, 0x6201, 84, 6, should_reset=True)
    reader.initialize()
    print(reader.read().strip())
    reader.disconnect()
