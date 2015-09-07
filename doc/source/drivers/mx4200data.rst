MX4200 Receiver Data Format
===========================

.. _mx4200data-control:

Control Port Sentences
-----------------------------------------------------

The Control (CDU) Port is used to initialize, monitor, and control the
receiver. The structure of the control port sentences is based on the
NMEA-0183 Standard for Interfacing Marine Electronics Navigation Devices
(version 1.5). For more details, please refer to the NMEA-0183
Specification available from the `National Marine Electronics
Association <http://www.nmea.org/>`__.

Reserved characters are used to indicate the beginning and the end of
records in the data stream, and to delimit data fields within a
sentence. Only printable ASCII characters (Hex 20 through 7F) may be
used in a sentence. :ref:`Table 2 <mx4200data-table\_2>` lists the reserved
characters and defines their usage. :ref:`Table 1 <mx4200data-table\_1>`
illustrates the general Magnavox proprietary NMEA sentence format.

.. _mx4200data-table_1:

Table 1. Magnavox Proprietary NMEA Sentence Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``$PMVXG,XXX,...................*CK``

+-------------+-------------------------------------+
| Character   | Meaning                             |
+=============+=====================================+
| ``$``       | Sentence Start Character            |
+-------------+-------------------------------------+
| ``P``       | Special ID (P = Proprietary)        |
+-------------+-------------------------------------+
| ``MVX``     | Originator ID (MVX = Magnavox)      |
+-------------+-------------------------------------+
| ``G``       | Interface ID (G = GPS)              |
+-------------+-------------------------------------+
| ``XXX``     | Sentence Type                       |
+-------------+-------------------------------------+
| ``...``     | Data                                |
+-------------+-------------------------------------+
| ``*``       | Optional Checksum Field Delimiter   |
+-------------+-------------------------------------+
| ``CK``      | Optional Checksum                   |
+-------------+-------------------------------------+

.. _mx4200data-table_2:

Table 2. NMEA Sentence Reserved Characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------+-------------+-------------------------------------+
| Character      | Hex Value   | Usage                               |
+================+=============+=====================================+
| ``$``          | 24          | Start of Sentence Identifier        |
+----------------+-------------+-------------------------------------+
| ``{cr}{lf}``   | 0D 0A       | End of Sentence Identifier          |
+----------------+-------------+-------------------------------------+
| ``,``          | 2C          | Sentence Delimiter                  |
+----------------+-------------+-------------------------------------+
| ``*``          | 2A          | Optional Checksum Field Delimiter   |
+----------------+-------------+-------------------------------------+

Following the start character ``$``, are five characters which
constitute the block label of the sentence. For Magnavox proprietary
sentences, this label is always ``PMVXG``. The next field after the
block label is the sentence type, consisting of three decimal digits.

The data, delimited by commas, follows the sentence type. Note that the
receiver uses a free-format parsing algorithm, so you need not send the
exact number of characters shown in the examples. You will need to use
the commas to determine how many bytes of data need to be retrieved.

The notation ``CK`` shown in :ref:`Table 1 <mx4200data-table\_1>`
symbolically indicates
the optional checksum in the examples. The checksum is computed by
exclusive-ORing all of the bytes between the ``$`` and the ``*``
characters. The ``$``, ``*`` and the checksum are not included in the
checksum computation.

Checksums are optional for Control Port input sentences, but are highly
recommended to limit the effects of communication errors. Magnavox
receivers always generate checksums for Control Port output sentences.

ASCII data characters are transmitted in the following format:

+-------------+--------------------+
| Data Bits   | 8 (msb always 0)   |
+-------------+--------------------+
| Parity      | None               |
+-------------+--------------------+
| Stop Bits   | 1                  |
+-------------+--------------------+

NULL fields are fields which do not contain any data. They would appear
as two commas together in the sentence format, except for the final
field. Some Magnavox proprietary sentences require that the format
contain NULL fields. mandatory NULL fields are identified by an '\*'
next to the respective field.

.. _mx4200data-input:

Control Port Input Sentences
---------------------------------------------------------

These are the subset of the MX4200 control port input sentences sent by
the NTP driver to the GPS receiver.

.. _mx4200data-input\_000:

$PMVXG,000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initialization/Mode Control - Part A
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Initializes the time, position and antenna height of the MX4200.

+--------------+--------------+--------------+--------------+--------------+--------------+
| Field        | Description  | Units        | Format       | Default      | Range        |
+==============+==============+==============+==============+==============+==============+
| 1            | Day          |              | Int          |              | 1-31         |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 2            | Month        |              | Int          |              | 1-12         |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 3            | Year         |              | Int          |              | 1991-9999    |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 4            | GMT Time     | HHMMSS       | Int          |              | 000000-23595 |
|              |              |              |              |              | 9            |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 5            | WGS-84       | DDMM.MMMM    | Float        | 0.0          | 0 -          |
|              | Latitude     |              |              |              | 8959.9999    |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 6            | North/South  |              | Char         | N            | N,S          |
|              | Indicator    |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 7            | WGS-84       | DDDMM.MMMM   | Float        | 0.0          | 0 -          |
|              | Longitude    |              |              |              | 17959.9999   |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 8            | East/West    |              | Char         | E            | E,W          |
|              | Indicator    |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 9            | Altitude     | Meters       | Float        | 0.0          | +/-99999.0   |
|              | (height      |              |              |              |              |
|              | above Mean   |              |              |              |              |
|              | Sea Level)   |              |              |              |              |
|              | in meters    |              |              |              |              |
|              | (WGS-84)     |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 10           | Not Used     |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+

Example:

``$PMVXG,000,,,,,,,,,,*48``

``$PMVXG,000,,,,,5128.4651,N,00020.0715,W,58.04,*4F``

.. _mx4200data-input\_001:

$PMVXG,001
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initialization/Mode Control - Part B
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Specifies various navigation parameters: Altitude aiding, acceleration
DOP limits, and satellite elevation limits.

+--------------+--------------+--------------+--------------+--------------+--------------+
| Field        | Description  | Units        | Format       | Default      | Range        |
+==============+==============+==============+==============+==============+==============+
| \*1          | Constrain    |              | Int          | 1            | 0=3D Only    |
|              | Altitude     |              |              |              | 1=Auto       |
|              |              |              |              |              | 2=2D Only    |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 2            | Not Used     |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| \*3          | Horizontal   | m/sec^2      | Float        | 1.0          | 0.5-10.0     |
|              | Acceleration |              |              |              |              |
|              | Factor       |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| \*4          | Not Used     |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| \*5          | VDOP Limit   |              | Int          | 10           | 1-9999       |
+--------------+--------------+--------------+--------------+--------------+--------------+
| \*6          | HDOP Limit   |              | Int          | 10           | 1-9999       |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 7            | Elevation    | Deg          | Int          | 5            | 0-90         |
|              | Limit        |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 8            | Time Output  |              | Char         | U            | U=UTC        |
|              | Mode         |              |              |              | L=Local Time |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 9            | Local Time   | HHMM         | Int          | 0            | +/- 0-2359   |
|              | Offset       |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+

Example:

``$PMVXG,001,3,,0.1,0.1,10,10,5,U,0*06``

.. _mx4200data-input\_007:

$PMVXG,007
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Control Port Output Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This message enables or disables output of the specified sentence and
defines the output rate. The user sends this message for each sentence
that the receiver is to output.

+--------------+--------------+--------------+--------------+--------------+--------------+
| Field        | Description  | Units        | Format       | Default      | Range        |
+==============+==============+==============+==============+==============+==============+
| 1            | Control Port |              | Char         |              |              |
|              | Output Block |              |              |              |              |
|              | Label        |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 2            | Clear        |              | Int          |              | 0=No         |
|              | Current      |              |              |              | 1=Yes        |
|              | Output List  |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 3            | Add/Delete   |              | Int          |              | 1=Append     |
|              | Sentence     |              |              |              | 2=Delete     |
|              | from List    |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 4            | Not Used     |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 5            | Sentence     | Sec          | Int          |              | 1-9999       |
|              | Output Rate  |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 6            | # digits of  |              | Int          | 2            | 2-4          |
|              | Precision    |              |              |              |              |
|              | for CGA and  |              |              |              |              |
|              | GLL          |              |              |              |              |
|              | sentences    |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 7            | Not Used     |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 8            | Not Used     |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+

Example:

``$PMVXG,007,022,0,1,,1,,,*4F``

.. _mx4200data-input\_023:

$PMVXG,023
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Time Recovery Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This message is used to enable/disable the time recovery feature of the
receiver. The time synchronization for the 1PPS output is specified in
addition to a user time bias and an error tolerance for a valid pulse.
This record is accepted in units configured for time recovery. If the
back panel contains a 1PPS outlet, the receiver is a time recovery unit.

+--------------+--------------+--------------+--------------+--------------+--------------+
| Field        | Description  | Units        | Format       | Default      | Range        |
+==============+==============+==============+==============+==============+==============+
| \*1          | Time         |              | Char         | D            | D=Dynamic    |
|              | Recovery     |              |              |              | S=Static     |
|              | Mode         |              |              |              | K=Known      |
|              |              |              |              |              | Position     |
|              |              |              |              |              | N=No Time    |
|              |              |              |              |              | Recovery     |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 2            | Time         |              | Char         | G            | U=UTC        |
|              | Synchronizat |              |              |              | G=GPS        |
|              | ion          |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 3            | Time Mark    |              | Char         | A            | A=Always     |
|              | Mode         |              |              |              | V=Valid      |
|              |              |              |              |              | Pulses Only  |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 4            | Maximum Time | Nsec         | Int          | 100          | 50-1000      |
|              | Error        |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 5            | User Time    | Nsec         | Int          | 0            | +/- 99999    |
|              | Bias         |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 6            | ASCII Time   |              | Int          | 0            | 0=No Output  |
|              | Message      |              |              |              | 1=830 to     |
|              | Control      |              |              |              | Control Port |
|              |              |              |              |              | 2=830 to     |
|              |              |              |              |              | Equipment    |
|              |              |              |              |              | Port         |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 7            | Known Pos    |              | Int          | 0            | 1-32         |
|              | PRN          |              |              |              | 0=Track All  |
|              |              |              |              |              | Sats         |
+--------------+--------------+--------------+--------------+--------------+--------------+

Example:

``$PMVXG,023,S,U,A,500,0,1,*16``

.. _mx4200data-input\_gpq:

$CDGPQ,YYY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Query From a Remote Device / Request to Output a Sentence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enables the controller to request a one-time transmission of a specific
block label. To output messages at a periodic rate, refer to input
sentence :ref:`$PMVXG,007
<mx4200data-input\_007>`.

+--------------+--------------+--------------+--------------+--------------+--------------+
| Field        | Description  | Units        | Format       | Default      | Range        |
+==============+==============+==============+==============+==============+==============+
| 1:CD         | ID of Remote |              | Char         |              | (See         |
|              | Device       |              |              |              | NMEA-0183)   |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 2:GP         | GPS          |              | Char         |              | (See         |
|              |              |              |              |              | NMEA-0183)   |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 3:Q          | Query        |              | Char         |              | (See         |
|              |              |              |              |              | NMEA-0183)   |
+--------------+--------------+--------------+--------------+--------------+--------------+
| 4:YYY        | Label of     |              | Char         |              | Any Valid    |
|              | Desired      |              |              |              | NMEA or      |
|              | Sentence     |              |              |              | Magnavox     |
|              |              |              |              |              | Sentence     |
|              |              |              |              |              | Type         |
+--------------+--------------+--------------+--------------+--------------+--------------+

Example:

``$CDGPQ,030*5E``

.. _mx4200data-output:

Control Port Output Sentences
-----------------------------------------------------------

These are the subset of the MX4200 control port output sentences
recognized by the NTP driver.

.. _mx4200data-output\_000:

$PMVXG,000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Receiver Status
^^^^^^^^^^^^^^^

Returns the current status of the receiver including the operating mode,
number of satellites visible, and the number of satellites being
tracked.

+----------------+----------------+----------------+----------------+----------------+
| Field          | Description    | Units          | Format         | Range          |
+================+================+================+================+================+
| 1              | Current        |                | Char           | ACQ=Reacquisit |
|                | Receiver       |                |                | ion            |
|                | Status         |                |                |                |
|                |                |                |                | ALT=Constellat |
|                |                |                |                | ion            |
|                |                |                |                | Selection      |
|                |                |                |                | IAC=Initial    |
|                |                |                |                | Acquisition    |
|                |                |                |                | IDL=Idle, No   |
|                |                |                |                | Satellites     |
|                |                |                |                |                |
|                |                |                |                | NAV=Navigating |
|                |                |                |                | STS=Search     |
|                |                |                |                | The Sky        |
|                |                |                |                | TRK=Tracking   |
+----------------+----------------+----------------+----------------+----------------+
| 2              | Number of      |                | Int            | 0-12           |
|                | Satellites     |                |                |                |
|                | that should be |                |                |                |
|                | Visible        |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 3              | Number of      |                | Int            | 0-12           |
|                | Satellites     |                |                |                |
|                | being Tracked  |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 4              | Time since     | HHMM           | Int            | 0-2359         |
|                | Last           |                |                |                |
|                | Navigation     |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 5              | Initialization |                | Int            | 0=Waiting for  |
|                | Status         |                |                | Initialization |
|                |                |                |                |                |
|                |                |                |                | 1=Initializati |
|                |                |                |                | on             |
|                |                |                |                | Complete       |
+----------------+----------------+----------------+----------------+----------------+

Example:

``$PMVXG,000,TRK,3,3,0122,1*19``

.. _mx4200data-output\_021:

$PMVXG,021
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Position, Height, Velocity
^^^^^^^^^^^^^^^^^^^^^^^^^^

This sentence gives the receiver position, height, navigation mode and
velocity north/east. *This sentence is intended for post analysis
applications.*

+----------------+----------------+----------------+----------------+----------------+
| Field          | Description    | Units          | Format         | Range          |
+================+================+================+================+================+
| 1              | UTC            | Seconds into   | Float          | 0-604800.00    |
|                | Measurement    | the week       |                |                |
|                | Time           |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 2              | WGS-84         | DDMM.MMMM      | Float          | 0-89.9999      |
|                | Latitude       |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 3              | North/South    |                | Char           | N, S           |
|                | Indicator      |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 4              | WGS-84         | DDDMM.MMMM     | Float          | 0-179.9999     |
|                | Longitude      |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 5              | East/West      |                | Char           | E, W           |
|                | Indicator      |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 6              | Altitude (MSL) | Meters         | Float          |                |
+----------------+----------------+----------------+----------------+----------------+
| 7              | Geoidal Height | Meters         | Float          |                |
+----------------+----------------+----------------+----------------+----------------+
| 8              | Velocity East  | M/Sec          | Float          |                |
+----------------+----------------+----------------+----------------+----------------+
| 9              | Velocity North | M/Sec          | Float          |                |
+----------------+----------------+----------------+----------------+----------------+
| 10             | Navigation     |                | Int            | *Navigating*   |
|                | Mode           |                |                | 1=Position     |
|                |                |                |                | From a Remote  |
|                |                |                |                | Device         |
|                |                |                |                | 2=2D           |
|                |                |                |                | 3=3D           |
|                |                |                |                | 4=2D           |
|                |                |                |                | differential   |
|                |                |                |                | 5=3D           |
|                |                |                |                | differential   |
|                |                |                |                | *Not           |
|                |                |                |                | Navigating*    |
|                |                |                |                | 51=Too Few     |
|                |                |                |                | Satellites     |
|                |                |                |                | 52=DOPs too    |
|                |                |                |                | large          |
|                |                |                |                | 53=Position    |
|                |                |                |                | STD too large  |
|                |                |                |                | 54=Velocity    |
|                |                |                |                | STD too large  |
|                |                |                |                | 55=Too many    |
|                |                |                |                | iterations for |
|                |                |                |                | velocity       |
|                |                |                |                | 56=Too many    |
|                |                |                |                | iterations for |
|                |                |                |                | position       |
|                |                |                |                | 57=3 Sat       |
|                |                |                |                | Startup failed |
+----------------+----------------+----------------+----------------+----------------+

Example:

``$PMVXG,021,142244.00,5128.4744,N,00020.0593,W,00054.4,0047.4,0000.1,-000.2,03*66``

.. _mx4200data-output\_022:

$PMVXG,022
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DOPs
^^^^

This sentence reports the DOP (Dilution Of Precision) values actually
used in the measurement processing corresponding to the satellites
listed. The satellites are listed in receiver channel order. Fields
11-16 are output only on 12-channel receivers.

+----------------+----------------+----------------+----------------+----------------+
| Field          | Description    | Units          | Format         | Range          |
+================+================+================+================+================+
| 1              | UTC            | Seconds into   | Float          | 0-604800.00    |
|                | Measurement    | the week       |                |                |
|                | Time           |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 2              | East DOP       |                | Float          |                |
|                | (EDOP)         |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 3              | North DOP      |                | Float          |                |
|                | (NDOP)         |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 4              | Vertical DOP   |                | Float          |                |
|                | (VDOP)         |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 5              | PRN on Channel |                | Int            | 1-32           |
|                | #1             |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 6              | PRN on Channel |                | Int            | 1-32           |
|                | #2             |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 7              | PRN on Channel |                | Int            | 1-32           |
|                | #3             |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 8              | PRN on Channel |                | Int            | 1-32           |
|                | #4             |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 9              | PRN on Channel |                | Int            | 1-32           |
|                | #5             |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 10             | PRN on Channel |                | Int            | 1-32           |
|                | #6             |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 11             | PRN on Channel |                | Int            | 1-32           |
|                | #7             |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 12             | PRN on Channel |                | Int            | 1-32           |
|                | #8             |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 13             | PRN on Channel |                | Int            | 1-32           |
|                | #9             |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 14             | PRN on Channel |                | Int            | 1-32           |
|                | #10            |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 15             | PRN on Channel |                | Int            | 1-32           |
|                | #11            |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 16             | PRN on Channel |                | Int            | 1-32           |
|                | #12            |                |                |                |
+----------------+----------------+----------------+----------------+----------------+

Example:

``$PMVXG,022,142243.00,00.7,00.8,01.9,27,26,10,09,13,23*77``

.. _mx4200data-output\_030:

$PMVXG,030
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software Configuration
^^^^^^^^^^^^^^^^^^^^^^

This sentence contains the navigation processor and baseband firmware
version numbers.

+----------------+----------------+----------------+----------------+----------------+
| Field          | Description    | Units          | Format         | Range          |
+================+================+================+================+================+
| 1              | Nav Processor  |                | Char           |                |
|                | Version Number |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 2              | Baseband       |                | Char           |                |
|                | Firmware       |                |                |                |
|                | Version Number |                |                |                |
+----------------+----------------+----------------+----------------+----------------+

Example:

``$PMVXG,030,DA35,015``

.. _mx4200data-output\_101:

$PMVXG,101
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Control Sentence Accept/Reject
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This sentence is returned (on the Control Port) for every **$PMVXG** and
**$XXGPQ** sentence that is received.

+----------------+----------------+----------------+----------------+----------------+
| Field          | Description    | Units          | Format         | Range          |
+================+================+================+================+================+
| 1              | Sentence ID    |                | Char           |                |
+----------------+----------------+----------------+----------------+----------------+
| 2              | Accept/Reject  |                | Int            | 0=Sentence     |
|                | Status         |                |                | Accepted       |
|                |                |                |                | 1=Bad          |
|                |                |                |                | Checksum       |
|                |                |                |                | 2=Illegal      |
|                |                |                |                | Value          |
|                |                |                |                |                |
|                |                |                |                | 3=Unrecognized |
|                |                |                |                | ID             |
|                |                |                |                | 4=Wrong # of   |
|                |                |                |                | fields         |
|                |                |                |                | 5=Required     |
|                |                |                |                | Data Field     |
|                |                |                |                | Missing        |
|                |                |                |                | 6=Requested    |
|                |                |                |                | Sentence       |
|                |                |                |                | Unavailable    |
+----------------+----------------+----------------+----------------+----------------+
| 3              | Bad Field      |                | Int            |                |
|                | Index          |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 4              | Requested      |                | Char           |                |
|                | Sentence ID    |                |                |                |
|                | (If field #1 = |                |                |                |
|                | GPQ)           |                |                |                |
+----------------+----------------+----------------+----------------+----------------+

Example:

``$PMVXG,101,GPQ,0,,030*0D``

.. _mx4200data-output\_523:

$PMVXG,523
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Time Recovery Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This sentence contains the configuration of the time recovery function
of the receiver.

+----------------+----------------+----------------+----------------+----------------+
| Field          | Description    | Units          | Format         | Range          |
+================+================+================+================+================+
| 1              | Time Recovery  |                | Char           | D=Dynamic      |
|                | Mode           |                |                | S=Static       |
|                |                |                |                | K=Known        |
|                |                |                |                | Position       |
|                |                |                |                | N=No Time      |
|                |                |                |                | Recovery       |
+----------------+----------------+----------------+----------------+----------------+
| 2              | Time           |                | Char           | U=UTC Time     |
|                | Synchronizatio |                |                | G=GPS Time     |
|                | n              |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 3              | Time Mark Mode |                | Char           | A=Always       |
|                |                |                |                | Output Time    |
|                |                |                |                | Pulse          |
|                |                |                |                | V=Only when    |
|                |                |                |                | Valid          |
+----------------+----------------+----------------+----------------+----------------+
| 4              | Maximum Time   | Nsec           | Int            |                |
|                | Error for      |                |                |                |
|                | which a time   |                |                |                |
|                | mark will be   |                |                |                |
|                | considered     |                |                |                |
|                | valid          |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 5              | User Time Bias | Nsec           | Int            |                |
+----------------+----------------+----------------+----------------+----------------+
| 6              | Time Message   |                | Int            | 0=No Message   |
|                | Control        |                |                | 1=830 to       |
|                |                |                |                | Control Port   |
|                |                |                |                | 2=830 to       |
|                |                |                |                | Equipment Port |
+----------------+----------------+----------------+----------------+----------------+
| 7              | Not Used       |                |                |                |
+----------------+----------------+----------------+----------------+----------------+

Example:

``$PMVXG,523,S,U,A,0500,000000,1,0*23``

.. _mx4200data-output\_830:

$PMVXG,830
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Time Recovery Results
^^^^^^^^^^^^^^^^^^^^^

This sentence is output approximately 1 second preceding the 1PPS
output. It indicates the exact time of the next pulse, whether or not
the time mark will be valid (based on operator-specified error
tolerance), the time to which the pulse is synchronized, the receiver
operating mode, and the time error of the **last** 1PPS output. The leap
second flag (Field #11) is not output by older receivers.

+----------------+----------------+----------------+----------------+----------------+
| Field          | Description    | Units          | Format         | Range          |
+================+================+================+================+================+
| 1              | Time Mark      |                | Char           | T=Valid        |
|                | Valid          |                |                | F=Not Valid    |
+----------------+----------------+----------------+----------------+----------------+
| 2              | Year           |                | Int            | 1993-          |
+----------------+----------------+----------------+----------------+----------------+
| 3              | Month          |                | Int            | 1-12           |
+----------------+----------------+----------------+----------------+----------------+
| 4              | Day            | Nsec           | Int            | 1-31           |
+----------------+----------------+----------------+----------------+----------------+
| 5              | Time           | HH:MM:SS       | Int            | 00:00:00-23:59 |
|                |                |                |                | :59            |
+----------------+----------------+----------------+----------------+----------------+
| 6              | Time           |                | Char           | U=UTC          |
|                | Synchronizatio |                |                | G=GPS          |
|                | n              |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 7              | Operating Mode |                | Char           | D=Dynamic      |
|                |                |                |                | S=Static       |
|                |                |                |                | K=Known        |
|                |                |                |                | Position       |
+----------------+----------------+----------------+----------------+----------------+
| 8              | Oscillator     | PPB            | Int            |                |
|                | Offset -       |                |                |                |
|                | estimate of    |                |                |                |
|                | oscillator     |                |                |                |
|                | frequency      |                |                |                |
|                | error          |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 9              | Time Mark      | Nsec           | Int            |                |
|                | Error of last  |                |                |                |
|                | pulse          |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| 10             | User Time Bias | Nsec           | Int            |                |
+----------------+----------------+----------------+----------------+----------------+
| 11             | Leap Second    |                | Int            | -1,0,1         |
|                | Flag -         |                |                |                |
|                | indicates that |                |                |                |
|                | a leap second  |                |                |                |
|                | will occur.    |                |                |                |
|                | This value is  |                |                |                |
|                | usually zero   |                |                |                |
|                | except during  |                |                |                |
|                | the week prior |                |                |                |
|                | to a leap      |                |                |                |
|                | second         |                |                |                |
|                | occurrence,    |                |                |                |
|                | when this      |                |                |                |
|                | value will be  |                |                |                |
|                | set to +/-1. A |                |                |                |
|                | value of +1    |                |                |                |
|                | indicates that |                |                |                |
|                | GPS time will  |                |                |                |
|                | be 1 second    |                |                |                |
|                | further ahead  |                |                |                |
|                | of UTC time.   |                |                |                |
+----------------+----------------+----------------+----------------+----------------+

Example:

``$PMVXG,830,T,1998,10,12,15:30:46,U,S,000298,00003,000000,01*02``
