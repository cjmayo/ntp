Miscellaneous Commands and Options
==================================

.. _miscopt-broadcastdelay:

.. confval:: broadcastdelay <delay>

    In broadcast and multicast modes, means are required to determine
    the network delay between the server and client. Ordinarily, this is
    done automatically by the initial calibration exchanges between the
    client and server. In some cases, the exchange might not be possible
    due to network or server access controls. The value of ``delay`` is
    by default zero, in which case the exchange is enabled. If ``delay``
    is greater than zero, it becomes the roundtrip delay (s), as
    measured by the Unix ``ping`` program, and the exchange is disabled.

.. _miscopt-driftfile:

.. confval:: driftfile <driftfile>

    This command specifies the complete path and name of the file used
    to record the frequency of the local clock oscillator. This is the
    same operation as the ``-f`` command line option. This command is
    mutually exclusive with the ``freq`` option of the ``tinker``
    command.
    If the file exists, it is read at startup in order to set the
    initial frequency and then updated once per hour or more with the
    current frequency computed by the daemon. If the file name is
    specified, but the file itself does not exist, the starts with an
    initial frequency of zero and creates the file when writing it for
    the first time. If this command is not given, the daemon will always
    start with an initial frequency of zero.
    The file format consists of a single line containing a single
    floating point number, which records the frequency offset measured
    in parts-per-million (PPM). The file is updated by first writing the
    current drift value into a temporary file and then renaming this
    file to replace the old version.

.. _miscopt-dscp:

.. confval:: dscp <dscp>

    This command specifies the Differentiated Services Code Point (DSCP)
    value that is used in sent NTP packets. The default value is 46 for
    Expedited Forwarding (EF).

.. _miscopt-enable:

.. confval:: enable [auth | bclient | calibrate | kernel | mode7 | monitor | ntp | stats]

.. confval:: disable [auth | bclient | calibrate | kernel | mode7 | monitor | ntp | stats]

    Provides a way to enable or disable various system options. Flags
    not mentioned are unaffected. Note that most of these flags can be
    modified remotely using :doc:`ntpq
    <ntpq>` utility program's ``:config`` and
    ``config-from-file`` commands.

    .. confval:: auth

        Enables the server to synchronize with unconfigured peers only
        if the peer has been correctly authenticated using either public
        key or private key cryptography. The default for this flag is
        enable.

    .. confval:: bclient

        Enables the server to listen for a message from a broadcast or
        multicast server, as in the ``multicastclient`` command with
        default address. The default for this flag is disable.

    .. confval:: calibrate

        Enables the calibrate feature for reference clocks. The default
        for this flag is disable.

    .. confval:: kernel

        Enables the kernel time discipline, if available. The default
        for this flag is enable if support is available, otherwise
        disable.

    .. confval:: mode7

        Enables processing of NTP mode 7 implementation-specific
        requests which are used by the deprecated ``ntpdc`` program. The
        default for this flag is disable. This flag is excluded from
        runtime configuration using ``ntpq``. The ``ntpq`` program
        provides the same capabilities as ``ntpdc`` using standard mode
        6 requests.

    .. confval:: monitor

        Enables the monitoring facility. See the
        :doc:`ntpq program
        <ntpq>` and the ``monstats`` and
        ``mrulist`` commands, as well as the
        :ref:`Access Control Options
        <accopt-discard>` for details. The
        monitoring facility is also enabled by the presence of
        :ref:`limited
        <accopt-limited>` in any ``restrict``
        commands. The default for this flag is enable.

    .. confval:: ntp

        Enables time and frequency discipline. In effect, this switch
        opens and closes the feedback loop, which is useful for testing.
        The default for this flag is enable.

    .. confval:: stats

        Enables the statistics facility. See the
        :doc:`Monitoring Options
        <monopt>` page for further information.
        The default for this flag is enabled. This flag is excluded from
        runtime configuration using ``ntpq``.

.. _miscopt-includefile:

.. confval:: includefile <includefile>

    This command allows additional configuration commands to be included
    from a separate file. Include files may be nested to a depth of
    five; upon reaching the end of any include file, command processing
    resumes in the previous configuration file. This option is useful
    for sites that run ``ntpd`` on multiple hosts, with (mostly) common
    options (e.g., a restriction list).

.. _miscopt-interface:

.. confval:: interface [listen | ignore | drop] [all | ipv4 | ipv6 | wildcard | name | address[/prefixlen]]

    This command controls which network addresses ``ntpd`` opens, and
    whether input is dropped without processing. The first parameter
    determines the action for addresses which match the second
    parameter. That parameter specifies a class of addresses, or a
    specific interface name, or an address. In the address case,
    ``prefixlen`` determines how many bits must match for this rule to
    apply. ``ignore`` prevents opening matching addresses, ``drop``
    causes ``ntpd`` to open the address and drop all received packets
    without examination. Multiple ``interface`` commands can be used.
    The last rule which matches a particular address determines the
    action for it. ``interface`` commands are disabled if any
    :ref:`-I <ntpd---interface>`,
    :ref:`--interface <ntpd---interface>`,
    :ref:`-L <ntpd---novirtualips>`, or
    :ref:`--novirtualips <ntpd---novirtualips>` command-line options
    are used. If none of those options are used and no ``interface``
    actions are specified in the configuration file, all available
    network addresses are opened. The ``nic`` command is an alias for
    ``interface``.

.. _miscopt-leapfile:

.. confval:: leapfile <leapfile>

    This command loads the NIST leapseconds file and initializes the
    leapsecond values for the next leapsecond time, expiration time and
    TAI offset. The file can be obtained directly from NIST national
    time servers using ``ftp`` as the ASCII file ``pub/leap-seconds``.
    The *leapfile* is scanned when ``ntpd`` processes the ``leapfile``
    directive or when ``ntpd`` detects that *leapfile* has changed.
    ``ntpd`` checks once a day to see if the *leapfile* has changed.
    While not strictly a security function, the Autokey protocol
    provides means to securely retrieve the current or updated
    leapsecond values from a server.

.. _miscopt-leapsmearinterval:

.. confval:: leapsmearinterval <seconds>

    This EXPERIMENTAL option is only available if ``ntpd`` was built
    with the ``--enable-leap-smear`` option to the ``configure`` script.
    It specifies the interval over which a leap second correction will
    be applied. Recommended values for this option are between 7200 (2
    hours) and 86400 (24 hours). **DO NOT USE THIS OPTION ON
    PUBLIC-ACCESS SERVERS!** See :ntp_bug:`2855` for more information.

.. _miscopt-logconfig:

.. confval:: logconfig <configkeyword>

    This command controls the amount and type of output written to the
    system ``syslog`` facility or the alternate ``logfile`` log file.
    All ``configkeyword`` keywords can be prefixed with ``=``, ``+``
    and ``-``, where ``=`` sets the ``syslogmask``, ``+`` adds and ``-``
    removes messages. ``syslog messages`` can be controlled in four
    classes (``clock``, ``peer``, ``sys`` and ``sync``). Within these
    classes four types of messages can be controlled: informational
    messages (``info``), event messages (``events``), statistics
    messages (``statistics``) and status messages (``status``).
    Configuration keywords are formed by concatenating the message class
    with the event class. The ``all`` prefix can be used instead of a
    message class. A message class may also be followed by the ``all``
    keyword to enable/disable all messages of the respective message
    class. By default, ``logconfig`` output is set to ``allsync``.
    Thus, a minimal log configuration could look like this:
    ``logconfig=syncstatus +sysevents``
    This would just list the synchronizations state of ``ntpd`` and the
    major system events. For a simple reference server, the following
    minimum message configuration could be useful:
    ``logconfig=syncall +clockall``
    This configuration will list all clock information and
    synchronization information. All other events and messages about
    peers, system events and so on is suppressed.

.. _miscopt-logfile:

.. confval:: logfile <logfile>

    This command specifies the location of an alternate log file to be
    used instead of the default system ``syslog`` facility. This is the
    same operation as the ``-l`` command line option.

.. _miscopt-mru:

.. confval:: mru [maxdepth <count> | maxmem <kilobytes> | mindepth <count> | maxage <seconds> | initalloc <count> | initmem <kilobytes> | incalloc <count> | incmem <kilobytes>]

    Controls size limits of the monitoring facility Most Recently Used
    :ref:`(MRU) list <ntpq-mrulist>` of client addresses, which
    is also used by the :ref:`rate control facility <accopt-discard>`.

    .. confval:: maxdepth <count>
    .. confval:: maxmem <kilobytes>

        Equivalent upper limits on the size of the MRU list, in terms of
        entries or kilobytes. The actual limit will be up to
        ``incalloc`` entries or ``incmem`` kilobytes larger. As with all
        of the ``mru`` options offered in units of entries or kilobytes,
        if both ``maxdepth`` and ``maxmem`` are used, the last one used
        controls. The default is 1024 kilobytes.

    .. confval:: mindepth <count>

        Lower limit on the MRU list size. When the MRU list has fewer
        than ``mindepth`` entries, existing entries are never removed to
        make room for newer ones, regardless of their age. The default
        is 600 entries.

    .. confval:: maxage <seconds>

        Once the MRU list has ``mindepth`` entries and an additional
        client address is to be added to the list, if the oldest entry
        was updated more than ``maxage`` seconds ago, that entry is
        removed and its storage reused. If the oldest entry was updated
        more recently, the MRU list is grown, subject to
        ``maxdepth``/``maxmem``. The default is 64 seconds.

    .. confval:: initalloc <count>
    .. confval:: initmem <kilobytes>

        Initial memory allocation at the time the monitoring facility is
        first enabled, in terms of entries or kilobytes. The default is
        4 kilobytes.

    .. confval:: incalloc <count>
    .. confval:: incmem <kilobytes>

        Size of additional memory allocations when growing the MRU list,
        in entries or kilobytes. The default is 4 kilobytes.

.. _miscopt-nonvolatile:

.. confval:: nonvolatile <threshold>

    Specify the ``threshold`` in seconds to write the frequency file,
    with default of 1e-7 (0.1 PPM). The frequency file is inspected each
    hour. If the difference between the current frequency and the last
    value written exceeds the threshold, the file is written and the
    ``threshold`` becomes the new threshold value. If the threshold is
    not exceeded, it is reduced by half. This is intended to reduce the
    frequency of unnecessary file writes for embedded systems with
    nonvolatile memory.

.. _miscopt-phone:

.. confval:: phone <dial> ...

    This command is used in conjunction with the ACTS modem driver (type
    18). The arguments consist of a maximum of 10 telephone numbers used
    to dial USNO, NIST or European time services. The Hayes command
    ATDT is normally prepended to the number, which can contain other
    modem control codes as well.

.. _miscopt-reset:

.. confval:: reset [allpeers] [auth] [ctl] [io] [mem] [sys] [timer]

    Reset one or more groups of counters maintained by ntpd and exposed
    by ``ntpq`` and ``ntpdc``.

.. _miscopt-rlimit:

.. confval:: rlimit [memlock <Nmegabytes> | stacksize <N4kPages> | filenum <Nfiledescriptors>]

    This command alters certain process storage allocation limits, and
    is only available on some operating systems. Options are as follows:

    .. confval:: memlock <Nmegabytes>

        Specify the number of megabytes of memory that can be allocated.
        Probably only available under Linux, this option is useful when
        dropping root (the ``-i`` option). The default is 32 megabytes.
        Setting this to zero will prevent any attemp to lock memory.

    .. confval:: stacksize <N4kPages>

        Specifies the maximum size of the process stack on systems with
        the ``mlockall()`` function. Defaults to 50 4k pages (200 4k
        pages in OpenBSD).

    .. confval:: filenum <Nfiledescriptors>

        Specifies the maximum number of file descriptors ntp may have
        open at the same time. Defaults to system default.

.. _miscopt-saveconfigdir:

.. confval:: saveconfigdir <directory_path>

    Specify the directory in which to write configuration snapshots
    requested with ``ntpq``'s :ref:`saveconfig <ntpq-saveconfig>` command.
    If ``saveconfigdir`` does not appear in the configuration file,
    saveconfig requests are rejected by ntpd.

.. _miscopt-setvar:

.. confval:: setvar <variable> [default]

    This command adds an additional system variable. These variables can
    be used to distribute additional information such as the access
    policy. If the variable of the form ``name = value`` is followed by
    the ``default`` keyword, the variable will be listed as part of the
    default system variables (``ntpq rv`` command). These additional
    variables serve informational purposes only. They are not related to
    the protocol other that they can be listed. The known protocol
    variables will always override any variables defined via the
    ``setvar`` mechanism. There are three special variables that contain
    the names of all variable of the same group. The ``sys_var_list``
    holds the names of all system variables. The ``peer_var_list`` holds
    the names of all peer variables and the ``clock_var_list`` holds the
    names of the reference clock variables.

.. _miscopt-tinker:

.. confval:: tinker [allan allan | dispersion dispersion | freq freq | huffpuff huffpuff | panic panic | step step | stepout stepout]

    This command alters certain system variables used by the clock
    discipline algorithm. The default values of these variables have
    been carefully optimized for a wide range of network speeds and
    reliability expectations. Very rarely is it necessary to change the
    default values; but, some folks can't resist twisting the knobs.
    Options are as follows:

    .. confval:: allan <allan>

        Specifies the Allan intercept, which is a parameter of the
        PLL/FLL clock discipline algorithm, in seconds with default 1500
        s.

    .. confval:: dispersion <dispersion>

        Specifies the dispersion increase rate in parts-per-million
        (PPM) with default 15 PPM.

    .. confval:: freq <freq>

        Specifies the frequency offset in parts-per-million (PPM). This
        option is mutually exclusive with the driftfile command.

    .. confval:: huffpuff <huffpuff>

        Specifies the huff-n'-puff filter span, which determines the
        most recent interval the algorithm will search for a minimum
        delay. The lower limit is 900 s (15 min), but a more reasonable
        value is 7200 (2 hours). See the
        :doc:`Huff-n'-Puff Filter <huffpuff>` page for further information.

    .. confval:: panic <panic>

        Specifies the panic threshold in seconds with default 1000 s. If
        set to zero, the panic sanity check is disabled and a clock
        offset of any value will be accepted.

    .. confval:: step <step>

        Specifies the step threshold in seconds. The default without
        this command is 0.128 s. If set to zero, step adjustments will
        never occur. Note: The kernel time discipline is disabled if the
        step threshold is set to zero or greater than 0.5 s. Further
        details are on the :doc:`Clock State Machine <clock>` page.

    .. confval:: stepout <stepout>

        Specifies the stepout threshold in seconds. The default without
        this command is 300 s. Since this option also affects the
        training and startup intervals, it should not be set less than
        the default. Further details are on the
        :doc:`Clock State Machine <clock>` page.

.. _miscopt-tos:

.. confval::
    tos [beacon <beacon> | ceiling <ceiling> | cohort {0 | 1} | floor <floor> | maxclock <maxclock> | maxdist <maxdist> | minclock <minclock> | mindist <mindist> | minsane <minsane> | orphan <stratum> | orphanwait <delay>]

    This command alters certain system variables used by the the clock
    selection and clustering algorithms. The default values of these
    variables have been carefully optimized for a wide range of network
    speeds and reliability expectations. Very rarely is it necessary to
    change the default values; but, some folks can't resist twisting the
    knobs. It can be used to select the quality and quantity of peers
    used to synchronize the system clock and is most useful in dynamic
    server discovery schemes. The options are as follows:

    .. confval:: beacon <beacon>

        The manycast server sends packets at intervals of 64 s if less
        than ``maxclock`` servers are available. Otherwise, it sends
        packets at the ``beacon`` interval in seconds. The default is
        3600 s. See the :doc:`Automatic Server Discovery <discover>` page
        for further details.

    .. confval:: ceiling <ceiling>

        Specify the maximum stratum (exclusive) for acceptable server
        packets. The default is 16. See the
        :doc:`Automatic Server Discovery <discover>` page for further details.

    .. confval:: cohort { 0 | 1 }

        Specify whether (1) or whether not (0) a server packet will be
        accepted for the same stratum as the client. The default is 0.
        See the :doc:`Automatic Server Discovery <discover>` page for further
        details.

    .. confval:: floor <floor>

        Specify the minimum stratum (inclusive) for acceptable server
        packets. The default is 1. See the
        :doc:`Automatic Server Discovery
        <discover>` page for further details.

    .. confval:: maxclock <maxclock>

        Specify the maximum number of servers retained by the server
        discovery schemes. The default is 10. See the
        :doc:`Automatic Server Discovery
        <discover>` page for further details.

    .. confval:: maxdist <maxdistance>

        Specify the synchronization distance threshold used by the clock
        selection algorithm. The default is 1.5 s. This determines both
        the minimum number of packets to set the system clock and the
        maximum roundtrip delay. It can be decreased to improve
        reliability or increased to synchronize clocks on the Moon or
        planets.

    .. confval:: minclock <minclock>

        Specify the number of servers used by the clustering algorithm
        as the minimum to include on the candidate list. The default is
        3. This is also the number of servers to be averaged by the
        combining algorithm.

    .. confval:: mindist <mindistance>

        Specify the minimum distance used by the selection and
        anticlockhop algorithm. Larger values increase the tolerance for
        outliers; smaller values increase the selectivity. The default
        is .001 s. In some cases, such as reference clocks with high
        jitter and a PPS signal, it is useful to increase the value to
        insure the intersection interval is always nonempty.

    .. confval:: minsane <minsane>

        Specify the number of servers used by the selection algorithm as
        the minimum to set the system clock. The default is 1 for legacy
        purposes; however, for critical applications the value should be
        somewhat higher but less than ``minclock``.

    .. confval:: orphan <stratum>

        Specify the orphan stratum with default 16. If less than 16 this
        is the stratum assumed by the root servers. See the
        :doc:`Orphan Mode
        <orphan>` page for further details.

    .. confval:: orphanwait <delay>

        Specify the delay in seconds from the time all sources are lost
        until orphan parent mode is enabled with default 300 s (five
        minutes). During this period, the local clock driver and the
        modem driver are not selectable, unless marked with the
        ``prefer`` keyword. This allows time for one or more primary
        sources to become reachable and selectable before using backup
        sources, and avoids transient use of the backup sources at
        startup.

.. _miscopt-trap:

.. confval:: trap host_address [port <port_number>] [interface <interface_address>]

    This command configures a trap receiver at the given host address
    and port number for sending messages with the specified local
    interface address. If the port number is unspecified, a value of
    18447 is used. If the interface address is not specified, the
    message is sent with a source address of the local interface the
    message is sent through. Note that on a multihomed host the
    interface used may vary from time to time with routing changes.
    The trap receiver will generally log event messages and other
    information from the server in a log file. While such monitor
    programs may also request their own trap dynamically, configuring a
    trap receiver will ensure that no messages are lost when the server
    is started.

.. _miscopt-ttl:

.. confval:: ttl <hop> ...

    This command specifies a list of TTL values in increasing order. up
    to 8 values can be specified. In manycast mode these values are used
    in turn in an expanding-ring search. The default is eight multiples
    of 32 starting at 31.
