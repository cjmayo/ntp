Monitoring Commands and Options
===============================

.. _monopt-intro:

Naming Conventions
-----------------------------------------------

The ``ntpd`` includes a comprehensive monitoring facility which collects
statistical data of various types and writes the data to files
associated with each type at defined events or intervals. The files
associated with a particular type are collectively called the generation
file set for that type. The files in the file set are the members of
that set.

File sets have names specific to the type and generation epoch. The
names are constructed from three concatenated elements ``prefix``,
``filename`` and ``suffix``:

.. option:: prefix

    The directory path specified in the ``statsdir`` command.

.. option:: name

    The name specified by the ``file`` option of the ``filegen``
    command.

.. option:: suffix

    A string of elements bdginning with . (dot) followed by a number of
    elements depending on the file set type.

Statistics files can be managed using scripts, examples of which are in
the ``./scripts`` directory. Using these or similar scripts and Unix
``cron`` jobs, the files can be automatically summarized and archived
for retrospective analysis.

.. _monopt-cmd:

Monitoring Commands and Options
----------------------------------------------------------

Unless noted otherwise, further information about these commands is on
the :doc:`Event Messages and Status Codes
<decode>` page.

.. _monopt-filegen:

``filegen name [file filename] [type type] [link | nolink] [enable | disable]``

    .. option:: name

        Specifies the file set type from the list in the next section.

    .. option:: file <filename>

        Specifies the filename prefix. The default is the file set type,
        such as "loopstats".

    .. option:: type <typename>

        Specifies the file set interval. The following intervals are
        supported with default ``day``:

        .. option:: none

            The file set is actually a single plain file.

        .. option:: pid

            One file set member is created for every incarnation of
            ``ntpd``. The file name suffix is the string .\ ``n``, where
            ``n`` is the process ID of the ``ntpd`` server process.

        .. option:: day

            One file set member is created per day. A day is defined as
            the period between 00:00 and 23:59 UTC. The file name suffix
            is the string .\ ``yyyymmdd``, where ``yyyy`` is the year,
            ``mm`` the month of the year and ``dd`` the day of the
            month. Thus, member created on 10 December 1992 would have
            suffix ``.19921210``.

        .. option:: week

            One file set member is created per week. The week is defined
            as the day of year modulo 7. The file name suffix is the
            string .\ ``yyyyWww``, where ``yyyy`` is the year, ``W``
            stands for itself and ``ww`` the week number starting from
            0. For example, The member created on 10 January 1992 would
            have suffix ``.1992W1``.

        .. option:: month

            One file set member is created per month. The file name
            suffix is the string .\ ``yyyymm``, where ``yyyy`` is the
            year and ``mm`` the month of the year starting from 1. For
            example, The member created on 10 January 1992 would have
            suffix ``.199201``.

        .. option:: year

            One file set member is generated per year. The file name
            suffix is the string .\ ``yyyy``, where ``yyyy`` is the
            year. For example, The member created on 1 January 1992
            would have suffix ``.1992``.

        .. option:: age

            One file set member is generated every 24 hours of ``ntpd``
            operation. The filename suffix is the string ``.adddddddd``,
            where ``a`` stands for itself and ``dddddddd`` is the
            ``ntpd`` running time in seconds at the start of the
            corresponding 24-hour period.

    ``link | nolink``
        It is convenient to be able to access the current file set
        members by file name, but without the suffix. This feature is
        enabled by ``link`` and disabled by ``nolink``. If enabled,
        which is the default, a hard link from the current file set
        member to a file without suffix is created. When there is
        already a file with this name and the number of links to this
        file is one, it is renamed by appending a dot, the letter ``C``,
        and the pid of the ``ntpd`` server process. When the number of
        links is greater than one, the file is unlinked. This allows the
        current file to be accessed by a constant name.
    ``enable | disable``
        Enable or disable the recording function, with default
        ``enable``. These options are intended for remote configuration
        commands.

.. _monopt-statistics:

``statistics name...``
    Enables writing of statistics records. Currently, eight kinds of
    statistics are supported: *name*\ s specify the file set type(s)
    from the list in the next section.

.. _monopt-statsdir:

.. option:: statsdir <directory_path>

    Specify the directory path prefix for statistics file names.

.. _monopt-types:

File Set Types
-------------------------------------------

.. option:: clockstats

    Record reference clock statistics. Each update received from a
    reference clock driver appends one line to the ``clockstats`` file
    set:
    ``49213 525.624 127.127.4.1 93 226 00:08:29.606 D``
    +-------------------+---------+---------------------------+
    | Item              | Units   | Description               |
    +-------------------+---------+---------------------------+
    | ``49213``         | MJD     | date                      |
    +-------------------+---------+---------------------------+
    | ``525.624``       | s       | time past midnight        |
    +-------------------+---------+---------------------------+
    | ``127.127.4.1``   | IP      | reference clock address   |
    +-------------------+---------+---------------------------+
    | ``message``       | text    | log message               |
    +-------------------+---------+---------------------------+

    The ``message`` field includes the last timecode received in decoded
    ASCII format, where meaningful. In some cases a good deal of
    additional information is displayed. See information specific to
    each reference clock for further details.

.. option:: cryptostats

    Record significant events in the Autokey protocol. This option
    requires the OpenSSL cryptographic software library. Each event
    appends one line to the ``cryptostats`` file set:
    ``49213 525.624 128.4.1.1 message``
    +-----------------+---------+-------------------------------------------+
    | Item            | Units   | Description                               |
    +-----------------+---------+-------------------------------------------+
    | ``49213``       | MJD     | date                                      |
    +-----------------+---------+-------------------------------------------+
    | ``525.624``     | s       | time past midnight                        |
    +-----------------+---------+-------------------------------------------+
    | ``128.4.1.1``   | IP      | source address (``0.0.0.0`` for system)   |
    +-----------------+---------+-------------------------------------------+
    | ``message``     | text    | log message                               |
    +-----------------+---------+-------------------------------------------+

    The ``message`` field includes the message type and certain
    ancillary information. See the
    :doc:`Authentication Options
    <authopt>` page for further information.

.. option:: loopstats

    Record clock discipline loop statistics. Each system clock update
    appends one line to the ``loopstats`` file set:
    ``50935 75440.031 0.000006019 13.778 0.000351733 0.013380 6``
    +-------------------+-------------------+---------------------------------------+
    | Item              | Units             | Description                           |
    +-------------------+-------------------+---------------------------------------+
    | ``50935``         | MJD               | date                                  |
    +-------------------+-------------------+---------------------------------------+
    | ``75440.031``     | s                 | time past midnight                    |
    +-------------------+-------------------+---------------------------------------+
    | ``0.000006019``   | s                 | clock offset                          |
    +-------------------+-------------------+---------------------------------------+
    | ``13.778``        | PPM               | frequency offset                      |
    +-------------------+-------------------+---------------------------------------+
    | ``0.000351733``   | s                 | RMS jitter                            |
    +-------------------+-------------------+---------------------------------------+
    | ``0.013380``      | PPM               | RMS frequency jitter (aka wander)     |
    +-------------------+-------------------+---------------------------------------+
    | ``6``             | log\ :sub:`2` s   | clock discipline loop time constant   |
    +-------------------+-------------------+---------------------------------------+

.. option:: peerstats

    Record peer statistics. Each NTP packet or reference clock update
    received appends one line to the ``peerstats`` file set:
    ``48773 10847.650 127.127.4.1 9714 -0.001605376 0.000000000 0.001424877 0.000958674``
    +--------------------+---------+----------------------+
    | Item               | Units   | Description          |
    +--------------------+---------+----------------------+
    | ``48773``          | MJD     | date                 |
    +--------------------+---------+----------------------+
    | ``10847.650``      | s       | time past midnight   |
    +--------------------+---------+----------------------+
    | ``127.127.4.1``    | IP      | source address       |
    +--------------------+---------+----------------------+
    | ``9714``           | hex     | status word          |
    +--------------------+---------+----------------------+
    | ``-0.001605376``   | s       | clock offset         |
    +--------------------+---------+----------------------+
    | ``0.000000000``    | s       | roundtrip delay      |
    +--------------------+---------+----------------------+
    | ``0.001424877``    | s       | dispersion           |
    +--------------------+---------+----------------------+
    | ``0.000958674``    | s       | RMS jitter           |
    +--------------------+---------+----------------------+

    The status field is encoded in hex format as described in Appendix B
    of the NTP specification RFC 1305.

.. option:: protostats

    Record significant peer, system and [rptpcp; events. Each
    significant event appends one line to the ``protostats`` file set:
    ``49213 525.624 128.4.1.1 963a 8a message``
    +-----------------+---------+-------------------------------------------+
    | Item            | Units   | Description                               |
    +-----------------+---------+-------------------------------------------+
    | ``49213``       | MJD     | date                                      |
    +-----------------+---------+-------------------------------------------+
    | ``525.624``     | s       | time past midnight                        |
    +-----------------+---------+-------------------------------------------+
    | ``128.4.1.1``   | IP      | source address (``0.0.0.0`` for system)   |
    +-----------------+---------+-------------------------------------------+
    | ``963a``        | code    | status word                               |
    +-----------------+---------+-------------------------------------------+
    | ``8a``          | code    | event message code                        |
    +-----------------+---------+-------------------------------------------+
    | ``message``     | text    | event message                             |
    +-----------------+---------+-------------------------------------------+

    The event message code and ``message`` field are described on the
    :doc:`Event Messages and Status Words
    <decode>` page.

.. option:: rawstats

    Record timestamp statistics. Each NTP packet received appends one
    line to the ``rawstats`` file set:
    ``56285 54575.160 128.4.1.1 192.168.1.5 3565350574.400229473 3565350574.442385200 3565350574.442436000 3565350575.154505763 0 4 4 1 8 -21 0.000000 0.000320 .PPS.``
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | Item                       | Units                                | Description                                            |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``56285``                  | MJD                                  | date                                                   |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``54575.160``              | s                                    | time past midnight                                     |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``128.4.1.1``              | IP                                   | source address                                         |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``192.168.1.5``            | IP                                   | destination address                                    |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``3565350574.400229473``   | NTP s                                | origin timestamp                                       |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``3565350574.442385200``   | NTP s                                | receive timestamp                                      |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``3565350574.442436000``   | NTP s                                | transmit timestamp                                     |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``3565350575.154505763``   | NTP s                                | destination timestamp                                  |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``0``                      | 0: OK, 1: insert pending,            | leap warning indicator                                 |
    |                            | 2: delete pending, 3: not synced     |                                                        |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``4``                      | 4 was current in 2012                | NTP version                                            |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``4``                      | 3: client, 4: server, 5: broadcast   | mode                                                   |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``1``                      | 1-15, 16: not synced                 | stratum                                                |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``8``                      | log\ :sub:`2` seconds                | poll                                                   |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``-21``                    | log\ :sub:`2` seconds                | precision                                              |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``0.000000``               | seconds                              | total roundtrip delay to the primary reference clock   |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``0.000320``               | seconds                              | total dispersion to the primary reference clock        |
    +----------------------------+--------------------------------------+--------------------------------------------------------+
    | ``PPS.``                   | IP or text                           | refid, association ID                                  |
    +----------------------------+--------------------------------------+--------------------------------------------------------+

.. option:: sysstats

    Record system statistics. Each hour one line is appended to the
    ``sysstats`` file set in the following format:
    ``50928 2132.543 3600 81965 0 9546 56 512 540 10 4 147 1``
    +----------------+---------+------------------------------+
    | Item           | Units   | Description                  |
    +----------------+---------+------------------------------+
    | ``50928``      | MJD     | date                         |
    +----------------+---------+------------------------------+
    | ``2132.543``   | s       | time past midnight           |
    +----------------+---------+------------------------------+
    | ``3600``       | s       | time since reset             |
    +----------------+---------+------------------------------+
    | ``81965``      | #       | packets received             |
    +----------------+---------+------------------------------+
    | ``0``          | #       | packets for this host        |
    +----------------+---------+------------------------------+
    | ``9546``       | #       | current versions             |
    +----------------+---------+------------------------------+
    | ``56``         | #       | old version                  |
    +----------------+---------+------------------------------+
    | ``512``        | #       | access denied                |
    +----------------+---------+------------------------------+
    | ``540``        | #       | bad length or format         |
    +----------------+---------+------------------------------+
    | ``10``         | #       | bad authentication           |
    +----------------+---------+------------------------------+
    | ``4``          | #       | declined                     |
    +----------------+---------+------------------------------+
    | ``147``        | #       | rate exceeded                |
    +----------------+---------+------------------------------+
    | ``1``          | #       | kiss-o'-death packets sent   |
    +----------------+---------+------------------------------+

.. option:: timingstats

    (Only available when the deamon is compiled with process time
    debugging support (--enable-debug-timing - costs performance).
    Record processing time statistics for various selected code paths.
    ``53876 36.920 10.0.3.5 1 0.000014592 input processing delay``
    +-------------------+---------+--------------------------------------+
    | Item              | Units   | Description                          |
    +-------------------+---------+--------------------------------------+
    | ``53876``         | MJD     | date                                 |
    +-------------------+---------+--------------------------------------+
    | ``36.920``        | s       | time past midnight                   |
    +-------------------+---------+--------------------------------------+
    | ``10.0.3.5``      | IP      | server address                       |
    +-------------------+---------+--------------------------------------+
    | ``1``             | #       | event count                          |
    +-------------------+---------+--------------------------------------+
    | ``0.000014592``   | s       | total time                           |
    +-------------------+---------+--------------------------------------+
    | ``message``       | text    | code path description (see source)   |
    +-------------------+---------+--------------------------------------+
