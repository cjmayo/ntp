Zyfer GPStarplus Receiver
=========================

Synopsis
--------

| Address: 127.127.42.\ *u*
|  Reference ID: ``GPS``
|  Driver ID: ``Zyfer GPStarplus``
|  Serial Port: ``/dev/zyferu``; 9600 baud, 8-bits, no parity
|  Features: ``(none)``

Description
-----------

This driver supports the `Zyfer GPStarplus <http://www.zyfer.com/>`__
receiver.

The receiver has a DB15 port on the back which has input TxD and RxD
lines for configuration and control, and a separate TxD line for the
once-per-second timestamp.

Additionally, there are BNC connectors on the back for things like PPS
and IRIG output.

Additional Information
----------------------

:doc:`Reference Clock Drivers
<../refclock>`
