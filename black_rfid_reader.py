from keyboard_alike import reader


class RFIDReader(reader.Reader):
    """
    This class supports common black RFID Readers for 125 kHz read only tokens
    http://www.dx.com/p/intelligent-id-card-usb-reader-174455
    """
    pass

if __name__ == "__main__":
    reader = RFIDReader(0x08ff, 0x0009, 84, 16, should_reset=False)
    reader.initialize()
    print(reader.read().strip())
    reader.disconnect()
