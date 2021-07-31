from keyboard_alike import reader


class RFIDReader(reader.Reader):
    """
    This class supports the Neuftech USB RFID Reader
    https://www.amazon.de/dp/B018OYOR3E

    Also supports the YARONGTECH USB RFID Card Reader - 125khz Contactless Proximity Sensor Smart ID Card Reader EM4100 (10H)
    The 10H version emits 10 digits in hex.
    https://www.amazon.com/gp/product/B078TK8KYL/

    # lsusb |grep 16c0
    Bus 003 Device 003: ID 16c0:27db Van Ooijen Technische Informatica Keyboard

    # dmesg
    usb 3-1: new low-speed USB device number 3 using ohci-platform
    usb 3-1: New USB device found, idVendor=16c0, idProduct=27db, bcdDevice= 0.01
    usb 3-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
    usb 3-1: Product: HIDKeys
    usb 3-1: Manufacturer: HXGCoLtd
    input: HXGCoLtd HIDKeys Keyboard as /devices/platform/ff5d0000.usb/usb3/3-1/3-1:1.0/0003:16C0:27DB.0003/input/input5
    hid-generic 0003:16C0:27DB.0003: input,hiddev96,hidraw0: USB HID v1.10 Keyboard [HXGCoLtd HIDKeys] on usb-ff5d0000.usb-1/input0
    """
    pass

if __name__ == "__main__":
    reader = RFIDReader(0x16c0, 0x27db, 42, 3, should_reset=False)
    reader.initialize()
    print(reader.read().strip())
    reader.disconnect()
