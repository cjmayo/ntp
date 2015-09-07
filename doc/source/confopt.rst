Server Commands and Options
===========================

.. _confopt-address:

Server and Peer Addresses
--------------------------------------------------------

Following is a description of the server configuration commands in
NTPv4. There are two classes of commands, configuration commands that
configure an association with a remote server, peer or reference clock,
and auxiliary commands that specify environment variables that control
various related operations.

The various modes described on the
:doc:`Association Management
<assoc>` page are determined by the command
keyword and the DNS name or IP address. Addresses are classed by type as
(s) a remote server or peer (IPv4 class A, B and C or IPv6), (b) the
IPv4 broadcast address of a local interface, (m) a multicast address
(IPv4 class D or IPv6), or (r) a reference clock address (127.127.x.x).
For type m addresses the IANA has assigned the multicast group address
IPv4 224.0.1.1 and IPv6 ff05::101 (site local) exclusively to NTP, but
other nonconflicting addresses can be used.

If the Basic Socket Interface Extensions for IPv6 (:rfc:`2553`) is
detected, support for the IPv6 address family is generated in addition
to the default IPv4 address family. IPv6 addresses can be identified by
the presence of colons ":" in the address field. IPv6 addresses can be
used almost everywhere where IPv4 addresses can be used, with the
exception of reference clock addresses, which are always IPv4. Note that
in contexts where a host name is expected, a ``-4`` qualifier preceding
the host name forces DNS resolution to the IPv4 namespace, while a
``-6`` qualifier forces DNS resolution to the IPv6 namespace.

.. _confopt-command:

Server Commands
----------------------------------------------

Unless noted otherwise, further information about these commands is on
the :doc:`Association Management <assoc>` page.

.. _confopt-server:

::

  server address [options ...]
  peer address [options ...]
  broadcast address [options ...]
  manycastclient address [options ...]
  pool address [options ...]
  unpeer [address | associd]

These commands specify the remote server name or address to be used
and the mode in which to operate. The *address* can be either a DNS
name or a IPv4 or IPv6 address in standard notation. In general,
multiple commands of each type can be used for different server and
peer addresses or multicast groups.

.. confval:: server

        For type s and r addresses (only), this command mobilizes a
        persistent client mode association with the specified remote
        server or local reference clock. If the ``preempt`` flag is
        specified, a preemptable client mode association is mobilized
        instead.

.. _confopt-peer:

.. confval:: peer

        For type s addresses (only), this command mobilizes a persistent
        symmetric-active mode association with the specified remote
        peer.

.. _confopt-broadcast:

.. confval:: broadcast

        For type b and m addressees (only), this command mobilizes a
        broadcast or multicast server mode association. Note that type b
        messages go only to the interface specified, but type m messages
        go to all interfaces.

.. _confopt-manycastclient:

.. confval:: manycastclient

        For type m addresses (only), this command mobilizes a
        preemptable manycast client mode association for the multicast
        group address specified. In this mode the address must match the
        address specified on the ``manycastserver`` command of one or
        more designated manycast servers. Additional information about
        this command is on the :ref:`Automatic
        Server Discovery <discover-mcst>` page.

.. _confopt-pool:

.. confval:: pool

        For type s addresses (only) this command mobilizes a preemptable
        pool client mode association for the DNS name specified. The DNS
        name must resolve to one or more IPv4 or IPv6 addresses.
        Additional information about this command is on the
        :ref:`Automatic Server Discovery <discover-pool>` page. The
        `www.pool.ntp.org <http://www.pool.ntp.org/>`__ page describes a
        compatible pool of public NTP servers.

.. _confopt-unpeer:

.. confval:: unpeer

        This command removes a previously configured association. An
        address or association ID can be used to identify the
        association. Either an IP address or DNS name can be used. This
        command is most useful when supplied via
        :doc:`ntpq  <ntpq>` runtime configuration commands
        ``:config`` and ``config-from-file``.

.. _confopt-option:

Server Command Options
----------------------------------------------------

.. confval:: autokey

    Send and receive packets authenticated by the Autokey scheme
    described on the :doc:`Autokey Public Key
    Authentication <autokey>` page. This option
    is mutually exclusive with the ``key`` option.

.. _confopt-burst:

.. confval:: burst

    When the server is reachable, send a burst of packets instead of the
    usual one. This option is valid only with the ``server`` command and
    type s addresses. It is a recommended option when the ``maxpoll``
    option is greater than 10 (1024 s). Additional information about
    this option is on the :doc:`Poll Program <poll>` page.

.. confval:: iburst

    When the server is unreachable, send a burst of packets instead of
    the usual one. This option is valid only with the ``server`` command
    and type ``s`` addresses. It is a recommended option with this
    command. Additional information about this option is on the
    :doc:`Poll Program <poll>` page.

.. confval:: ident <group>

    Specify the group name for the association. See the
    :doc:`Autokey Public-Key Authentication
    <autokey>` page for further information.

.. confval:: key <key>

    Send and receive packets authenticated by the symmetric key scheme
    described in the :doc:`Authentication Support <authentic>` page.
    The ``<key>``
    specifies the key identifier with values from 1 to 65534, inclusive.
    This option is mutually exclusive with the ``autokey`` option.

.. confval:: minpoll <minpoll>

.. confval:: maxpoll <maxpoll>

    These options specify the minimum and maximum poll intervals for NTP
    messages, in seconds as a power of two. The maximum poll interval
    defaults to 10 (1024 s), but can be increased by the ``maxpoll``
    option to an upper limit of 17 (36 hr). The minimum poll interval
    defaults to 6 (64 s), but can be decreased by the ``minpoll`` option
    to a lower limit of 3 (8 s). Additional information about this
    option is on the :doc:`Poll Program
    <poll>` page.

.. confval:: mode <option>

    Pass the ``option`` to a reference clock driver, where ``option`` is
    an integer in the range from 0 to 255, inclusive. This option is
    valid only with type r addresses.

.. confval:: noselect

    Marks the server or peer to be ignored by the selection algorithm as
    unreachable, but visible to the monitoring program. This option is
    valid only with the ``server`` and ``peer`` commands.

.. confval:: preempt

    Specifies the association as preemptable rather than the default
    persistent. This option is ignored with the ``broadcast`` command
    and is most useful with the ``manycastclient`` and ``pool``
    commands.

.. confval:: prefer

    Mark the server as preferred. All other things being equal, this
    host will be chosen for synchronization among a set of correctly
    operating hosts. See the :doc:`Mitigation
    Rules and the prefer Keyword <prefer>` page
    for further information. This option is valid only with the
    ``server`` and ``peer`` commands.

.. confval:: true

    Mark the association to assume truechimer status; that is, always
    survive the selection and clustering algorithms. This option can be
    used with any association, but is most useful for reference clocks
    with large jitter on the serial port and precision pulse-per-second
    (PPS) signals. Caution: this option defeats the algorithms designed
    to cast out falsetickers and can allow these sources to set the
    system clock. This option is valid only with the ``server`` and
    ``peer`` commands.

.. confval:: ttl <ttl>

    This option specifies the time-to-live ``ttl`` for the ``broadcast``
    command and the maximum ``ttl`` for the expanding ring search used
    by the ``manycastclient`` command. Selection of the proper value,
    which defaults to 127, is something of a black art and should be
    coordinated with the network administrator. This option is invalid
    with type r addresses.

.. confval:: version <version>

    Specifies the version number to be used for outgoing NTP packets.
    Versions 1-4 are the choices, with version 4 the default.

.. confval:: xleave

    Operate in interleaved mode (symmetric and broadcast modes only).
    Further information is on the :doc:`NTP
    Interleaved Modes <xleave>` page.

.. _confopt-aux:

Auxiliary Commands
---------------------------------------------

.. _confopt-broadcastclient:

.. confval:: broadcastclient

    Enable reception of broadcast server messages to any local interface
    (type b address). Ordinarily, upon receiving a broadcast message for
    the first time, the broadcast client measures the nominal server
    propagation delay using a brief client/server exchange, after which
    it continues in listen-only mode. If a nonzero value is specified in
    the ``broadcastdelay`` command, the value becomes the delay and the
    volley is not executed. Note: the ``novolley`` option has been
    deprecated for future enhancements. Note that, in order to avoid
    accidental or malicious disruption in this mode, both the server and
    client should operate using symmetric key or public key
    authentication as described in the
    :doc:`Authentication Options <authopt>` page. Note that the volley is
    required with public key authentication in order to run the Autokey
    protocol.

.. _confopt-manycastserver:

.. confval:: manycastserver <address> [...]

    Enable reception of manycast client messages (type m) to the
    multicasts group address(es) (type m) specified. At least one
    address is required. Note that, in order to avoid accidental or
    malicious disruption, both the server and client should operate
    using symmetric key or public key authentication as described in the
    :doc:`Authentication Options <authopt>` page.

.. _confopt-multicastclient:

.. confval:: multicastclient <address> [...]

    Enable reception of multicast server messages to the multicast group
    address(es) (type m) specified. Upon receiving a message for the
    first time, the multicast client measures the nominal server
    propagation delay using a brief client/server exchange with the
    server, then enters the broadcast client mode, in which it
    synchronizes to succeeding multicast messages. Note that, in order
    to avoid accidental or malicious disruption in this mode, both the
    server and client should operate using symmetric key or public key
    authentication as described in the
    :doc:`Authentication Options <authopt>` page.

.. _confopt-mdnstries:

.. confval:: mdnstries <number>

    If we are participating in mDNS, after we have synched for the first
    time we attempt to register with the mDNS system. If that
    registration attempt fails, we try again at one minute intervals for
    up to ``mdnstries`` times. After all, ``ntpd`` may be starting
    before mDNS. The default value for ``mdnstries`` is 5.
