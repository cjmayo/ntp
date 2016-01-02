Dumb Clock
==========

Synopsis
--------

| Address: 127.127.33.\ *u*
|  Reference ID: ``DUMBCLOCK``
|  Driver ID: ``DUMBCLOCK``
|  Serial Port: ``/dev/dumbclocku``; 9600 bps, 8-bits, no parity
|  Features: ``(none)``

Description
-----------

This driver supports a dumb ASCII clock that only emits localtime at a
reliable interval. This has no provisions for leap seconds, quality
codes, etc. It assumes output in the local time zone, and that the C
library mktime()/localtime() routines will correctly convert back and
forth between local and UTC.

Most of this code is originally from refclock\_wwvb.c with thanks. It
has been so mangled that wwvb is not a recognizable ancestor.

::

    Timecode format: hh:mm:ssCL
    hh:mm:ss - local time
    C - \r (carriage return)
    L - \n (newline)
