Conrad parallel port radio clock
================================

Synopsis
--------

| Address: 127.127.35.\ *u*
|  Reference ID: ``PCF``
|  Driver ID: ``PCF``
|  Parallel Port: ``/dev/pcfclocks/u`` or ``/dev/pcfclocku``

Description
-----------

This driver supports the parallel port radio clock sold by `Conrad
Electronic <http://www.conrad-electronic.com/>`__ under order numbers
967602 and 642002. This clock is put between a parallel port and your
printer. It receives the legal German time, which is either CET or CEST,
from the DCF77 transmitter and uses it to set its internal quartz clock.
The DCF77 transmitter is located near to Frankfurt/Main and covers a
radius of more than 1500 kilometers.

The pcfclock device driver is required in order to use this reference
clock driver. Currently device drivers for
`Linux <http://home.pages.de/%7evoegele/pcf.html>`__ and
`FreeBSD <http://schumann.cx/pcfclock/>`__ are available.

This driver uses C library functions to convert the received timecode to
UTC and thus requires that the local timezone be CET or CEST. If your
server is not located in Central Europe you have to set the environment
variable TZ to CET before starting ``ntpd``.

Monitor Data
------------

Each timecode is written to the ``clockstats`` file in the format
``YYYY MM DD HH MI SS``.

Fudge Factors
-------------

``time1 time``
    Specifies the time offset calibration factor, in seconds and
    fraction, with default 0.1725.
``time2 time``
    Not used by this driver.
``stratum number``
    Specifies the driver stratum, in decimal from 0 to 15, with default
    0.
``refid string``
    Specifies the driver reference identifier, an ASCII string from one
    to four characters, with default ``PCF``.
``flag1 0 | 1``
    Not used by this driver.
``flag2 0 | 1``
    If set to 1, the radio clock's synchronisation status bit is
    ignored, ie the timecode is used without a check.
``flag3 0 | 1``
    Not used by this driver.
``flag4 0 | 1``
    Not used by this driver.
