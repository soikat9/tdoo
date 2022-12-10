# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from glob import glob

from tele.applets.hw_drivers.interface import Interface


class SerialInterface(Interface):
    connection_type = 'serial'

    def get_devices(self):
        serial_devices = {}
        for identifier in glob('/dev/serial/by-path/*'):
            serial_devices[identifier] = {
                'identifier': identifier
            }
        return serial_devices
