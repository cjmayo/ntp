PSTI/Traconex 1020 WWV/WWVH Receiver
====================================

Synopsis
--------

| Address: 127.127.3.\ *u*
| Reference ID: ``WWV``
| Driver ID: ``WWV_PST``
| Serial Port: ``/dev/wwvu``; 9600 baud, 8-bits, no parity
| Features: ``tty_clk``

Description
-----------

This driver supports the PSTI 1010 and Traconex 1020 WWV/WWVH Receivers.
No specific claim of accuracy is made for these receiver, but actual
experience suggests that 10 ms would be a conservative assumption.

The dipswitches should be set for 9600 bps line speed, 24-hour
day-of-year format and UTC time zone. Automatic correction for DST
should be disabled. It is very important that the year be set correctly
in the DIP-switches; otherwise, the day of year will be incorrect after
28 April of a normal or leap year. As the there are only four
dipswitches to set the year and the base value of zero correspondes to
1986, years beyond 2001 recycle with the value of zero corresponding to
2002. The propagation delay DIP-switches should be set according to the
distance from the transmitter for both WWV and WWVH, as described in the
instructions. While the delay can be set only to within 11 ms, the fudge
time1 parameter can be used for vernier corrections.

Using the poll sequence ``QTQDQM``, the response timecode is in three
sections totalling 50 ASCII printing characters, as concatenated by the
driver, in the following format:

::

    ahh:mm:ss.fffs<cr> yy/dd/mm/ddd<cr>
    frdzycchhSSFTttttuuxx<cr>

    on-time = first <cr>
    hh:mm:ss.fff = hours, minutes, seconds, milliseconds
    a = AM/PM indicator (' ' for 24-hour mode)
    yy = year (from DIPswitches)
    dd/mm/ddd = day of month, month, day of year
    s = daylight-saving indicator (' ' for 24-hour mode)
    f = frequency enable (O = all frequencies enabled)
    r = baud rate (3 = 1200, 6 = 9600)
    d = features indicator (@ = month/day display enabled)
    z = time zone (0 = UTC)
    y = year (5 = 91)
    cc = WWV propagation delay (52 = 22 ms)
    hh = WWVH propagation delay (81 = 33 ms)
    SS = status (80 or 82 = operating correctly)
    F = current receive frequency (4 = 15 MHz)
    T = transmitter (C = WWV, H = WWVH)
    tttt = time since last update (0000 = minutes)
    uu = flush character (03 = ^c)
    xx = 94 (unknown)

The alarm condition is indicated by other than ``8`` at ``a``, which
occurs during initial synchronization and when received signal is lost
for an extended period; unlock condition is indicated by other than
``0000`` in the ``tttt`` subfield.

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
    to four characters, with default ``WWV``.
``flag1 0 | 1``
    Not used by this driver.
``flag2 0 | 1``
    Not used by this driver.
``flag3 0 | 1``
    Not used by this driver.
``flag4 0 | 1``
    Not used by this driver.

Additional Information
----------------------

:doc:`Reference Clock Drivers <../refclock>`
