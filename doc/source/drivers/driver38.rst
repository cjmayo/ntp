\ *hopf*\  Serial Line Receivers (6021 and  kompatible)
=======================================================

.. _driver38-synopsis:

Synopsis
--------

| Address:  127.127.38.X
| Reference ID:  .hopf. (default), GPS, DCF
| Driver ID:  HOPF_S
| Serial Port:  /dev/hopfclockX
| Serial I/O:  9600 baud, 8-bits, 1-stop, no parity

|image0|

Description
-----------

The **refclock\_hopf\_serial** driver supports `hopf electronic
receivers <http://www.hopf.com>`__ with serial Interface kompatibel
6021.

Additional software and information about the software drivers is
available from: http://www.ATLSoft.de/ntp.

Latest NTP driver source, executables and documentation is maintained
at: http://www.ATLSoft.de/ntp

Operating System Compatibility
------------------------------

The hopf clock driver has been tested on the following software and
hardware platforms:

+--------------------------------------+--------------------------------------+
| **Platform**                         | **Operating System**                 |
+--------------------------------------+--------------------------------------+
| i386 (PC)                            | Linux                                |
+--------------------------------------+--------------------------------------+
| i386 (PC)                            | Windows NT                           |
+--------------------------------------+--------------------------------------+
| i386 (PC)                            | Windows 2000                         |
+--------------------------------------+--------------------------------------+

O/S Serial Port Configuration
-----------------------------

The driver attempts to open the device
:ref:`/dev/hopfclock\<X\> <driver38-synopsis>` where <X> is the NTP
refclock unit number as defined by the LSB of the refclock address. 
Valid refclock unit numbers are 0 - 3.

The user is expected to provide a symbolic link to an available serial
port device.  This is typically performed by a command such as:

    ``ln -s /dev/ttyS0 /dev/hopfclock0``

Windows NT does not support symbolic links to device files. 
**COMx**: is used by the driver, based on the refclock unit number,
where **unit 1** corresponds to **COM1**: and **unit 3** corresponds
to **COM3**:

Fudge Factors
-------------

``time1 <time>``
    Specifies the time offset calibration factor, in seconds and
    fraction, with default 0.0. Should be set to 20 milliseconds to
    correct serial line and operating system delays incurred in
    capturing time stamps from the synchronous packets.
:ref:`refid \<string\> <driver38-synopsis>`
    Specifies the driver reference identifier, **GPS** *or* **DCF**.
``flag1 0 | 1``
    When set to 1, driver sync's even if only crystal driven.

.. _driver38-DataFormat:

Data Format
---------------------------------------------

as specified in clock manual under pt. [ **Data String for NTP** (
***Network Time Protocol*** ) ]

Questions or Comments:
~~~~~~~~~~~~~~~~~~~~~~

`Bernd Altmeier <mailto:altmeier@atlsoft.de>`__
Ing.-Büro für Software `www.ATLSoft.de <http://www.ATLSoft.de>`__

.. |image0| image:: ../pic/fg6021.png
