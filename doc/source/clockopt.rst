Reference Clock Commands and Options
====================================

.. _clockopt-addrs:

Reference Clock Adddresses
-------------------------------------------------------

Unless noted otherwise, further information about these ccommands is on
the :doc:`Reference Clock Support
<refclock>` page.

Reference clocks are identified by a syntactically correct but invalid
IP address, in order to distinguish them from ordinary NTP peers. These
addresses are of the form 127.127.\ *t*.\ *u*, where *t* is an integer
denoting the clock type and *u* indicates the unit number in the range
0-3. While it may seem overkill, it is in fact sometimes useful to
configure multiple reference clocks of the same type, in which case the
unit numbers must be unique.

.. _clockopt-cmd:

Commands and Options
-----------------------------------------------

.. _clockopt-server:

``server 127.127.t.u [prefer] [mode int] [minpoll int] [maxpoll int]``
    This command can be used to configure reference clocks in special
    ways. The options are interpreted as follows:

    .. confval:: prefer

        Marks the reference clock as preferred. All other things being
        equal, this host will be chosen for synchronization among a set
        of correctly operating hosts. See the
        :doc:`Mitigation Rules and the prefer
        Keyword <prefer>` page for further
        information.

    .. confval:: mode <int>

        Specifies a mode number which is interpreted in a
        device-specific fashion. For instance, it selects a dialing
        protocol in the ACTS driver and a device subtype in the
        ``parse`` drivers.

    .. confval:: minpoll <int>

     .. confval:: maxpoll <int>

        These options specify the minimum and maximum polling interval
        for reference clock messages in log\ :sub:`2` seconds. For most
        directly connected reference clocks, both ``minpoll`` and
        ``maxpoll`` default to 6 (64 s). For modem reference clocks,
        ``minpoll`` is ordinarily set to 10 (about 17 m) and ``maxpoll``
        to 15 (about 9 h). The allowable range is 4 (16 s) to 17 (36 h)
        inclusive.

.. _clockopt-fudge:

``fudge 127.127.t.u [time1 sec] [time2 sec]     [stratum int] [refid string] [flag1 0|1]     [flag2 0|1] [flag3 0|1] [flag4 0|1]``
    This command can be used to configure reference clocks in special
    ways. It must immediately follow the ``server`` command which
    configures the driver. Note that the same capability is possible at
    run time using the :doc:`ntpdc
    <ntpdc>` program. The options are
    interpreted as follows:

    .. confval:: time1 <sec>

        Specifies a constant to be added to the time offset produced by
        the driver, a fixed-point decimal number in seconds. This is
        used as a calibration constant to adjust the nominal time offset
        of a particular clock to agree with an external standard, such
        as a precision PPS signal. It also provides a way to correct a
        systematic error or bias due to serial port or operating system
        latencies, different cable lengths or receiver internal delay.
        The specified offset is in addition to the propagation delay
        provided by other means, such as internal DIPswitches. Where a
        calibration for an individual system and driver is available, an
        approximate correction is noted in the driver documentation
        pages.
        Note: in order to facilitate calibration when more than one
        radio clock or PPS signal is supported, a special calibration
        feature is available. It takes the form of an argument to the
        ``enable`` command described in the
        :doc:`Miscellaneous Options
        <miscopt>` page and operates as
        described in the :doc:`Reference Clock
        Support <refclock>` page.

    .. confval:: time2 <secs>

        Specifies a fixed-point decimal number in seconds, which is
        interpreted in a driver-dependent way. See the descriptions of
        specific drivers in the :doc:`Reference
        Clock Support <refclock>` page.

    .. confval:: stratum <int>

        Specifies the stratum number assigned to the driver in the range
        0 to 15, inclusive. This number overrides the default stratum
        number ordinarily assigned by the driver itself, usually zero.

    .. confval:: refid <string>

        Specifies an ASCII string of from one to four characters which
        defines the reference identifier used by the driver. This string
        overrides the default identifier ordinarily assigned by the
        driver itself.
    ``flag1 flag2 flag3 flag4``
        These four flags are used for customizing the clock driver. The
        interpretation of these values, and whether they are used at
        all, is a function of the particular driver. However, by
        convention ``flag4`` is used to enable recording monitoring data
        to the ``clockstats`` file configured with the ``filegen``
        command. Additional information on the ``filegen`` command is on
        the :doc:`Monitoring Options
        <monopt>` page.
