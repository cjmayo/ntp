Austron 2200A/2201A GPS Receivers
=================================

Synopsis
--------

| Address: 127.127.10.\ *u*
|  Reference ID: ``GPS``
|  Driver ID: ``GPS_AS2201``
|  Serial Port: ``/dev/gpsu``; 9600 baud, 8-bits, no parity
|  Features: ``tty_clk``

Description
-----------

This driver supports the Austron 2200A/2201A GPS/LORAN Synchronized
Clock and Timing Receiver connected via a serial port. It supports
several special features of the clock, including the Input Buffer
Module, Output Buffer Module, IRIG-B Interface Module and LORAN Assist
Module. It requires the RS232 Buffered Serial Interface module for
communication with the driver.

For use with a single computer, the receiver can be connected directly
to the receiver. For use with multiple computers, one of them is
connected directly to the receiver and generates the polling messages.
The other computers just listen to the receiver output directly or
through a buffer amplifier. For computers that just listen,
``fudge flag2`` must be set and the ``ppsclock`` streams module
configured on each of them.

This receiver is capable of a comprehensive and large volume of
statistics and operational data. The specific data collection commands
and attributes are embedded in the driver source code; however, the
collection process can be enabled or disabled using the flag4 flag. If
set, collection is enabled; if not, which is the default, it is
disabled. A comprehensive suite of data reduction and summary scripts is
in the ./scripts/stats directory

of the ntp3 distribution.

Monitor Data
------------

When enabled by the ``flag4`` fudge flag, every received timecode is
written as-is to the ``clockstats`` file.

Fudge Factors
-------------

``time1 time``
    Specifies the time offset calibration factor, in seconds and
    fraction, with default 0.0.
``time2 time``
    Not used by this driver.
``stratum number``
    Specifies the driver stratum, in decimal from 0 to 15, with default
    0.
``refid string``
    Specifies the driver reference identifier, an ASCII string from one
    to four characters, with default ``GPS``.
``flag1 0 | 1``
    Not used by this driver.
``flag2 0 | 1``
    Set for computers that listen-only.
``flag3 0 | 1``
    Not used by this driver.
``flag4 0 | 1``
    Enable verbose ``clockstats`` recording if set.

Additional Information
----------------------

:doc:`Reference Clock Drivers
<../refclock>`
