pyusb-keyboard-alike
====================

Handler for keyboards and keyboard-alike devices like bar code scanners, RFID readers.

You will find some reusable base classes and few example classes handling data reading from USB bar code scanner and RFID reader that
emulate keyboards.


Requirements
------------
* pyusb 1.X (not 0.4)


How to use
----------
The **keyboard_alike** folder holds a re-usable Reader class. In most case you will be able to use it just by passing correct arguments.

There are device examples:

* lindy_bar_code_scanner.py - Lindy USB bar code scanner
* black_rfid_reader.py - USB 125 kHz RFID reader

If you have matching device - connect it and run the code. Under Linux will have to run the code as root/sudo or give your user permission to access given device.


PyQt4 application example
-------------------------
The **pyqt_example.py** is an example PyQt4 desktop application using the RFID reader. It will add IDs of read tags to the list widget.

The code flow is quite simple:

* On init we connect to the USB reader and start a thread that will end when the USB device returns a result (or exception)
* When thread is finished a signal is emitted that will be handled by *_receive_data* method. It checks if the thread set a return value
and if so it will add it to list. On error it will print it and if it's repeating (device gone wild) it will terminate the application.
In more production-ready applications the exception control should be more strict (like skipping trash-reads exception, but not exceptions preventing operations on the device).
* If all is good *_receive_data* will start the reading thread again allowing the application to work continuously. 


Exceptions
----------
Sometimes pyusb/Reader class will throw exceptions, more often at start when it may read some leftover data (will throw "Got X bytes instead of Y").
Some devices *support* resetting, which seems to prevent any weird reads (Lindy bar code scanner works with reset, while the RFID reader stops working if reset is called).

Lack of permissions will also cause exceptions. The code will have to run as root/sudo or you will have to use udev rules to add permissions for given device.

Sometimes *unknown* exceptions may show up. In many cases retrying to run the code works. In some other the device must be re-connected. Example:

```
keyboard_alike.reader.DeviceException: Could not set configuration: [Errno None] Unknown error
```


Handling new devices
--------------------
If you want to handle your device then at start some experimenting/debugging is required to get to know the device.

* Assuming you are using Linux - connect the device and print **dmesg** (or use **lsusb**) to get the VENDOR and DEVICE id 
* For the code the vendor and device IDs are *0xTHE_VALUE_YOU_GOT* (the 0x at start)
* Next stage is to check the raw output from the device - a list of digits that actually is a set of smaller lists-chunks that we will have to find
* Use debug=True and some data_size/chunk_size - it will print the list with raw data and quite likely it will raise an exception that it didn't got *data_size* of data
* Look on the list and see how many elements is in one chunk. In every chunk the value must be at the same index, like those are 6 element chunks:

```
0, 0, 31, 0, 0, 0,
0, 0, 27, 0, 0, 0
```

* Some raw data examples can be found in the **examples_tests.py**
* Set the correct chunk and data size - now it should work


Pull requests
-------------
You got your device up and running? Provide a basic example with a pull request or send me a link to your blog post :)


More on
-------
You can visit my sites for more tutorials and stuff:

* http://www.rkblog.rk.edu.pl - English
* http://www.python.rk.edu.pl - Polish


Credits
-------
* The code was based on https://github.com/guyzmo/tmsr33-pyusb by Guyzmo Pratz
