from machine import Pin, I2C
import time
import binascii

class ds3231(object):
    address = 0x68
    start_reg = 0x00
    alarm1_reg = 0x07
    control_reg = 0x0e
    status_reg = 0x0f

    def __init__(self, i2c_port = 0, i2c_scl = 21, i2c_sda = 20):
        try:
            self.bus = I2C(i2c_port, scl=Pin(i2c_scl), sda=Pin(i2c_sda))
            self.bus.readfrom_mem(int(self.address), int(self.start_reg), 7)
        except OSError:
            # Fall back to i2c port 1 (pins 6,7) used by earlier, but still common, versions of the Waveshare RTC module
            self.bus = I2C(1, scl=Pin(7), sda=Pin(6))
            self.bus.readfrom_mem(int(self.address), int(self.start_reg), 7)

    def set_time(self, new_time):
        ti = time.localtime(new_time)
        hour = "%02d" % ti[3]
        minute = "%02d" % ti[4]
        second = "%02d" % ti[5]
        week = "%02d" % (ti[6] + 1)
        year = str(ti[0])[2:4]
        month = "%02d" % ti[1]
        day = "%02d" % ti[2]
        now_time = binascii.unhexlify(
            (second + " " + minute + " " + hour + " " + week + " " + day + " " + month + " " + year).replace(' ', ''))
        self.bus.writeto_mem(int(self.address), int(self.start_reg), now_time)

    def read_time(self):
        t = self.bus.readfrom_mem(int(self.address), int(self.start_reg), 7)
        second = int("%02x" % (t[0] & 0x7F))
        minute = int("%02x" % (t[1] & 0x7F))
        hour = int("%02x" % (t[2] & 0x3F))
        # week = (t[3] & 0x07) - 1
        day = int("%02x" % (t[4] & 0x3F))
        month = int("%02x" % (t[5] & 0x1F))
        year = int("20%x" % t[6])
        return time.mktime((year, month, day, hour, minute, second, 0, 0))