Forum Graphic GPS Dating station
================================

Synopsis
--------

| Address: 127.127.37.\ *u*
| Reference ID: ``GPS``
| Driver ID: ``GPS``
| Parallel Port: ``/dev/fgclocku``

Description
-----------

This driver supports the Forum Graphic GPS Dating station sold by `EMR
company <http://www.emr.fr/gpsclock.html>`__.

Unfortunately sometime FG GPS start continues reporting of the same
date. The only way to fix this problem is GPS power cycling and ntpd
restart after GPS power-up.

After Jan 10, 2000 my FG GPS unit start send a wrong answer after 10:00am
till 11:00am. It repeat hour value in result string twice. I wroite a
small code to avoid such problem. Unfortunately I have no second FG GPS
unit to evaluate this problem. Please let me know if your GPS has no
problems after Y2K.

Monitor Data
------------

Each timecode is written to the ``clockstats`` file in the format
``YYYY YD HH MI SS``.

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
    to four characters, with default ``FG``.
``flag1 0 | 1``
    Not used by this driver.
``flag2 0 | 1``
    Not used by this driver.
``flag3 0 | 1``
    Not used by this driver.
``flag4 0 | 1``
    Not used by this driver.

Dmitry Smirnov (das@amt.ru)
