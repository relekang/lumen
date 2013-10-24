# -*- coding: utf-8 -*-
SERIALPORT = "/dev/tty.usbmodemfa121"


try:
    from local import *
except ImportError:
    print "Found no local settings"
