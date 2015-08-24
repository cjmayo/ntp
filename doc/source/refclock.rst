Reference Clock Support
=======================

NTP Version 4 supports almost four dozen satellite, radio and telephone
modem reference clocks plus several audio devices for instrumentation
signals. A general description of the reference clock support is on this
page. Additional information about each reference clock driver can be
found via links from this page. Additional information is on the
:doc:`Debugging Hints for Reference Clock
Drivers <rdebug>` and
:doc:`How To Write a Reference Clock Driver
<howto>` pages. Information on how to support
pulse-per-second (PPS) signals produced by some devices is on the
:doc:`Pulse-per-second (PPS) Signal Interfacing
<pps>` page. All reference clock drivers
require that the reference clock use only Coordinated Universal Time
(UTC). Timezone and standard/daylight adjustments are performed by the
operating system kernel.

A reference clock will generally (though not always) be a radio timecode
receiver synchronized to standard time as provided by NIST and USNO in
the US, NRC in Canada and their counterparts elsewhere in the world. A
device driver specific to each reference clock must be compiled in the
distribution; however, most common radio, satellite and telephone modem
clocks are included by default and are activated by configuration
commands.

Reference clocks are supported in the same way as ordinary NTP clients
and use the same filter, select, cluster and combine algorithms. Drivers
have addresses in the form 127.127.\ *t.u*, where *t* is the driver type
and *u* is a unit number in the range 0-3 to distinguish multiple
instances of the same driver. The connection to the computer is device
dependent, usually a serial port, parallel port or special bus
peripheral, but some can work directly from an audio codec or sound
card. The particular device is specified by adding a soft link from the
name used by the driver to the particular device name.

The ``server`` command is used to configure a reference clock. Only the
``mode``, ``minpoll``, ``maxpoll``, and ``prefer`` options are supported
for reference clocks, as described on the
:doc:`Reference Clock Commands
<clockopt>` page. The ``prefer`` option is
discussed on the :doc:`Mitigation Rules and the
prefer Keyword <prefer>` page. Some of these
options have meaning only for selected clock drivers.

The ``fudge`` command can be used to provide additional information for
individual drivers and normally follows immediately after the ``server``
command. The reference clock stratum is by default 0, so that the server
stratum appears to clients as 1. The ``stratum`` option can be used to
set the stratum to any value in the range 0 through 15. The ``refid``
option can be used to change the reference identifier, as might in the
case when the driver is disciplined by a pulse-per-second (PPS) source.
The device-dependent ``mode``, ``time`` and ``flag`` options can provide
additional driver customization.

.. _refclock-spec:

Special Considerations
--------------------------------------------------

The :doc:`Audio Drivers
<audio>` page describes three software drivers
that process audio signals from an audio codec or sound card. One is for
the NIST time and frequency stations WWV and WWVH, another for the
Canadian time and frequency station CHU. These require an external
shortwave radio and antenna. A third is for the generic IRIG signal
produced by some timing devices. Currently, these are supported in
FreeBSD, Solaris and SunOS and likely in other system as well.

The :doc:`Undisciplined Local Clock
<drivers/driver1>` driver can simulate a
reference clock when no external synchronization sources are available.
If a server with this driver is connected directly or indirectly to the
public Internet, there is some danger that it can destabilize other
clients. It is not recommended that the local clock driver be used in
this way, as the orphan mode described on the
:doc:`Association Management
<assoc>` page provides a generic backup
capability.

The local clock driver can also be used when an external synchronization
source such as the IEEE 1588 Precision Time Protocol or NIST Lockclock
directly synchronizes the computer time. Further information is on the
:doc:`External Clock Discipline and the Local
Clock Driver <extern>` page.

Several drivers make use of the pulse-per-second (PPS) signal
discipline, which is part of the generic driver interface, so require no
specific configuration. For those drivers that do not use this
interface, the :doc:`PPS Clock Discipline
<drivers/driver22>` driver can be can provide
this function. It normally works in conjunction with the reference clock
that produces the timecode signal, but can work with another driver or
remote server. When PPS kernel features are present, the driver can
redirect the PPS signal to the kernel.

Some drivers depending on longwave or shortwave radio services need to
know the radio propagation time from the transmitter to the receiver.
This must be calculated for each specific receiver location and requires
the geographic coordinates of both the transmitter and receiver. The
transmitter coordinates for various radio services are given in the
`Time and Frequency Standard Station
Information <http://www.eecis.udel.edu/%7emills/ntp/qth.html>`__ page.
Receiver coordinates can be obtained locally or from Google Earth. The
actual calculations are beyond the scope of this document.

Depending on interface type, port speed, etc., a reference clock can
have a small residual offset relative to another. To reduce the effects
of jitter when switching from one driver to the another, it is useful to
calibrate the drivers to a common ensemble offset. The
``enable calibrate`` configuration command described on the
:doc:`Miscellaneous Options
<miscopt>` page activates a special feature
which automatically calculates a correction factor for each driver
relative to an association designated the prefer peer.

.. _refclock-list:

List of Reference Clock Drivers
-----------------------------------------------------------

Following is a list showing the type and title of each driver currently
implemented. The compile-time identifier for each is shown in
parentheses. Click on a selected type for specific description and
configuration documentation, including the clock address, reference ID,
driver ID, device name and serial line speed. For those drivers without
specific documentation, please contact the author listed in the
:doc:`Copyright Notice
<copyright>` page.

-  :doc:`Type 1
   <drivers/driver1>` Undisciplined Local Clock
   (``LOCAL``)
-  Type 2 Deprecated: was Trak 8820 GPS Receiver
-  :doc:`Type 3
   <drivers/driver3>` PSTI/Traconex 1020
   WWV/WWVH Receiver (``WWV_PST``)
-  :doc:`Type 4
   <drivers/driver4>` Spectracom WWVB/GPS
   Receivers (``WWVB_SPEC``)
-  :doc:`Type 5
   <drivers/driver5>` TrueTime GPS/GOES/OMEGA
   Receivers (``TRUETIME``)
-  :doc:`Type 6
   <drivers/driver6>` IRIG Audio Decoder
   (``IRIG_AUDIO``)
-  :doc:`Type 7
   <drivers/driver7>` Radio CHU Audio
   Demodulator/Decoder (``CHU``)
-  :doc:`Type 8
   <drivers/driver8>` Generic Reference Driver
   (``PARSE``)
-  :doc:`Type 9
   <drivers/driver9>` Magnavox MX4200 GPS
   Receiver (``GPS_MX4200``)
-  :doc:`Type 10
   <drivers/driver10>` Austron 2200A/2201A GPS
   Receivers (``GPS_AS2201``)
-  :doc:`Type 11
   <drivers/driver11>` Arbiter 1088A/B GPS
   Receiver (``GPS_ARBITER``)
-  :doc:`Type 12
   <drivers/driver12>` KSI/Odetics TPRO/S IRIG
   Interface (``IRIG_TPRO``)
-  Type 13 Leitch CSD 5300 Master Clock Controller (``ATOM_LEITCH``)
-  Type 14 EES M201 MSF Receiver (``MSF_EES``)
-  Type 15 reserved
-  :doc:`Type 16
   <drivers/driver16>` Bancomm GPS/IRIG
   Receiver (``GPS_BANCOMM``)
-  Type 17 Datum Precision Time System (``GPS_DATUM``)
-  :doc:`Type 18
   <drivers/driver18>` NIST/USNO/PTB Modem Time
   Services (``ACTS_MODEM``)
-  :doc:`Type 19
   <drivers/driver19>` Heath WWV/WWVH Receiver
   (``WWV_HEATH``)
-  :doc:`Type 20
   <drivers/driver20>` Generic NMEA GPS
   Receiver (``NMEA``)
-  Type 21 TrueTime GPS-VME Interface (``GPS_VME``)
-  :doc:`Type 22
   <drivers/driver22>` PPS Clock Discipline
   (``PPS``)
-  Type 23 reserved
-  Type 24 reserved
-  Type 25 reserved
-  :doc:`Type 26
   <drivers/driver26>` Hewlett Packard 58503A
   GPS Receiver (``GPS_HP``)
-  :doc:`Type 27
   <drivers/driver27>` Arcron MSF Receiver
   (``MSF_ARCRON``)
-  :doc:`Type 28
   <drivers/driver28>` Shared Memory Driver
   (``SHM``)
-  :doc:`Type 29
   <drivers/driver29>` Trimble Navigation
   Palisade GPS (``GPS_PALISADE``)
-  :doc:`Type 30
   <drivers/driver30>` Motorola UT Oncore GPS
   ``GPS_ONCORE``)
-  :doc:`Type 31
   <drivers/driver31>` Rockwell Jupiter GPS
   (``GPS_JUPITER``)
-  :doc:`Type 32
   <drivers/driver32>` Chrono-log K-series WWVB
   receiver (``CHRONOLOG``)
-  :doc:`Type 33
   <drivers/driver33>` Dumb Clock
   (``DUMBCLOCK``)
-  :doc:`Type 34
   <drivers/driver34>` Ultralink WWVB Receivers
   (``ULINK``)
-  :doc:`Type 35
   <drivers/driver35>` Conrad Parallel Port
   Radio Clock (``PCF``)
-  :doc:`Type 36
   <drivers/driver36>` Radio WWV/H Audio
   Demodulator/Decoder (``WWV``)
-  :doc:`Type 37
   <drivers/driver37>` Forum Graphic GPS Dating
   station (``FG``)
-  :doc:`Type 38
   <drivers/driver38>` hopf GPS/DCF77 6021/komp
   for Serial Line (``HOPF_S``)
-  :doc:`Type 39
   <drivers/driver39>` hopf GPS/DCF77 6039 for
   PCI-Bus (``HOPF_P``)
-  :doc:`Type 40
   <drivers/driver40>` JJY Receivers (``JJY``)
-  Type 41 TrueTime 560 IRIG-B Decoder
-  :doc:`Type 42
   <drivers/driver42>` Zyfer GPStarplus
   Receiver
-  :doc:`Type 43
   <drivers/driver43>` RIPE NCC interface for
   Trimble Palisade
-  :doc:`Type 44
   <drivers/driver44>` NeoClock4X - DCF77 / TDF
   serial line
-  :doc:`Type 45
   <drivers/driver45>` Spectracom TSYNC PCI
-  :doc:`Type 46
   <drivers/driver46>` GPSD NG client protocol
