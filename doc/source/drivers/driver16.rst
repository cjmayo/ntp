bc635VME/bc350VXI Time and Frequency Processor
==============================================

Synopsis
--------

| Address: 127.127.16.\ *u*
| Reference ID: BTFP
| Driver ID: GPS\_BANCOMM
| Bancomm Device ``/dev/btfp0``
| Requires: Bancomm bc635 TFP device module driver for SunOS 4.x/SunOS 5.x

Description
-----------

This is the clock driver for the Bancomm bc635VME Time and Frequency
Processor. It requires the BANCOMM bc635VME bc350VXI Time and Frequency
Processor Module Driver for SunOS 4.x/SunOS 5.x UNIX Systems.

Most of this code is originally from refclock\_bancomm.c with thanks. It
has been modified and tested on an UltraSparc IIi-cEngine running
Solaris 2.6. A port for HPUX is not available henceforth.

Additional Information
----------------------

:doc:`Reference Clock Drivers <../refclock>`
