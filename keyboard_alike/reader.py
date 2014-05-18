import usb.core
import usb.util

from keyboard_alike import mapping


class DeviceException(Exception):
    pass


class ReadException(Exception):
    pass


class Reader(object):
    def __init__(self, vendor_id, product_id, data_size, chunk_size, debug=False):
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.data_size = data_size
        self.chunk_size = chunk_size
        self.debug = debug
        self._endpoint = None

    def initialize(self):
        device = usb.core.find(idVendor=self.vendor_id, idProduct=self.product_id)

        if device is None:
            raise DeviceException('No device found, check vendor_id and product_id')

        if device.is_kernel_driver_active(0):
            try:
                device.detach_kernel_driver(0)
            except usb.core.USBError as e:
                raise DeviceException('Could not detach kernel driver: %s' % str(e))

        try:
            device.set_configuration()
        except usb.core.USBError as e:
            raise DeviceException('Could not set configuration: %s' % str(e))

        self._endpoint = device[0][(0, 0)][0]

    def read(self):
        data = []
        data_read = False

        while True:
            try:
                data += self._endpoint.read(self._endpoint.wMaxPacketSize)
                data_read = True
            except usb.core.USBError as e:
                if e.args[0] == 110 and data_read:
                    if len(data) < self.data_size:
                        raise ReadException('Got %s bytes instead of %s' % (len(data), self.data_size))
                    else:
                        break

        if self.debug:
            print('Raw data', data)
        return self.decode_raw_data(data)

    def decode_raw_data(self, raw_data):
        data = self.extract_meaningful_data_from_chunk(raw_data)
        return self.raw_data_to_keys(data)

    def extract_meaningful_data_from_chunk(self, raw_data):
        shift_indicator_index = 0
        raw_key_value_index = 2
        for chunk in self.get_chunked_data(raw_data):
            if len(chunk) == self.chunk_size:
                yield (chunk[shift_indicator_index], chunk[raw_key_value_index])

    def get_chunked_data(self, raw_data):
        return mapping.chunk_data(raw_data, self.chunk_size)

    @staticmethod
    def raw_data_to_keys(extracted_data):
        return ''.join(map(mapping.raw_to_key, extracted_data))
