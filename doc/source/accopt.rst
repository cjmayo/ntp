Access Control Commands and Options
===================================

Commands and Options
--------------------

Unless noted otherwise, further information about these commands is on
the :doc:`Access Control Support <accopt>` page.

.. _accopt-discard:

.. confval:: discard [ average <avg> ][ minimum <min> ] [ monitor <prob> ]

    Set the parameters of the rate control facility which protects the
    server from client abuse. If the ``limited`` flag is present in the
    ACL, packets that violate these limits are discarded. If, in
    addition, the ``kod`` flag is present, a kiss-o'-death packet is
    returned. See the :doc:`Rate Management <rate>` page for further
    information. The options are:

    .. confval:: average <avg>

        Specify the minimum average interpacket spacing (minimum average
        headway time) in log\ :sub:`2` s with default 3.

    .. confval:: minimum <min>

        Specify the minimum interpacket spacing (guard time) in seconds
        with default 2.

    .. confval:: monitor <prob>

        Specify the probability of being recorded for packets that
        overflow the MRU list size limit set by ``mru maxmem`` or
        ``mru maxdepth``. This is a performance optimization for servers
        with aggregate arrivals of 1000 packets per second or more.

.. _accopt-restrict:

.. confval::
    restrict default [flag][...]
    restrict source [flag][...]
    restrict <address> [mask <mask>] [flag][...]

    The ``address`` argument expressed in dotted-quad form is the
    address of a host or network. Alternatively, the ``address``
    argument can be a valid host DNS name. The ``mask`` argument
    expressed in IPv4 or IPv6 numeric address form defaults to all mask
    bits on, meaning that the ``address`` is treated as the address of
    an individual host. A default entry (address 0.0.0.0, mask 0.0.0.0
    for IPv4 and address :: mask :: for IPv6) is always the first entry
    in the list. ``restrict default``, with no mask option, modifies
    both IPv4 and IPv6 default entries. ``restrict source`` configures a
    template restriction automatically added at runtime for each
    association, whether configured, ephemeral, or preemptible, and
    removed when the association is demobilized.
    Some flags have the effect to deny service, some have the effect to
    enable service and some are conditioned by other flags. The flags.
    are not orthogonal, in that more restrictive flags will often make
    less restrictive ones redundant. The flags that deny service are
    classed in two categories, those that restrict time service and
    those that restrict informational queries and attempts to do
    run-time reconfiguration of the server. One or more of the following
    flags may be specified:

    .. confval:: flake

        Discard received NTP packets with probability 0.1; that is, on
        average drop one packet in ten. This is for testing and
        amusement. The name comes from Bob Braden's *flakeway*, which
        once did a similar thing for early Internet testing.

    .. confval:: ignore

        Deny packets of all kinds, including ``ntpq`` and ``ntpdc``
        queries.

    .. confval:: kod

        Send a kiss-o'-death (KoD) packet if the ``limited`` flag is
        present and a packet violates the rate limits established by the
        ``discard`` command. KoD packets are themselves rate limited for
        each source address separately. If the ``kod`` flag is used in a
        restriction which does not have the ``limited`` flag, no KoD
        responses will result.

    .. _accopt-limited:

    .. confval:: limited

        Deny time service if the packet violates the rate limits
        established by the ``discard`` command. This does not apply to
        ``ntpq`` and ``ntpdc`` queries.

    .. confval:: lowpriotrap

        Declare traps set by matching hosts to be low priority. The
        number of traps a server can maintain is limited (the current
        limit is 3). Traps are usually assigned on a first come, first
        served basis, with later trap requestors being denied service.
        This flag modifies the assignment algorithm by allowing low
        priority traps to be overridden by later requests for normal
        priority traps.

    .. confval:: mssntp

        Enable Microsoft Windows MS-SNTP authentication using Active
        Directory services. **Note: Potential users should be aware that
        these services involve a TCP connection to another process that
        could potentially block, denying services to other users.
        Therefore, this flag should be used only for a dedicated server
        with no clients other than MS-SNTP.**

    .. confval:: nomodify

        Deny ``ntpq`` and ``ntpdc`` queries which attempt to modify the
        state of the server (i.e., run time reconfiguration). Queries
        which return information are permitted.

    .. confval:: noquery

        Deny ``ntpq`` and ``ntpdc`` queries. Time service is not
        affected.

    .. confval:: nopeer

        Deny packets that might mobilize an association unless
        authenticated. This includes broadcast, symmetric-active and
        manycast server packets when a configured association does not
        exist. It also includes ``pool`` associations, so if you want to
        use servers from a ``pool`` directive and also want to use
        ``nopeer`` by default, you'll want a ``"restrict source ..."``
        line as well that does *not* include the ``nopeer`` directive.
        Note that this flag does not apply to packets that do not
        attempt to mobilize an association.

    .. confval:: noserve

        Deny all packets except ``ntpq`` and ``ntpdc`` queries.

    .. confval:: notrap

        Decline to provide mode 6 control message trap service to
        matching hosts. The trap service is a subsystem of the ``ntpdc``
        control message protocol which is intended for use by remote
        event logging programs.

    .. confval:: notrust

        Deny packets that are not cryptographically authenticated. Note
        carefully how this flag interacts with the ``auth`` option of
        the ``enable`` and ``disable`` commands. If ``auth`` is enabled,
        which is the default, authentication is required for all packets
        that might mobilize an association. If ``auth`` is disabled, but
        the ``notrust`` flag is not present, an association can be
        mobilized whether or not authenticated. If ``auth`` is disabled,
        but the ``notrust`` flag is present, authentication is required
        only for the specified address/mask range.

    .. confval:: ntpport

        This is actually a match algorithm modifier, rather than a
        restriction flag. Its presence causes the restriction entry to
        be matched only if the source port in the packet is the standard
        NTP UDP port (123). A restrict line containing ``ntpport`` is
        considered more specific than one with the same address and
        mask, but lacking ``ntpport``.

    .. confval:: version

        Deny packets that do not match the current NTP version.

    Default restriction list entries with the flags ``ignore, ntpport``,
    for each of the local host's interface addresses are inserted into
    the table at startup to prevent the server from attempting to
    synchronize to its own time. A default entry is also always present,
    though if it is otherwise unconfigured; no flags are associated with
    the default entry (i.e., everything besides your own NTP server is
    unrestricted).
