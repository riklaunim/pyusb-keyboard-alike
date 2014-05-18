from keyboard_alike import reader


class RFIDReader(reader.Reader):
    """
    This class supports common black RFID Readers for 125 kHz read only tokens
    http://www.dx.com/p/intelligent-id-card-usb-reader-174455
    """
    def extract_meaningful_data_from_chunk(self, raw_data):
        # every good chunk is followed by blank chunk
        chunks = super(RFIDReader, self).extract_meaningful_data_from_chunk(raw_data)
        for index, chunk in enumerate(chunks):
            if index % 2 == 0:
                yield chunk


if __name__ == "__main__":
    reader = RFIDReader(0x08ff, 0x0009, 84, 8, should_reset=False)
    reader.initialize()
    print(reader.read().strip())
    reader.disconnect()
