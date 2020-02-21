from keyboard_alike import reader


class RFIDReader(reader.Reader):
    """
    This class supports the Neuftech USB RFID Reader
    https://www.amazon.de/dp/B018OYOR3E
    """
    pass

if __name__ == "__main__":
    reader = RFIDReader(0x16c0, 0x27db, 42, 3, should_reset=False)
    reader.initialize()
    print(reader.read().strip())
    reader.disconnect()
