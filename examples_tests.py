import unittest

from black_rfid_reader import RFIDReader
from lindy_bar_code_scanner import BarCodeReader


class TestRFIDReader(unittest.TestCase):
    def test_if_raw_message_is_decoded(self):
        reader = RFIDReader(0x08ff, 0x0009, 84, 16, should_reset=False)
        raw_data = [0, 0, 39, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 39, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        result = reader.decode_raw_data(raw_data)
        expected = '0027314141\n'
        self.assertEqual(expected, result)

    def test_if_neuftech_raw_message_is_decoded(self):
        reader = RFIDReader(0x16c0, 0x27db, 42, 3, should_reset=False)
        raw_data = [1, 0, 39, 1, 0, 0, 1, 0, 39, 1, 0, 0, 1, 0, 39, 1, 0, 31, 1, 0, 30, 1, 0, 31, 1, 0, 37, 1, 0, 33, 1, 0, 36, 1, 0, 34, 1, 0, 40, 1, 0, 0]

        result = reader.decode_raw_data(raw_data)
        expected = '0002128475\n'
        self.assertEqual(expected, result)


class TestBarCodeReader(unittest.TestCase):
    def test_if_raw_message_is_decoded(self):
        reader = BarCodeReader(0x03eb, 0x6201, 84, 6, should_reset=True)
        # Luke, Obi-Wan never told you what's in this raw_data...
        raw_data = [0, 0, 34, 0, 0, 0, 0, 0, 38, 0, 0, 0, 0, 0, 39, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 34, 0, 0, 0, 0, 0, 36, 0, 0, 0, 0, 0, 39, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 40, 0, 0, 0]

        result = reader.decode_raw_data(raw_data)
        expected = '5903570132223\n'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
