``sntp`` - Simple Network Time Protocol (SNTP) Client
=====================================================
.. program:: sntp

Synopsis
--------

``sntp [{--help -?}][{-4 -6}][-a keynum][-b bcaddress][-B bctimeout][-c][-d][-D debug-level][-g delay][-K kodfile][-k keyfile][-l logfile][-M steplimit][-o ntpver][-r][-S][-s][-u uctimeout][--wait][--version][address(es)]``

Description
-----------

This program is a Simple Network Time Protocol (SNTP) client that can be
used to query a Network Time Protocol (NTP) server and display the time
offset of the system clock relative to the server clock. Run as root it
can correct the system clock to this offset as well. It can be run as an
interactive command or from a script by a ``cron`` job. The program
implements the SNTP client protocol defined in :rfc:`5905`, including the
full on-wire protocol but does not provide the sanity checks, access
controls, security functions and mitigation algorithms as in the full
NTP version 4 specification, also defined in :rfc:`5905`.

By default, ``sntp`` writes the local date and time (i.e., not UTC) to
the standard output in the format

``2011-08-04 00:40:36.642222 (+0000) +0.006611 +/- 0.041061  psp-os1 149.20.68.26 s3 no-leap``

where the ``+0.006611 +/- 0.041061`` indicates the time offset and error
bound of the system clock relative to the server clock, in seconds. The
hostname and/or the IP is displayed, as is the stratum of the server.
Finally, the leap indicator status is displayed.

If -b *bcaddress* is not specified, the program sends a single message
to each address and waits up to *uctimeout* (default 5) seconds for a
unicast server response. Otherwise, it sends no message and waits up to
*bctimeout* (default 68) seconds for a broadcast NTP message.

Options
-------

``sntp`` recognizes the following options:

.. option:: -?, --help

    displays usage information. The short form typically requires shell
    quoting, such as ``-\?``, otherwise ``?`` is consumed by the shell.

.. option:: -4, --ipv4

    When resolving hostnames to IP addresses, use IPv4 addresses only.

.. option:: -6, --ipv6

    When resolving hostnames to IP addresses, use IPv6 addresses only.
.. option:: -a <keynum>, --authentication <keynum>

    Enable authentication with the key ID *keynum*. *keynum* is a number
    specified in the keyfile along with an authentication secret
    (password or digest). See the ``-k, --keyfile`` option for more
    details.
.. option:: -b <bcaddress>, --broadcast <bcaddress>

    Listen for NTP packets sent to the broadcast or multicast address
    *bcaddress*, which can be a DNS name or IP address. The default
    maximum time to listen for broadcasts/multicasts, 68 seconds, can be
    modified with the ``-B, --bctimeout`` option.
.. option:: -B <bctimeout>, --bctimeout <bctimeout>

    Wait *bctimeout* seconds for broadcast or multicast NTP message
    before terminating. The default is 68 seconds, chosen because ntpd
    typically transmits broadcasts/multicasts every 64 seconds. Note
    that the short option is ``-B``, an uppercase letter B.

.. option:: -c, --concurrent

    Concurrently query all addresses returned for hostname. Requests
    from an NTP client to a single server should never be sent more
    often than once every two seconds. By default, all addresses
    resolved from a single hostname are assumed to be for a single
    instance of ntpd, and therefore sntp will send queries to these
    addresses one after another, waiting two seconds between queries.
    This option indicates multiple addresses returned for a hostname are
    on different machines, so sntp can send concurrent queries. This is
    appropriate when using \*.pool.ntp.org, for example.

.. option:: -d, --debug-level

    Increase debug verbosity level by one. May be specified multiple
    times. See also the ``-D, --set-debug-level`` option.
.. option:: -D <debug-level>, --set-debug-level <debug-level>

    Set the debug verbosity level to *debug-level*. The default level is
    zero. Note that the short option is ``-D``, an uppercase letter D.
    See also the ``-d, --debug-level`` option.
.. option:: -g <delay>, --gap <delay>

    Specify the *delay* in milliseconds between outgoing queries,
    defaulting to 50. ``sntp`` sends queries to all provided
    hostnames/addresses in short succession, and by default terminates
    once the first valid response is received. With multiple time
    sources provided, all but one will not be used. To limit the number
    of queries whose responses will not be used, each query is separated
    from the preceding one by *delay* milliseconds, to allow time for
    responses to earlier queries to be received. A larger *delay*
    reduces the query load on the time sources, increasing the time to
    receive a valid response if the first source attempted is slow or
    unreachable.
.. option:: -K <kodfile>, --kod <kodfile>

    Specifies the filename *kodfile* to be used for the persistent
    history of KoD (Kiss Of Death, or rate-limiting) responses received
    from servers. The default is ``/var/db/ntp-kod``. If the file does
    not exist, a warning message will be displayed. The file will not be
    created. Note that the short option is ``-K``, an uppercase letter
    K.
.. option:: -k <keyfile>, --keyfile <keyfile>

    Specifies the filename *keyfile* used with the
    ``-a``/``--authentication`` option. The format of the file is
    described on the :doc:`ntp-keygen page
    <keygen>`.
.. option:: -l <logfile>, --filelog <logfile>

    Specifies the filename in which to append a copy of status messages,
    which also appear on the terminal.
.. option:: -M <steplimit>, --steplimit <steplimit>

    If both ``-S``/``--step`` and ``-s``/``--slew`` options are
    provided, an offset of less than *steplimit* milliseconds will be
    corrected by slewing the clock using adjtime(), while an offset of
    *steplimit* or more will be corrected by setting the clock to the
    corrected time. Note that the short option is ``-M``, an uppercase
    letter M.
.. option:: -o <ntpver>, --ntpversion <ntpver>

    Specifies the NTP protocol version number *ntpver* to include in
    requests, default 4. This option is rarely useful.

.. option:: -r, --usereservedport

    By default, ``sntp`` uses a UDP source port number selected by the
    operating system. When this option is used, the reserved NTP port
    123 is used, which most often requires ``sntp`` be invoked as the
    superuser (commonly "root"). This can help identify connectivity
    failures due to port-based firewalling which affect ``ntpd``, which
    always uses source port 123.

.. option:: -S, --step

    By default, ``sntp`` displays the clock offset but does not attempt
    to correct it. This option enables offset correction by stepping,
    that is, directly setting the clock to the corrected time. This
    typically requires ``sntp`` be invoked as the superuser ("root").
    Note that the short option is ``-S``, an uppercase letter S.

.. option:: -s, --slew

    By default, ``sntp`` displays the clock offset but does not attempt
    to correct it. This option enables offset correction by slewing
    using adjtime(), which changes the rate of the clock for a period
    long enough to accomplish the required offset (phase) correction.
    This typically requires ``sntp`` be invoked as the superuser
    ("root").
.. option:: -u <uctimeout>, --uctimeout <uctimeout>

    Specifies the maximum time *uctimeout* in seconds to wait for a
    unicast response before terminating.

.. option:: --wait

    When neither ``-S``/``--step`` nor ``-s``/``--slew`` options are
    provided, ``sntp`` will by default terminate after the first valid
    response is received. This option causes ``sntp`` to instead wait
    for all pending queries' responses.

.. option:: --version

    Display the ``sntp`` program's version number and the date and time
    it was compiled.

Return Value
------------

The program returns an exit status of zero for if a valid response is
received and non-zero otherwise.

Author
------

This ``sntp`` was originally developed by Johannes Maximilian Kuehn.
Harlan Stenn and Dave Hart modified it to query more than one server at
a time. See the file ``ChangeLog`` in the distribution for details.
