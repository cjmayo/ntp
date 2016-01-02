``ntpq`` - standard NTP query program
=====================================
.. program:: ntpq

Synopsis
--------

``ntpq [-46dinp] [-c command] [host] [...]``

Description
-----------

The ``ntpq`` utility program is used to monitor NTP daemon ``ntpd``
operations and determine performance. It uses the standard NTP mode 6
control message formats defined in Appendix B of the NTPv3 specification
:rfc:`1305`. The same formats are used in NTPv4, although some of the
variable names have changed and new ones added. The description on this
page is for the NTPv4 variables.

The program can be run either in interactive mode or controlled using
command line arguments. Requests to read and write arbitrary variables
can be assembled, with raw and pretty-printed output options being
available. The ``ntpq`` can also obtain and print a list of peers in a
common format by sending multiple queries to the server.

If one or more request options is included on the command line when
``ntpq`` is executed, each of the requests will be sent to the NTP
servers running on each of the hosts given as command line arguments, or
on localhost by default. If no request options are given, ``ntpq`` will
attempt to read commands from the standard input and execute these on
the NTP server running on the first host given on the command line,
again defaulting to localhost when no other host is specified. ``ntpq``
will prompt for commands if the standard input is a terminal device.

``ntpq`` uses NTP mode 6 packets to communicate with the NTP server, and
hence can be used to query any compatible server on the network which
permits it. Note that since NTP is a UDP protocol this communication
will be somewhat unreliable, especially over large distances in terms of
network topology. ``ntpq`` makes one attempt to retransmit requests, and
will time requests out if the remote host is not heard from within a
suitable timeout time.

Note that in contexts where a host name is expected, a ``-4`` qualifier
preceding the host name forces DNS resolution to the IPv4 namespace,
while a ``-6`` qualifier forces DNS resolution to the IPv6 namespace.

For examples and usage, see the :doc:`NTP Debugging Techniques <debug>` page.

Command line options are described following. Specifying a command line
option other than ``-i`` or ``-n`` will cause the specified query
(queries) to be sent to the indicated host(s) immediately. Otherwise,
``ntpq`` will attempt to read interactive format commands from the
standard input.

.. option:: -4

    Force DNS resolution of following host names on the command line to
    the IPv4 namespace.

.. option:: -6

    Force DNS resolution of following host names on the command line to
    the IPv6 namespace.

.. option:: -c

    The following argument is interpreted as an interactive format
    command and is added to the list of commands to be executed on the
    specified host(s). Multiple ``-c`` options may be given.

.. option:: -d

    Turn on debugging mode.

.. option:: -i

    Force ``ntpq`` to operate in interactive mode. Prompts will be
    written to the standard output and commands read from the standard
    input.

.. option:: -n

    Output all host addresses in dotted-quad numeric format rather than
    converting to the canonical host names.

.. option:: -p

    Print a list of the peers known to the server as well as a summary
    of their state. This is equivalent to the ``peers`` interactive
    command.

Internal Commands
-----------------

Interactive format commands consist of a keyword followed by zero to
four arguments. Only enough characters of the full keyword to uniquely
identify the command need be typed. The output of a command is normally
sent to the standard output, but optionally the output of individual
commands may be sent to a file by appending a ``>``, followed by a file
name, to the command line. A number of interactive format commands are
executed entirely within the ``ntpq`` program itself and do not result
in NTP mode-6 requests being sent to a server. These are described
following.

.. _ntpq-help:

``? [command_keyword]``

.. option:: help [command_keyword]

    A ``?`` by itself will print a list of all the command keywords
    known to ``ntpq``. A ``?`` followed by a command keyword will print
    function and usage information about the command.

.. _ntpq-addvars:

.. option::
    addvars name [ = value] [...]
    rmvars name [...]
    clearvars

    The arguments to this command consist of a list of items of the form
    ``name = value``, where the ``= value`` is ignored, and can be
    omitted in read requests. ``ntpq`` maintains an internal list in
    which data to be included in control messages can be assembled, and
    sent using the ``readlist`` and ``writelist`` commands described
    below. The ``addvars`` command allows variables and optional values
    to be added to the list. If more than one variable is to be added,
    the list should be comma-separated and not contain white space. The
    ``rmvars`` command can be used to remove individual variables from
    the list, while the ``clearlist`` command removes all variables from
    the list.

.. _ntpq-cooked:

.. option:: cooked

    Display server messages in prettyprint format.

.. _ntpq-debug:

.. option:: debug more | less | off

    Turns internal query program debugging on and off.

.. _ntpq-delay:

.. option:: delay <milliseconds>

    Specify a time interval to be added to timestamps included in
    requests which require authentication. This is used to enable
    (unreliable) server reconfiguration over long delay network paths or
    between machines whose clocks are unsynchronized. Actually the
    server does not now require timestamps in authenticated requests, so
    this command may be obsolete.

.. _ntpq-host:

.. option:: host <name>

    Set the host to which future queries will be sent. The name may be
    either a DNS name or a numeric address.

.. _ntpq-hostnames:

.. option:: hostnames [yes | no]

    If ``yes`` is specified, host names are printed in information
    displays. If ``no`` is specified, numeric addresses are printed
    instead. The default is ``yes``, unless modified using the command
    line ``-n`` switch.

.. _ntpq-keyid:

.. option:: keyid <keyid>

    This command specifies the key number to be used to authenticate
    configuration requests. This must correspond to a key ID configured
    in ``ntp.conf`` for this purpose.

.. _ntpq-keytype:

.. option:: keytype

    Specify the digest algorithm to use for authenticated requests, with
    default ``MD5``. If the OpenSSL library is installed, digest can be
    be any message digest algorithm supported by the library. The
    current selections are: ``MD2``, ``MD4``, ``MD5``, ``MDC2``,
    ``RIPEMD160``, ``SHA`` and ``SHA1``.

.. _ntpq-ntpversion:

.. option:: ntpversion 1 | 2 | 3 | 4

    Sets the NTP version number which ``ntpq`` claims in packets.
    Defaults to 2, Note that mode-6 control messages (and modes, for
    that matter) didn't exist in NTP version 1.

.. _ntpq-passwd:

.. option:: passwd

    This command prompts for a password to authenticate requests. The
    password must correspond to the key ID configured in ``ntp.conf``
    for this purpose.

.. _ntpq-quit:

.. option:: quit

    Exit ``ntpq``.

.. _ntpq-raw:

.. option:: raw

    Display server messages as received and without reformatting.

.. _ntpq-timeout:

.. option:: timeout <millseconds>

    Specify a timeout period for responses to server queries. The
    default is about 5000 milliseconds. Note that since ``ntpq`` retries
    each query once after a timeout, the total waiting time for a
    timeout will be twice the timeout value set.

Control Message Commands
------------------------

Association IDs are used to identify system, peer and clock variables.
System variables are assigned an association ID of zero and system name
space, while each association is assigned a nonzero association ID and
peer namespace. Most control commands send a single mode-6 message to
the server and expect a single response message. The exceptions are the
``peers`` command, which sends a series of messages, and the
``mreadlist`` and ``mreadvar`` commands, which iterate over a range of
associations.

.. _ntpq-as:

.. option:: associations

    Display a list of mobilized associations in the form

    ``ind assid status conf reach auth condition last_event cnt``

    +------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | Variable         | Description                                                                                                                                  |
    +------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | ``ind``          | index on this list                                                                                                                           |
    +------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | ``assid``        | association ID                                                                                                                               |
    +------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | ``status``       | :ref:`peer status word <decode-peer>`                                                                                                        |
    +------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | ``conf``         | ``yes``: persistent, ``no``: ephemeral                                                                                                       |
    +------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | ``reach``        | ``yes``: reachable, ``no``: unreachable                                                                                                      |
    +------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | ``auth``         | ``ok``, ``yes``, ``bad`` and ``none``                                                                                                        |
    +------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | ``condition``    | selection status (see the ``select`` field of the :ref:`peer status word <decode-peer>`)                                                     |
    +------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | ``last_event``   | event report (see the ``event`` field of the :ref:`peer status word <decode-peer>`)                                                          |
    +------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | ``cnt``          | event count (see the ``count`` field of the :ref:`peer status word <decode-peer>`)                                                           |
    +------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

.. _ntpq-cv:

.. option::
    clockvar assocID [name [ = value [...]] [...]
    cv assocID [name [ = value [...] ][...]

    Display a list of :ref:`clock variables  <ntpq-clock>`
    for those associations supporting a reference clock.

.. _ntpq-:config:

.. option:: :config [...]

    Send the remainder of the command line, including whitespace, to the
    server as a run-time configuration command in the same format as the
    configuration file. This command is experimental until further
    notice and clarification. Authentication is of course required.

.. _ntpq-config-from-file:

.. option:: config-from-file <filename>

    Send the each line of *filename* to the server as run-time
    configuration commands in the same format as the configuration file.
    This command is experimental until further notice and clarification.
    Authentication is required.

.. _ntpq-ifstats:

.. option:: ifstats

    Display statistics for each local network address. Authentication is
    required.

.. _ntpq-iostats:

.. option:: iostats

    Display network and reference clock I/O statistics.

.. _ntpq-kerninfo:

.. option:: kerninfo

    Display kernel loop and PPS statistics. As with other ntpq output,
    times are in milliseconds. The precision value displayed is in
    milliseconds as well, unlike the precision system variable.

.. _ntpq-lassoc:

.. option:: lassociations

    Perform the same function as the associations command, except
    display mobilized and unmobilized associations.

.. _ntpq-monstats:

.. option:: monstats

    Display monitor facility statistics.

.. _ntpq-mrulist:

.. option:: mrulist [limited | kod | mincount=count | laddr=localaddr | sort=sortorder | resany=hexmask | resall=hexmask]

    Obtain and print traffic counts collected and maintained by the
    monitor facility. With the exception of ``sort=sortorder``, the
    options filter the list returned by ``ntpd``. The ``limited`` and
    ``kod`` options return only entries representing client addresses
    from which the last packet received triggered either discarding or a
    KoD response. The ``mincount=count`` option filters entries
    representing less than ``count`` packets. The ``laddr=localaddr``
    option filters entries for packets received on any local address
    other than ``localaddr``. ``resany=hexmask`` and ``resall=hexmask``
    filter entries containing none or less than all, respectively, of
    the bits in ``hexmask``, which must begin with ``0x``.
    The ``sortorder`` defaults to ``lstint`` and may be any of ``addr``,
    ``count``, ``avgint``, ``lstint``, or any of those preceded by a
    minus sign (hyphen) to reverse the sort order. The output columns
    are:

    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Column               | Description                                                                                                                                                                                                                                              |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``lstint``           | Interval in s between the receipt of the most recent packet from this address and the completion of the retrieval of the MRU list by ``ntpq``.                                                                                                           |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``avgint``           | Average interval in s between packets from this address.                                                                                                                                                                                                 |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``rstr``             | Restriction flags associated with this address. Most are copied unchanged from the matching ``restrict`` command, however 0x400 (kod) and 0x20 (limited) flags are cleared unless the last packet from this address triggered a rate control response.   |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``r``                | Rate control indicator, either a period, ``L`` or ``K`` for no rate control response, rate limiting by discarding, or rate limiting with a KoD response, respectively.                                                                                   |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``m``                | Packet mode.                                                                                                                                                                                                                                             |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``v``                | Packet version number.                                                                                                                                                                                                                                   |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``count``            | Packets received from this address.                                                                                                                                                                                                                      |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``rport``            | Source port of last packet from this address.                                                                                                                                                                                                            |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``remote address``   | DNS name, numeric address, or address followed by claimed DNS name which could not be verified in parentheses.                                                                                                                                           |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _ntpq-mreadvar:

.. option:: mreadvar assocID assocID [ variable_name [ = value[ ... ]

.. _ntpq-mrv:

.. option:: mrv assocID assocID [ variable_name [ = value[ ... ]

    Perform the same function as the ``readvar`` command, except for a
    range of association IDs. This range is determined from the
    association list cached by the most recent ``associations`` command.

.. _ntpq-passoc:

.. option:: passociations

    Perform the same function as the ``associations command``, except
    that it uses previously stored data rather than making a new query.

.. _ntpq-pe:

.. option:: peers

    Display a list of peers in the form
    ``[tally]remote refid st t when pool reach delay offset jitter``

    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Variable      | Description                                                                                                                                                                                                  |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``[tally]``   | single-character code indicating current value of the ``select`` field of the :ref:`peer status word <decode-peer>`                                                                                          |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``remote``    | host name (or IP number) of peer                                                                                                                                                                             |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``refid``     | association ID or :ref:`kiss code <decode-kiss>`                                                                                                                                                             |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``st``        | stratum                                                                                                                                                                                                      |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``t``         | ``u``: unicast or manycast client, ``b``: broadcast or multicast client, ``l``: local (reference clock), ``s``: symmetric (peer), ``A``: manycast server, ``B``: broadcast server, ``M``: multicast server   |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``when``      | sec/min/hr since last received packet                                                                                                                                                                        |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``poll``      | poll interval (log:sub:`2` s)                                                                                                                                                                                |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``reach``     | reach shift register (octal)                                                                                                                                                                                 |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``delay``     | roundtrip delay                                                                                                                                                                                              |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``offset``    | offset of server relative to this host                                                                                                                                                                       |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``jitter``    | jitter                                                                                                                                                                                                       |
    +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _ntpq-rv:

.. option::
    readvar assocID name [ = value ] [,...]
    rv assocID [ name ] [,...]

    Display the specified variables. If ``assocID`` is zero, the
    variables are from the :ref:`system
    variables <ntpq-system>` name space,
    otherwise they are from the :ref:`peer
    variables <ntpq-peer>` name space. The
    ``assocID`` is required, as the same name can occur in both spaces.
    If no ``name`` is included, all operative variables in the name
    space are displayed. In this case only, if the ``assocID`` is
    omitted, it is assumed zero. Multiple names are specified with comma
    separators and without whitespace. Note that time values are
    represented in milliseconds and frequency values in
    parts-per-million (PPM). Some NTP timestamps are represented in the
    format YYYYMMDDTTTT, where YYYY is the year, MM the month of year,
    DD the day of month and TTTT the time of day.

.. _ntpq-saveconfig:

.. option:: saveconfig <filename>

    Write the current configuration, including any runtime modifications
    given with ``:config`` or ``config-from-file``, to the ntpd host's
    file *filename*. This command will be rejected by the server unless
    :ref:`saveconfigdir
    <miscopt-saveconfigdir>` appears in the
    ``ntpd`` configuration file. *filename* can use strftime() format
    specifies to substitute the current date and time, for example,
    ``saveconfig ntp-%Y%m%d-%H%M%S.conf``. The filename used is stored
    in system variable ``savedconfig``. Authentication is required.

.. _ntpq-writevar:

.. option:: writevar assocID name = value [,...]

    Write the specified variables. If the ``assocID`` is zero, the
    variables are from the :ref:`system
    variables <ntpq-system>` name space,
    otherwise they are from the :ref:`peer
    variables <ntpq-peer>` name space. The
    ``assocID`` is required, as the same name can occur in both spaces.

.. _ntpq-sysinfo:

.. option:: sysinfo

    Display operational summary.

.. _ntpq-sysstats:

.. option:: sysstats

    Print statistics counters maintained in the protocol module.

.. _ntpq-status:

Status Words and Kiss Codes
---------------------------------------------------------

The current state of the operating program is shown in a set of status
words maintained by the system and each association separately. These
words are displayed in the ``rv`` and ``as`` commands both in
hexadecimal and decoded short tip strings. The codes, tips and short
explanations are on the :doc:`Event Messages
and Status Words <decode>` page. The page also
includes a list of system and peer messages, the code for the latest of
which is included in the status word.

Information resulting from protocol machine state transitions is
displayed using an informal set of ASCII strings called
:ref:`kiss codes
<decode-kiss>`. The original purpose was for
kiss-o'-death (KoD) packets sent by the server to advise the client of
an unusual condition. They are now displayed, when appropriate, in the
reference identifier field in various billboards.

.. _ntpq-system:

System Variables
----------------------------------------------

The following system variables appear in the ``rv`` billboard. Not all
variables are displayed in some configurations.

+------------------+----------------------------------------------------------------------------------------------------+
| Variable         | Description                                                                                        |
+------------------+----------------------------------------------------------------------------------------------------+
| ``status``       | :ref:`system status word <decode-sys>`                                                             |
+------------------+----------------------------------------------------------------------------------------------------+
| ``version``      | NTP software version and build time                                                                |
+------------------+----------------------------------------------------------------------------------------------------+
| ``processor``    | hardware platform and version                                                                      |
+------------------+----------------------------------------------------------------------------------------------------+
| ``system``       | operating system and version                                                                       |
+------------------+----------------------------------------------------------------------------------------------------+
| ``leap``         | leap warning indicator (0-3)                                                                       |
+------------------+----------------------------------------------------------------------------------------------------+
| ``stratum``      | stratum (1-15)                                                                                     |
+------------------+----------------------------------------------------------------------------------------------------+
| ``precision``    | precision (log:sub:`2` s)                                                                          |
+------------------+----------------------------------------------------------------------------------------------------+
| ``rootdelay``    | total roundtrip delay to the primary reference clock                                               |
+------------------+----------------------------------------------------------------------------------------------------+
| ``rootdisp``     | total dispersion to the primary reference clock                                                    |
+------------------+----------------------------------------------------------------------------------------------------+
| ``peer``         | system peer association ID                                                                         |
+------------------+----------------------------------------------------------------------------------------------------+
| ``tc``           | time constant and poll exponent (log:sub:`2` s) (3-17)                                             |
+------------------+----------------------------------------------------------------------------------------------------+
| ``mintc``        | minimum time constant (log:sub:`2` s) (3-10)                                                       |
+------------------+----------------------------------------------------------------------------------------------------+
| ``clock``        | date and time of day                                                                               |
+------------------+----------------------------------------------------------------------------------------------------+
| ``refid``        | reference ID or :ref:`kiss code <decode-kiss>`                                                     |
+------------------+----------------------------------------------------------------------------------------------------+
| ``reftime``      | reference time                                                                                     |
+------------------+----------------------------------------------------------------------------------------------------+
| ``offset``       | combined offset of server relative to this host                                                    |
+------------------+----------------------------------------------------------------------------------------------------+
| ``sys_jitter``   | combined system jitter                                                                             |
+------------------+----------------------------------------------------------------------------------------------------+
| ``frequency``    | frequency offset (PPM) relative to hardware clock                                                  |
+------------------+----------------------------------------------------------------------------------------------------+
| ``clk_wander``   | clock frequency wander (PPM)                                                                       |
+------------------+----------------------------------------------------------------------------------------------------+
| ``clk_jitter``   | clock jitter                                                                                       |
+------------------+----------------------------------------------------------------------------------------------------+
| ``tai``          | TAI-UTC offset (s)                                                                                 |
+------------------+----------------------------------------------------------------------------------------------------+
| ``leapsec``      | NTP seconds when the next leap second is/was inserted                                              |
+------------------+----------------------------------------------------------------------------------------------------+
| ``expire``       | NTP seconds when the NIST leapseconds file expires                                                 |
+------------------+----------------------------------------------------------------------------------------------------+

The jitter and wander statistics are exponentially-weighted RMS
averages. The system jitter is defined in the NTPv4 specification; the
clock jitter statistic is computed by the clock discipline module.

When the NTPv4 daemon is compiled with the OpenSSL software library,
additional system variables are displayed, including some or all of the
following, depending on the particular Autokey dance:

+-----------------+-----------------------------------------------------+
| Variable        | Description                                         |
+-----------------+-----------------------------------------------------+
| ``host``        | Autokey host name for this host                     |
+-----------------+-----------------------------------------------------+
| ``ident``       | Autokey group name for this host                    |
+-----------------+-----------------------------------------------------+
| ``flags``       | host flags (see Autokey specification)              |
+-----------------+-----------------------------------------------------+
| ``digest``      | OpenSSL message digest algorithm                    |
+-----------------+-----------------------------------------------------+
| ``signature``   | OpenSSL digest/signature scheme                     |
+-----------------+-----------------------------------------------------+
| ``update``      | NTP seconds at last signature update                |
+-----------------+-----------------------------------------------------+
| ``cert``        | certificate subject, issuer and certificate flags   |
+-----------------+-----------------------------------------------------+
| ``until``       | NTP seconds when the certificate expires            |
+-----------------+-----------------------------------------------------+

.. _ntpq-peer:

Peer Variables
------------------------------------------

The following peer variables appear in the ``rv`` billboard for each
association. Not all variables are displayed in some configurations.

+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Variable                   | Description                                                                                                                  |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``associd``                | association ID                                                                                                               |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``status``                 | :ref:`peer status word <decode-peer>`                                                                                        |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``srcadr srcport``         | source (remote) IP address and port                                                                                          |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``dstadr dstport``         | destination (local) IP address and port                                                                                      |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``leap``                   | leap indicator (0-3)                                                                                                         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``stratum``                | stratum (0-15)                                                                                                               |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``precision``              | precision (log:sub:`2` s)                                                                                                    |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``rootdelay``              | total roundtrip delay to the primary reference clock                                                                         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``rootdisp``               | total root dispersion to the primary reference clock                                                                         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``refid``                  | reference ID or :ref:`kiss code <decode-kiss>`                                                                               |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``reftime``                | reference time                                                                                                               |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``reach``                  | reach register (octal)                                                                                                       |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``unreach``                | unreach counter                                                                                                              |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``hmode``                  | host mode (1-6)                                                                                                              |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``pmode``                  | peer mode (1-5)                                                                                                              |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``hpoll``                  | host poll exponent (log:sub:`2` s) (3-17)                                                                                    |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``ppoll``                  | peer poll exponent (log:sub:`2` s) (3-17)                                                                                    |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``headway``                | headway (see :doc:`Rate Management and the Kiss-o'-Death Packet) <rate>`                                                     |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``flash``                  | :ref:`flash status word <decode-flash>`                                                                                      |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``offset``                 | filter offset                                                                                                                |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``delay``                  | filter delay                                                                                                                 |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``dispersion``             | filter dispersion                                                                                                            |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``jitter``                 | filter jitter                                                                                                                |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``ident``                  | Autokey group name for this association                                                                                      |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``bias``                   | unicast/broadcast bias                                                                                                       |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``xleave``                 | interleave delay (see :doc:`NTP Interleaved Modes <xleave>`)                                                                 |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------+

The bias variable is calculated when the first broadcast packet is
received after the calibration volley. It represents the offset of the
broadcast subgraph relative to the unicast subgraph. The xleave variable
appears only the interleaved symmetric and interleaved modes. It
represents the internal queuing, buffering and transmission delays for
the preceding packet.

When the NTPv4 daemon is compiled with the OpenSSL software library,
additional peer variables are displayed, including the following:

+--------------------+------------------------------------------+
| Variable           | Description                              |
+--------------------+------------------------------------------+
| ``flags``          | peer flags (see Autokey specification)   |
+--------------------+------------------------------------------+
| ``host``           | Autokey server name                      |
+--------------------+------------------------------------------+
| ``flags``          | peer flags (see Autokey specification)   |
+--------------------+------------------------------------------+
| ``signature``      | OpenSSL digest/signature scheme          |
+--------------------+------------------------------------------+
| ``initsequence``   | initial key ID                           |
+--------------------+------------------------------------------+
| ``initkey``        | initial key index                        |
+--------------------+------------------------------------------+
| ``timestamp``      | Autokey signature timestamp              |
+--------------------+------------------------------------------+

.. _ntpq-clock:

Clock Variables
--------------------------------------------

The following clock variables appear in the ``cv`` billboard for each
association with a reference clock. Not all variables are displayed in
some configurations.

+------------------+---------------------------------------------------------------------------------------------+
| Variable         | Description                                                                                 |
+------------------+---------------------------------------------------------------------------------------------+
| ``associd``      | association ID                                                                              |
+------------------+---------------------------------------------------------------------------------------------+
| ``status``       | :ref:`clock status word <decode-clock>`                                                     |
+------------------+---------------------------------------------------------------------------------------------+
| ``device``       | device description                                                                          |
+------------------+---------------------------------------------------------------------------------------------+
| ``timecode``     | ASCII time code string (specific to device)                                                 |
+------------------+---------------------------------------------------------------------------------------------+
| ``poll``         | poll messages sent                                                                          |
+------------------+---------------------------------------------------------------------------------------------+
| ``noreply``      | no reply                                                                                    |
+------------------+---------------------------------------------------------------------------------------------+
| ``badformat``    | bad format                                                                                  |
+------------------+---------------------------------------------------------------------------------------------+
| ``baddata``      | bad date or time                                                                            |
+------------------+---------------------------------------------------------------------------------------------+
| ``fudgetime1``   | fudge time 1                                                                                |
+------------------+---------------------------------------------------------------------------------------------+
| ``fudgetime2``   | fudge time 2                                                                                |
+------------------+---------------------------------------------------------------------------------------------+
| ``stratum``      | driver stratum                                                                              |
+------------------+---------------------------------------------------------------------------------------------+
| ``refid``        | driver reference ID                                                                         |
+------------------+---------------------------------------------------------------------------------------------+
| ``flags``        | driver flags                                                                                |
+------------------+---------------------------------------------------------------------------------------------+
